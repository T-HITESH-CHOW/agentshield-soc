# AgentShield SOC

> **Evidence-first. Evaluation-driven. AI-assisted security operations.**

AgentShield SOC is an open-source research and portfolio project exploring how AI agents can assist Security Operations Centers (SOCs) without turning security decisions into opaque AI guesses.

The core principle is simple:

> **Every AI security verdict should be explainable, evidence-backed, and measurable.**

Instead of treating an LLM response as the final authority, AgentShield is designed around evidence collection, counter-evidence, confidence, structured reasoning metadata, analyst feedback, and measurable evaluation.

---

## ⚠️ Project Status

**Early development — architecture and frontend foundation**

AgentShield SOC is currently under active development.

Implemented so far:

- Repository foundation
- FastAPI backend foundation
- Next.js / TypeScript frontend foundation
- SOC dashboard interface
- Alerts interface
- Cases interface
- Investigations interface
- Verdict Lab interface
- Evaluation interface
- Settings interface
- Evidence-first empty states

Not implemented yet:

- Real security telemetry ingestion
- Detection engine
- Alert correlation
- Risk scoring
- PostgreSQL persistence
- AI investigation
- Threat intelligence enrichment
- MITRE ATT&CK integration
- Analyst feedback pipeline
- TP/TN/FP/FN evaluation
- Automated response

The interface intentionally avoids fabricating security telemetry or AI results before those systems exist.

---

## 🎯 Vision

Traditional SOC workflows can involve large volumes of alerts, fragmented evidence, manual investigation, and inconsistent analyst decisions.

AgentShield explores an alternative:

```text
Security Telemetry
        │
        ▼
   Normalization
        │
        ▼
    Detection
        │
        ▼
   Correlation
        │
        ▼
    Risk Score
        │
        ▼
      Case
        │
        ▼
 Evidence Collection
        │
        ▼
 AI Investigation
        │
        ▼
  Verdict Engine
        │
        ├───────────────┐
        ▼               ▼
 MALICIOUS          BENIGN
        │
        └──────┐
               ▼
       Analyst Feedback
               │
               ▼
       Evaluation Lab
               │
               ▼
       TP / TN / FP / FN
