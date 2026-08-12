# Openmind

> **Open-source systems project for connecting context, information, automation, and intelligent capabilities through a deliberately small, inspectable architecture.**

Openmind is the **engineering layer of my public portfolio** and the single open-source project I am building publicly.

The project is intentionally built from real historical engineering evidence, but the public repository only keeps work that can be explained, implemented, tested, and maintained as part of Openmind.

**Open source is the development model. Openmind is the project.**

## Why Openmind exists

Modern knowledge work is fragmented across documents, applications, APIs, workflows, and AI tools. The engineering problem is not simply adding another AI feature or another integration. It is creating useful boundaries between **context, knowledge, external systems, automation, and intelligent capabilities** without producing an unmaintainable integration mesh.

Openmind explores that problem through incremental implementation.

**Problem → requirements → boundaries → implementation → tests → evidence → iteration**

## Current implementation

The first implemented capability is a **provider-neutral connection registry**.

It establishes a small domain boundary for external connections before provider-specific integrations are introduced.

### What is implemented

- Typed `Connection` domain model
- Input validation for required identifiers
- Capability normalization and de-duplication
- Immutable connection records
- Provider-based lookup
- Capability-based lookup
- Duplicate registration protection
- Connection disable operation
- Connection removal
- Automated tests for core behaviour
- Strict TypeScript configuration

### Why this is the first increment

The historical project corpus repeatedly showed the same architectural risk: external providers, authentication, APIs, AI models, automation, and business logic can become tightly coupled when they are introduced too early.

Openmind therefore starts with a small boundary:

```text
Openmind domain
      │
      ▼
Connection Registry
      │
      ▼
Provider Adapter
      │
      ▼
External System
```

The registry does not know how GitHub, Notion, an AI provider, or another service authenticates or communicates. Those concerns belong behind an adapter boundary.

That keeps the core replaceable and makes future integrations easier to reason about.

## Proof of work

The repository now contains inspectable implementation rather than only architecture documentation.

### Source

- [`src/domain/connection.ts`](src/domain/connection.ts) — domain model and validation
- [`src/core/connection-registry.ts`](src/core/connection-registry.ts) — registry behaviour

### Tests

- [`tests/connection-registry.test.ts`](tests/connection-registry.test.ts) — registration, duplicate protection, filtering, and lifecycle behaviour

### Configuration

- [`package.json`](package.json) — executable test/type-check commands
- [`tsconfig.json`](tsconfig.json) — strict TypeScript settings

### Local verification

The current implementation has been compiled with TypeScript and exercised with a smoke test covering registration, provider/capability lookup, disable behaviour, and duplicate protection.

The repository will treat CI as the canonical repeatable verification path as the implementation surface expands.

## Engineering evidence from the historical corpus

Openmind is not being invented from scratch for presentation. The historical project corpus contains real work covering:

- TypeScript / Next.js application architecture
- Authentication and session management
- Authorization and policy concepts
- Prisma / database modelling
- API and integration boundaries
- AES-256-GCM encryption and secret handling
- Rate limiting and audit logging
- AI model abstraction and retrieval patterns
- Workflow orchestration
- Docker deployment
- CI and repository engineering practices
- Architecture, module, delivery, and deployment documentation

Examples from the historical corpus are being used selectively. A capability enters Openmind only when it satisfies an actual project requirement.

## Architecture direction

```text
User / Workflow
      │
      ▼
Application / API
      │
      ▼
Domain capabilities
      │
 ┌────┼──────────────┐
 ▼    ▼              ▼
Context  AI       Automation
 │       │              │
 └───────┼──────────────┘
         ▼
Connection / Integration Boundary
         │
         ▼
External Systems
         │
         ▼
Data · Security · Observability
```

The architecture is intentionally evolutionary. A diagram is not evidence that a component exists; source code and tests determine implementation status.

## Engineering state model

| State | Meaning |
|---|---|
| **Planned** | Intended, not implemented |
| **Designed** | Architecture / approach defined |
| **Implemented** | Working code exists |
| **Tested** | Defined tests have been executed |
| **Deployed** | Running in a real environment |
| **Validated** | Evidence supports the stated result |

The current connection registry is **Implemented** and **Tested locally**. It is not being described as deployed or production-validated.

## Roadmap

### Near term

1. Provider adapter interface
2. Connection persistence boundary
3. Credential / secret boundary
4. Audit events for connection lifecycle
5. CI-based type checking and tests

### Later, only if justified

- API layer
- External provider adapters
- AI provider abstraction
- Context and knowledge services
- Workflow execution
- Observability
- Deployment

The roadmap is deliberately conditional. Scope expands only when the preceding boundary is useful and validated.

## Documentation

- [`docs/architecture.md`](docs/architecture.md) — system boundaries and architectural principles
- [`docs/evidence.md`](docs/evidence.md) — evidence and maturity rules

## Audience

**Recruiter / hiring manager:** see the problem, current implementation, and proof of work.

**Business / operations leader:** understand why the boundary matters and what operational problem it can support.

**Engineer / architect:** inspect the domain model, registry implementation, tests, architecture and trade-offs.

**Senior technical reviewer:** evaluate scope control, separation of concerns, evidence discipline, and implementation quality.

## Evidence discipline

No invented users, revenue, adoption, production scale, security guarantees, or business impact.

Claims should remain traceable to **source code, tests, reproducible behaviour, architecture decisions, or deployment evidence**.

---

**Principle:** build something real, explain why it exists, make the engineering inspectable, and let evidence create the credibility.
