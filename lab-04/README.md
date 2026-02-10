# DCIT 403 LAB 4: AGENT COMMUNICATION USING FIPA-ACL
## LAB 4 Team Roles & Responsibilities

---

## 👥 Team Members

### Subgroup A – Environment & Perception

#### Environment Setup & Project Lead [Favour - 11014111]


**Responsibilities:**
- Create shared GitHub repository
- Configure GitHub Codespaces
- Install SPADE and dependencies
- Provide project structure and run instructions

**Deliverables:**
- Repository skeleton
- Setup documentation
- Verified agent startup

---

#### Sensor Simulation Module [Eunice - 11015648]

**Responsibilities:**
- Implement smoke sensor model
- Implement vibration sensor model
- Ensure bounded, incremental sensor changes

**Deliverables:**
- Sensor classes
- Local test outputs

---

### Subgroup B – Communication & Coordination

#### SensorAgent Developer [Morgan - 11079266]

**Responsibilities:**
- Integrate sensor modules
- Periodically collect percepts
- Format sensor data
- Send FIPA-ACL INFORM messages

**Deliverables:**
- SensorAgent code
- INFORM message logs

---

#### CoordinatorAgent & FSM [N - 11052329]

**Responsibilities:**
- Design FSM states and transitions
- Parse incoming INFORM messages
- Decide on disaster severity
- Send REQUEST messages to rescue agents

**Deliverables:**
- CoordinatorAgent implementation
- FSM transition trace

---

#### FIPA-ACL Messaging Specification [Astrea - 11288954]

**Responsibilities:**
- Define performatives (INFORM, REQUEST)
- Specify message structure and metadata
- Ensure semantic consistency across agents

**Deliverables:**
- ACL specification document
- Example message formats

---

### Subgroup C – Action & Integration

#### RescueAgent Developer [Larry - 11116870]

**Responsibilities:**
- Implement RescueAgent
- Parse REQUEST messages
- Simulate rescue actions
- Log task execution

**Deliverables:**
- RescueAgent code
- REQUEST handling logs

---

#### System Integrator & Tester [Muiz - 11068463]

**Responsibilities:**
- Integrate all agents into a single system
- Validate end-to-end message exchange
- Verify FIPA-ACL usage
- Collect execution logs for submission

**Deliverables:**
- Integrated runnable system (run_system.py)
- Final message logs
- Submission-ready code

---

## 📋 Task Dependency Order
```
1. Environment setup (Favour)
   ↓
2. Sensor simulation (Eunice)
   ↓
3. SensorAgent (Morgan)
   ↓
4. ACL spec + Coordinator FSM (N & Astrea - parallel)
   ↓
5. RescueAgent (Larry)
   ↓
6. System integration and validation (Muiz)
```

---

## 🚀 Getting Started

See [SETUP.md](SETUP.md) for detailed environment configuration and running instructions.