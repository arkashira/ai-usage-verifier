# REQUIREMENTS.md

## Overview
The `ai-usage-verifier` is a standardized tool developed by Axentx to authenticate and verify AI usage within software products or services. It enables developers, marketers, and consumers to validate claims of AI integration with cryptographic and audit-ready proofing mechanisms. This document outlines the functional, non-functional, and operational requirements for a shippable v1.0 release.

All development occurs under the `arkashira/ai-usage-verifier` repository. The implementation must integrate with the shared BRAIN (pgvector) for knowledge persistence and leverage existing C. Frameworks (vLLM, SGLang) where applicable.

---

## Functional Requirements

### FR-1: AI Usage Declaration Schema
The system SHALL provide a standardized JSON/YAML schema (`ai_usage_manifest.json`) that describes:
- AI components used (e.g., model name, version, provider)
- Inference method (on-premise, cloud, edge)
- Training data source (public, synthetic, proprietary)
- Intended use case and ethical constraints
- Compliance flags (GDPR, CCPA, AI Act)

This schema MUST be versioned and published in the repo under `/schemas/v1`.

### FR-2: Cryptographic Attestation
The system SHALL generate a tamper-evident attestation token (JWT-based) signed by the developer’s private key, binding:
- The manifest hash
- Timestamp of generation
- Developer identity (DID or GitHub OIDC)
- Deployment environment fingerprint (optional)

Attestation tooling MUST be CLI-accessible via `ai-verify attest --manifest=...`.

### FR-3: Public Verification Endpoint
The system SHALL expose a public REST endpoint (`POST /verify`) that:
- Accepts a base64-encoded attestation token
- Validates the cryptographic signature
- Returns structured JSON response indicating:
  - `valid: boolean`
  - `issuer: string (DID/GitHub handle)`
  - `manifest_summary: object`
  - `warnings: string[]` (e.g., deprecated model, untrusted source)

Endpoint MUST support CORS for integration with third-party marketplaces.

### FR-4: Local CLI Verification
The system SHALL include a CLI command `ai-verify verify <token>` that:
- Parses and validates the token offline
- Checks revocation status via embedded CRL or OCSP-like mechanism
- Outputs human-readable report to stdout
- Exits with code 0 if valid, non-zero otherwise

### FR-5: Revocation Registry
The system SHALL maintain a revocation registry (on-chain or IPFS-backed) where developers can:
- Revoke compromised or misused attestations
- Publish revocation reasons (security breach, ethical violation)

CLI command `ai-verify revoke <token_id>` MUST be provided.

### FR-6: Integration with Existing Axentx Pipeline
The system SHALL:
- Store generated manifests and attestations in the shared BRAIN (pgvector) with metadata tags
- Emit events to the validation queue for BD/HR review when new AI usage is declared
- Support auto-injection into PRD and QA stages via CI/CD hooks

Manifests MUST be retrievable via `GET /brain/ai_usage?product_id=...`.

### FR-7: Transparency Dashboard
The system SHALL serve a lightweight web dashboard (`/dashboard`) that:
- Lists all verified AI usages across the Axentx portfolio
- Shows real-time validation stats (total attestations, revocations, top models)
- Allows filtering by team, product, model type

Dashboard MUST be embeddable via iframe for internal use.

---

## Non-Functional Requirements

### Performance
- Attestation generation: ≤ 100ms latency (p95)
- Public verification: ≤ 200ms latency (p95), even under 10k RPM
- Dashboard load time: ≤ 1s with 10k entries

### Security
- Private keys MUST NOT be handled by the server; signing occurs client-side or in trusted environment
- All tokens MUST use ES256 or equivalent quantum-resistant algorithm
- Revocation registry MUST be append-only and auditable
- No PII stored in logs or manifests without explicit opt-in

### Reliability
- Service uptime: 99.9% SLA (monitored via uptime checker)
- Attestation data backed up hourly to cold storage
- Zero-downtime deployments via blue-green strategy

### Scalability
- Support up to 1M attestations in registry within first 6 months
- Horizontal scaling of verification API via Kubernetes deployment
- Indexing of BRAIN entries optimized for <50ms lookup at scale

### Maintainability
- Full test coverage (≥90%) for core logic (attestation, verification)
- CI/CD pipeline in `.github/workflows` with lint, test, security scan
- OpenAPI spec (`/openapi.yaml`) auto-generated and versioned

---

## Constraints

- Language: Python 3.11+ (aligns with vLLM/SGLang stack)
- Framework: FastAPI for REST endpoints
- Deployment: Containerized via Docker, orchestrated on K8s
- Authentication: GitHub OIDC for developer identity
- Data storage: PostgreSQL for registry, pgvector for BRAIN sync
- Licensing: Apache-2.0 (consistent with instr-resp datasets)

No external model hosting; only verification of usage claims.

---

## Assumptions

- Developers have basic PKI tooling (e.g., `ssh-keygen`, `openssl`) or use integrated keygen (`ai-verify keys generate`)
- Consumers trust the issuer's identity if signature validates
- Model versioning is accurate and provided truthfully in manifest
- The Axentx BRAIN is always reachable during pipeline execution
- Regulatory landscape (e.g., EU AI Act) remains stable through v1.0 lifecycle

---

## Out of Scope

- Real-time model behavior monitoring
- Dynamic AI usage detection (e.g., reverse-engineering binaries)
- Financial payment or licensing enforcement
- Legal liability for false claims

--- 

*Document status: Draft v0.9 — Approved for implementation*
