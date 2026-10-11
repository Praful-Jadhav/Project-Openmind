# Openmind — Zero-Trust Development Contract

**Status:** Mandatory working rule. This repository is a public, provider-neutral connection-registry prototype. Public visibility is intentional; private ecosystem records, credentials and operational secrets are not.

## Trust rule
AI-generated code, files, test results, repository badges and prior summaries are untrusted until independently verified. The existence of code or a few lines in a file does not prove that a capability works. Do not claim completion because a model or tool says so.

## Completion statuses
DRAFT, IN_PROGRESS, BLOCKED, FAILED, VERIFIED, VALIDATED, ACCEPTED, ACCEPTED_RISK, DEFERRED. Missing evidence is UNKNOWN. VERIFIED means technical checks passed on a specific revision; VALIDATED means the intended behavior/outcome passed; ACCEPTED requires both plus review by an accountable owner.

## Material-change evidence
Changes to source, tests, packages, workflow files or the public claims in README require a source-controlled packet under docs/evidence/. Packets must identify task, owner, risk, scope, acceptance criteria, verification, validation, privacy/security, limitations, recovery and tested revision. The CI gate checks presence and structure only; it does not prove the packet's claims.

## Security and scope
- Never commit secrets, private URLs, live customer details, provider tokens or privileged credentials.
- Treat external provider responses and registry metadata as untrusted data.
- Validate input and authorization at the trusted boundary; frontend-only checks are insufficient.
- Preserve provider neutrality; no credential should be exposed through examples, logs or tests.
- Do not call the repository production-ready until runtime, auth, abuse/failure handling, deployment, recovery and real-user journey have been verified.

A failed check is a finding, not a reason to weaken the gate.