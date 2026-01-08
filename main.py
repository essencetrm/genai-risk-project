# -------------------------
# Day 1: Risk Register Core
# -------------------------


"""
genai-risk-assessment-tool
Version: v0.1
Purpose: Practice Python while exploring OWASP GenAI risks
Author: The King
"""

# -------------------------
# Imports (later, not now)
# -------------------------


# -------------------------
# Constants / Configuration
# -------------------------

TOOL_NAME = "genai-risk-assessment-tool"
VERSION = "v0.1"


# -------------------------
# Functions
# -------------------------

def display_tool_info():
    print(TOOL_NAME, "-", VERSION)


# -------------------------
# Main Execution
# -------------------------

if __name__ == "__main__":
    display_tool_info()

# GenAI Risk Assessment Tool – v0.1
print ("GenAI Risk Assessment Tool – v0.1")

# Learning [Lists, Dictionaries] as it applies in real world
risks1 = ["Prompt Injection", "Data Leakage"]
risks2 = ["Model Misuse"]

# Prompt Injection
print(risks2)
risks2.append("Training Data Exposure")
print(risks1)
risks1.append("Testing Error")

# Added "Training Data Exposure" to Learning [Lists, Dictionaries] as it applies in real world
risks1 = ["Prompt Injection", "Data Leakage", "Testing Error"]
risks2 = ["Model Misuse", "Training Data Exposure"]

# Calling An Attack From risks2 
print(risks2[1])

# Calling An Attack From risks1
print(risks1[1]), (risks2[1])

# -------------------------
# Day 2: Risk Register Core
# -------------------------

#Dictionaries = meaning + structure (this is the real power)
genai_risks_register = {
    "Prompt Injection": "Manipulating model input to bypass safeguards", 
    "Data Leakage": "Exposure of sensitive training or user data",
    "Model Misuse": " Using AI systems for unintended or harmful purpose",
    "Testing Error": "The king is just Checking if the code works"
}

# List all risks
print("GenAI Risks Identified:")
for risk1 in genai_risks_register:
    print("-", risk1)

# Retrieve a single risk
print("\nRisk Detail:")
print("Model Misuse", genai_risks_register["Model Misuse"])
print("Data Leakage", genai_risks_register["Data Leakage"])
print("Testing Error", genai_risks_register["Testing Error"])

# -------------------------
# Day 3: Risk Register Core
# -------------------------

	# if / else
	# Simple logic: risk_level = "High"
	# if risk_level == "High":
	# print("Immediate action required")


risk_levels = {
    "Low" : 1,
    "Medium" : 2,
    "High" : 3
}

risk_level = "High"
if risk_levels[risk_level] == 3:
    print("Immediate action required")
else:
    print("Monitor the situation")
    
    
    
# ---------------------------
# Agentic Risk Evaluation
# ---------------------------

risk_name1 = "Model Misuse"
agent_autonomy = True
input_trust_level = "Low"
risk_level = "High"

risk_name2 = "Data Leakage"
agent_autonomy = True
input_trust_level = "Low"
risk_level = "High"

risk_name3 = "Testing Error"
agent_autonomy = True
input_trust_level = "Low"
risk_level = "High"

def assess_agentic_risk(risk_name, agent_autonomy, input_trust_level):
    print(f"\nAssessing Risk: {risk_name}")
    
    if risk_name == "Testing Error":
        print("Zero Danger scenerio: Agent should stand down")
        print("Mitigation: Go home")
        return
    
    if agent_autonomy and input_trust_level == "Low":
        print("High-risk scenerio: Agent instruction integrity may be compromised")
        print("Mitigation: Enforce input isolation, role seperation, and policy validation")
    else:
        print("Risk level acceptable under current conditions")    
    

assess_agentic_risk(
    risk_name="Model Misuse",
    agent_autonomy=True,
    input_trust_level="Low"
)

assess_agentic_risk(
    risk_name="Data Leakage",
    agent_autonomy=True,
    input_trust_level="Low"
)

assess_agentic_risk(
    risk_name="Testing Error",
    agent_autonomy=True,
    input_trust_level="Low"
)
