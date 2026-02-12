import asyncio
from spade.agent import Agent
from spade.behaviour import CyclicBehaviour
from spade.message import Message


class RescueAgent(Agent):

    class RescueBehaviour(CyclicBehaviour):
        async def run(self):
            print("[RescueAgent] Waiting for REQUEST...")

            # Wait up to 30 seconds for an incoming request
            msg = await self.receive(timeout=30)

            if msg and msg.get_metadata("performative") == "request":
                print(f"[RescueAgent] REQUEST received -> {msg.body}")

                # Store the action instruction from the message
                action = msg.body
                print("[RescueAgent] Executing rescue operation...")

                # Simulate the time it takes to carry out the rescue
                await asyncio.sleep(3)

                result = f"Rescue completed: {action}"

                # Build a confirmation message to send back to CoordinatorAgent
                reply = Message(to="coordinator2000@xmpp.jp")
                reply.set_metadata("performative", "inform")
                reply.body = result

                await self.send(reply)

                print(f"[RescueAgent] INFORM sent -> {result}")

                # Log the completed rescue to file
                with open("rescue_logs.txt", "a") as f:
                    f.write(result + "\n")

    async def setup(self):
        print("RescueAgent starting...")
        # Register the rescue behaviour so the agent starts listening
        self.add_behaviour(self.RescueBehaviour())


if __name__ == "__main__":

    async def main():
        # Create the rescue agent with its XMPP credentials
        agent = RescueAgent("rescue2000@xmpp.jp", "rescue123")
        await agent.start()

        print("RescueAgent running...")

        # Keep the program alive so the agent keeps listening
        while True:
            await asyncio.sleep(1)

    asyncio.run(main())