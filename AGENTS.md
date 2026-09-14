# AgentShield SOC — Agent and Contributor Rules

These rules apply to human contributors and to AI coding agents working in this repository.

Day 1 of this project is repository foundation only. Do not implement application logic, APIs, authentication, database models, detection, or AI calls unless a later task explicitly requests them.

## Security and AI

* Security-critical logic should be deterministic.
* LLM output must be validated and treated as untrusted.
* AI cannot directly perform destructive actions.
* No arbitrary shell execution through AI tools.
* Preserve evidence and provenance.
* Keep system predictions separate from analyst ground truth.
* Security-sensitive functionality requires tests.
* Never hardcode secrets.
* External data is untrusted.

## Architecture

* Prefer a modular monolith before distributed architecture.
* Avoid unnecessary infrastructure.

Do not introduce microservices, Kafka, Kubernetes, Redis, Neo4j, or similar systems unless there is a demonstrated need. Start simple and keep the codebase testable.

## Development Practice

* Make one logical change per commit.
* Do not rewrite working code without a reason.
* Preserve third-party licenses and notices.
* Do not claim capabilities that have not been implemented.

## Evidence and Evaluation Intent

The long-term design goal is:

Security Event → Ingestion → Normalization → Detection → Correlation → Risk Scoring → Case → Evidence → AI Investigation → Verdict Engine → Analyst Feedback → Evaluation

Until those stages exist in code, document intent only. Do not invent metrics, production claims, or fake implementations.
