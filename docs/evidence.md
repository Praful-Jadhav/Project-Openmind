# Evidence Register

This page prevents the repository from confusing **capability evidence** with **claims about the current product**.

## Evidence categories

| Category | Meaning |
|---|---|
| Historical | Work completed before Openmind and retained as evidence / reference |
| Reused | Historical implementation deliberately incorporated into Openmind |
| New | Built specifically for Openmind |
| Verified | Reproduced or independently checked against a defined criterion |

## Historical engineering evidence

The project corpus reviewed for Openmind contains material covering:

- Next.js / TypeScript application architecture
- authentication and authorization flows
- Prisma schema and persistence design
- encryption-related implementation and tests
- security and deployment documentation
- API design and integration patterns
- AI model abstraction and retrieval concepts
- workflow automation and orchestration
- Docker-based deployment
- automated validation

These items establish that there is real prior technical work available for consolidation. They do **not** automatically prove that the corresponding capability exists in Openmind.

## First architectural evidence

The initial Openmind architecture document establishes explicit boundaries between:

- application / API
- domain capabilities
- context and knowledge
- AI
- automation
- data and external integrations
- infrastructure concerns

This is the first design artifact for the public project.

## Verification rule

Before a capability is described in the README as implemented, the repository should contain enough evidence for another technical reader to reproduce or inspect it.

Preferred evidence order:

1. source code
2. automated tests
3. reproducible local setup
4. executable demonstration
5. deployment evidence
6. documentation explaining the decision

## Claims deliberately excluded

The historical corpus contains broad claims about production readiness and test volume. Those claims are not repeated here unless the underlying implementation can be reproduced and verified.

This register therefore acts as a credibility control, not a marketing page.
