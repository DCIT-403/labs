from spade.agent import Agent
from spade.behaviour import CyclicBehaviour
from spade.message import Message
import asyncio

# Custom sensor modules that simulate real hardware readings
from sensors.smoke_sensor import SmokeSensor
from sensors.vibration_sensor import VibrationSensor


class SensorAgent(Agent):

    class SenseBehaviour(CyclicBehaviour):
        async def run(self):

            # Refresh both sensors to get the latest simulated values
            self.agent.smoke_sensor.update()
            self.agent.vibration_sensor.update()

            # Read the current values from each sensor
            smoke = self.agent.smoke_sensor.read()
            vibration = self.agent.vibration_sensor.read()

            # Determine severity based on sensor thresholds
            if smoke > 150 or vibration > 5:
                severity = "High"
            elif smoke > 50 or vibration > 2:
                severity = "Medium"
            else:
                severity = "Low"

            # Build the alert message content with all sensor data
            content = (
                f"Disaster: Fire | Severity: {severity} | "
                f"SMOKE:{smoke}, VIBRATION:{vibration}"
            )

            # Create and send an INFORM message to CoordinatorAgent
            msg = Message(to="coordinator2000@xmpp.jp")
            msg.set_metadata("performative", "inform")
            msg.body = content

            await self.send(msg)

            print(f"[SensorAgent {self.agent.jid}] INFORM sent -> {content}")

            # Log the alert to file for record keeping
            with open("sensor_logs.txt", "a") as f:
                f.write(content + "\n")

            # Wait 3 seconds before the next sensor reading
            await asyncio.sleep(3)

    async def setup(self):
        print("SensorAgent starting...")

        # Initialize both sensors so they are ready to read
        self.smoke_sensor = SmokeSensor()
        self.vibration_sensor = VibrationSensor()

        # Start the sensing loop
        self.add_behaviour(self.SenseBehaviour())


if __name__ == "__main__":
    async def main():
        # Create the sensor agent with its XMPP credentials
        agent = SensorAgent("sensor2000@xmpp.jp", "sensor123")
        await agent.start()

        print("SensorAgent running...")

        # Keep the program alive so the agent keeps sending readings
        while True:
            await asyncio.sleep(1)

    asyncio.run(main())