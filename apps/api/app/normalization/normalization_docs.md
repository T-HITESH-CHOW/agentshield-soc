# Event Normalization Documentation

## 1. Why Normalization Exists
In an evidence-first SOC environment, security events originate from diverse telemetry sources (Windows, Linux, Firewalls, EDRs), each using distinct formats and field names. Normalization exists to translate these disparate vendor-specific logs into a single, cohesive schema. This allows detection rules, correlations, and risk engines to operate universally without knowing the specifics of the original source format.

## 2. Fields in NormalizedEvent
The `NormalizedEvent` Pydantic schema acts as our universal language. It contains:
- `event_id`: Optional identifier for the event.
- `timestamp`: Timezone-aware datetime when the event occurred.
- `source` & `source_type`: Identifying where the event came from (e.g., windows, wazuh).
- `event_type`: Categorical grouping (e.g., authentication, network, process).
- `action`: Specific action occurring (e.g., login_success, connection_attempt).
- Identity context: `username`, `source_ip`, `destination_ip`, `hostname`.
- Execution context: `process`, `command_line`.
- `status`: Optional execution status.
- `raw_event`: Unaltered preservation of the original data.

## 3. Supported Windows Mappings
Currently, the deterministic Windows parser supports common authentication event mappings:
- **Event ID 4624**: Mapped to `event_type = authentication`, `action = login_success`.
- **Event ID 4625**: Mapped to `event_type = authentication`, `action = login_failed`.
It additionally maps fields like `AccountName` to `username`, `IpAddress` to `source_ip`, and `ComputerName` to `hostname`.

## 4. Handling Unknown/Missing Fields
The parser gracefully handles missing data. If an expected field is not present in the raw event, its mapped value in the `NormalizedEvent` becomes `None` (null). For categorization, if the parser encounters an unrecognizable event type or action, it defaults safely to the Enum value `unknown`. No data is hallucinated or invented to fill gaps.

## 5. Preservation of Raw Events
The pristine, unmodified `raw_event` is preserved explicitly in the `NormalizedEvent` model. This is critical in an evidence-first SOC because it maintains absolute forensic provenance. Analysts and investigators must be able to audit exactly what the original telemetry sent, without losing data to lossy translation phases or having to hunt down raw logs separately.

## 6. Deterministic vs LLM-Based Normalization
Security-critical pipeline normalization must remain deterministic. Using an LLM for initial event ingestion presents severe risks: non-deterministic execution times, unreliability, hallucination of data or fields, and susceptibility to prompt-injection attacks from malicious payloads embedded within logs. Parsers strictly utilize hard-coded dictionary mapping, regex, and aliases to ensure the process is safe, perfectly repeatable, and highly performant. LLMs are reserved strictly for high-level later-stage analytical assistance, not real-time ETL plumbing.
