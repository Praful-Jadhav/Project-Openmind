# Evidence Packet — Openmind Zero-Trust Gate

Task ID: OM-ZTG-001
Status: IN_PROGRESS
Accountable owner: Openmind maintainer
Risk tier: R2

## Claim and risk
Introduce an evidence requirement for material source, dependency and workflow changes. The principal risk is treating registry code that compiles as a production-safe integration boundary.

## Scope and acceptance criteria
In scope: local agent contract, CI, evidence validator, unit tests and evidence packet. Out of scope: production service/deployment, credential custody and external provider execution. Material source/tests/package/workflow/docs changes require a substantive packet; missing sections and unsupported acceptance statuses must fail.

## Verification plan and results
The PR workflow will install dependencies, run the packet validator tests, validate this packet, run registry tests and TypeScript typecheck. Exact candidate SHA and workflow result must be read back when the run completes. No PASS is asserted in advance.

## Validation plan and results
A future production claim requires real provider/auth tests and failure/recovery evidence beyond this static gate. This PR does not validate any external integration or real-world business outcome.

## Security and privacy
No live provider credentials or private personal/business details are used. Public repository content must remain safe for unrestricted readers.

## Limitations and open items
There was no existing CI workflow on main at audit time. No package lockfile was observed, so reproducible dependency installation remains open. This gate checks packet structure only, not evidence truth.

## Recovery and rollback
Revert the new workflow, script, tests and policy if the gate creates false positives or silently misses material files. No production system is changed.

## Evidence and tested revision
Record the exact PR head SHA and CI results after the run finishes. Keep status IN_PROGRESS until reviewed and accepted.
