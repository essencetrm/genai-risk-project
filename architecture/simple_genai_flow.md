
# Simple GenAI Flow Architecture

This document describes the basic interaction flow of a GenAI system
as observed for risk analysis purposes.

Flow:
1. User Input
2. System Prompt / Guardrails
3. Model Inference
4. Output Generation
5. Logging & Observation

Risk Entry Points:
- User input can influence model behavior
- Model may override instructions (Prompt Injection)
- Model may expose protected context (Data Leakage)

This architecture is used as the baseline for all risk testing
performed in this repository.
