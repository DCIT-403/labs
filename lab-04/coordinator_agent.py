import asyncio
from spade.agent import Agent
from spade.behaviour import FSMBehaviour, State
from spade.message import Message

# The three stages the coordinator cycles through
STATE_WAITING = "WAITING"
STATE_ANALYZING = "ANALYZING"
STATE_DISPATCHING = "DISPATCHING"

class CoordinatorAgent(Agent):

    async def setup(self):
        print("CoordinatorAgent starting...")

        # Shared data used across all FSM states
        self.received_event = None
        self.severity = None
        self.decision = None

        # Create the Finite State Machine
        fsm = FSMBehaviour()

        # Register all states, WAITING is where it starts
        fsm.add_state(name=STATE_WAITING, state=self.WaitingState(), initial=True)
        fsm.add_state(name=STATE_ANALYZING, state=self.AnalyzingState())
        fsm.add_state(name=STATE_DISPATCHING, state=self.DispatchingState())

        # Define the allowed paths between states
        fsm.add_transition(STATE_WAITING, STATE_ANALYZING)
        fsm.add_transition(STATE_ANALYZING, STATE_DISPATCHING)
        fsm.add_transition(STATE_DISPATCHING, STATE_WAITING)

        # Attach the FSM to this agent
        self.add_behaviour(fsm)

    # WAITING 
    class WaitingState(State):
        async def run(self):
            print("\n[WAITING] Waiting for INFORM...")

            # Wait up to 30 seconds for an incoming message
            msg = await self.receive(timeout=30)

            if msg and msg.get_metadata("performative") == "inform":
                print(f"[WAITING] INFORM received -> {msg.body}")
                # Save message body so the next state can use it
                self.agent.received_event = msg.body
                # Log the received event to file
                with open("coordinator_logs.txt", "a") as f:
                    f.write(f"RECEIVED: {msg.body}\n")
                self.set_next_state(STATE_ANALYZING)
            else:
                # No message received, stay in WAITING
                self.set_next_state(STATE_WAITING)

    #  ANALYZING 
    class AnalyzingState(State):
        async def run(self):
            print("[ANALYZING] Parsing event...")

            event = self.agent.received_event

            # Extract the severity value from the message string
            if "Severity:" in event:
                self.agent.severity = event.split("Severity:")[1].split("|")[0].strip()
            else:
                self.agent.severity = "Unknown"

            # Map severity to a response decision
            if self.agent.severity == "High":
                self.agent.decision = "IMMEDIATE_RESPONSE"
            elif self.agent.severity == "Medium":
                self.agent.decision = "PRIORITY_RESPONSE"
            else:
                self.agent.decision = "MONITOR"

            print(f"[ANALYZING] Severity={self.agent.severity}")
            print(f"[ANALYZING] Decision={self.agent.decision}")

            # Log the decision to file
            with open("coordinator_logs.txt", "a") as f:
                f.write(f"DECISION: {self.agent.decision}\n")

            self.set_next_state(STATE_DISPATCHING)

    # DISPATCHING 
    class DispatchingState(State):
        async def run(self):

            # Low severity — no rescue needed, go back to waiting
            if self.agent.decision == "MONITOR":
                print("[DISPATCHING] Monitoring only. No rescue needed.")
                self.set_next_state(STATE_WAITING)
                return

            print("[DISPATCHING] Sending REQUEST to RescueAgent...")

            # Build the rescue request message
            msg = Message(to="rescue2000@xmpp.jp")
            msg.set_metadata("performative", "request")
            msg.body = f"Action Required: {self.agent.decision}"

            # Send the request to RescueAgent
            await self.send(msg)

            # Log the sent request to file
            with open("coordinator_logs.txt", "a") as f:
                f.write(f"SENT REQUEST: {msg.body}\n")

            print("[DISPATCHING] REQUEST sent!")

            # Return to WAITING for the next event
            self.set_next_state(STATE_WAITING)


# MAIN RUNNER 
if __name__ == "__main__":
    async def main():
        # Create the coordinator agent with its XMPP credentials
        agent = CoordinatorAgent("coordinator2000@xmpp.jp", "123Qwerty")
        await agent.start()

        print("Coordinator running...")

        # Keep the program alive so the FSM keeps running
        while True:
            await asyncio.sleep(1)

    asyncio.run(main())