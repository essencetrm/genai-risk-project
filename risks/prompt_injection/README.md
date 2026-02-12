# Prompt Injection Risk

Failure Type:
Instruction Override

Description:
User input overrides system-level intent,
leading to loss of behavioral control.

OWASP Mapping:
LLM01 – Prompt Injection


## Risk Classification (Week 3 day 4)
Failure type: Instruction Override
Security Principle impacted: Integrity

---

## Risk Statement 

If a GenAI system is permitted  to initiate or recommend actions without adequate human validation, it may exceed its intended aut resulting in unathorized operational decisions.

---

## Business Impact

### Legal

- Liability arising from autonomous decisions
- Regulatory challenges in high-risk AI environments

###  Trust 

- Loss of stakeholder confidence in AI oversight
- Perception of uncontrolled automation

### Compliance 

- Violation of human-in-loop requirements
- Breakdown of governace accountability structures

---

## High-Level Controls

- Human-in-the-loop approval mechanisms
- Action threshold enforcement
- Role-based authorization controls
- Clear system capability boundaries
- Governance documentation and review cycles

--- 

## Auditor Perspective

Excessive Agency is assessed as a governance failure.