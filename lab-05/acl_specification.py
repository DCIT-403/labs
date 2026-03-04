# Defines the messaging rules between agents using the FIPA-ACL standard.
# FIPA-ACL is a standard protocol that defines how agents should communicate.
"""
FIPA-ACL Messaging Specification
Lab 4 – Disaster Response System

Agents:
- SensorAgent
- CoordinatorAgent
- RescueAgent

Performatives Used:
- INFORM
- REQUEST
"""


# Dictionary that documents all message types used in the system
ACL_SPEC = {

    # INFORM is used to report data — sent by SensorAgent or RescueAgent
    "INFORM": {
        "sender": "SensorAgent / RescueAgent",
        "receiver": "CoordinatorAgent",
        "purpose": "Report sensor readings or action results",
        # Expected fields inside the message body
        "structure": {
            "disaster": "Fire",
            "severity": "Low | Medium | High",
            "smoke": "float (ppm)",
            "vibration": "float"
        }
    },

    # REQUEST is used to trigger a rescue action — sent by CoordinatorAgent
    "REQUEST": {
        "sender": "CoordinatorAgent",
        "receiver": "RescueAgent",
        "purpose": "Request rescue action",
        # Expected fields inside the message body
        "structure": {
            "action": "IMMEDIATE_RESPONSE | PRIORITY_RESPONSE"
        }
    }
}


if __name__ == "__main__":
    # Print a readable summary of all ACL message types and their details
    print("ACL Specification Loaded:")
    for perf, details in ACL_SPEC.items():
        print(f"\n{perf}:")
        for key, value in details.items():
            print(f"  {key}: {value}")