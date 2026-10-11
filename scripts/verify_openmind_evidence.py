#!/usr/bin/env python3
"""Require a substantive evidence packet for material Openmind changes."""
import json, os, re, subprocess, sys
from pathlib import Path
PREFIXES=("src/","tests/","scripts/",".github/workflows/","docs/")
FILES={"package.json","package-lock.json","README.md","tsconfig.json"}
HEADINGS=("## Claim and risk","## Scope and acceptance criteria","## Verification plan and results","## Validation plan and results","## Security and privacy","## Limitations and open items","## Recovery and rollback","## Evidence and tested revision")
STATUSES={"DRAFT","IN_PROGRESS","BLOCKED","FAILED","VERIFIED","VALIDATED","ACCEPTED","ACCEPTED_RISK","DEFERRED"}

def material(path):
    p=path.replace("\\","/")
    return p in FILES or any(p.startswith(x) for x in PREFIXES)

def validate_packet(text,path="<packet>"):
    errors=[]
    m=re.search(r"(?im)^Status:\s*([A-Z_]+)\s*$",text)
    status=m.group(1) if m else None
    if status not in STATUSES: errors.append(path+": missing/invalid Status")
    for field,pat in (("Task ID",r"(?im)^Task ID:\s*\S+"),("Accountable owner",r"(?im)^Accountable owner:\s*\S+"),("Risk tier",r"(?im)^Risk tier:\s*(R0|R1|R2|R3)\b")):
        if not re.search(pat,text): errors.append(path+": missing "+field)
    for h in HEADINGS:
        m=re.search(r"(?m)^"+re.escape(h)+r"\s*$",text)
        if not m: errors.append(path+": missing section "+h); continue
        n=re.search(r"(?m)^##\s+",text[m.end():]); end=m.end()+n.start() if n else len(text)
        body=text[m.end():end].strip()
        if len(re.sub(r"\s+|[>#*_\-\[\]]","",body))<18: errors.append(path+": empty section "+h)
        if re.search(r"(?i)\b(TODO|TBD|PLACEHOLDER|FILL\s+IN|WRITE\s+HERE)\b",body): errors.append(path+": unresolved placeholder in "+h)
    if status in {"VERIFIED","VALIDATED","ACCEPTED"}:
        for f in ("Verification status: PASS","Validation status: PASS","Independent read-back: PASS"):
            if not re.search(r"(?im)^"+re.escape(f)+r"\s*$",text): errors.append(path+": cannot be "+status+" without "+f)
        if not re.search(r"(?im)^Tested revision:\s*[0-9a-f]{7,40}\s*$",text): errors.append(path+": accepted status needs tested SHA")
        if not re.search(r"(?im)^Acceptance authority:\s*\S+",text): errors.append(path+": accepted status needs acceptance authority")
    if status=="ACCEPTED_RISK":
        for f in ("Risk acceptance owner:","Risk rationale:","Risk expiry:"):
            if not re.search(r"(?im)^"+re.escape(f)+r"\s*\S+",text): errors.append(path+": ACCEPTED_RISK needs "+f)
    if status=="DEFERRED":
        for f in ("Deferral reason:","Reconsider by:"):
            if not re.search(r"(?im)^"+re.escape(f)+r"\s*\S+",text): errors.append(path+": DEFERRED needs "+f)
    return errors

def get_changes(name,event):
    if name=="pull_request":
        base=event.get("pull_request",{}).get("base",{}).get("sha")
        if not base: raise ValueError("missing pull request base SHA")
        cmd=["git","diff","--name-only",base+"...HEAD"]
    elif name=="push":
        before,after=event.get("before",""),event.get("after","HEAD")
        cmd=(["git","ls-tree","-r","--name-only",after] if not before or set(before)=={"0"} else ["git","diff","--name-only",before,after])
    else: return []
    r=subprocess.run(cmd,check=True,capture_output=True,text=True)
    return [p.strip() for p in r.stdout.splitlines() if p.strip()]

def main():
    name=os.environ.get("GITHUB_EVENT_NAME","")
    if name not in {"pull_request","push"}: print("SKIP: no change diff."); return 0
    try:
        event=json.loads(Path(os.environ["GITHUB_EVENT_PATH"]).read_text(encoding="utf-8"))
        paths=get_changes(name,event)
    except Exception as e: print("FAIL: cannot establish candidate diff: "+str(e),file=sys.stderr); return 2
    code=[p for p in paths if material(p) and not p.startswith("docs/evidence/")]
    if not code: print("PASS: no material change needs evidence."); return 0
    packets=[p for p in paths if p.startswith("docs/evidence/") and p.endswith(".md")]
    if not packets:
        print("FAIL: material change without docs/evidence/*.md packet.")
        for p in code: print("- "+p)
        return 1
    errors=[]
    for p in packets:
        try: errors.extend(validate_packet(Path(p).read_text(encoding="utf-8"),p))
        except Exception as e: errors.append(p+": cannot read packet: "+str(e))
    if errors:
        print("FAIL: "+str(len(errors))+" issue(s)")
        for e in errors: print("- "+e)
        return 1
    print("PASS: "+str(len(code))+" material path(s), "+str(len(packets))+" packet(s); structural gate only.")
    return 0

if __name__=="__main__": raise SystemExit(main())
