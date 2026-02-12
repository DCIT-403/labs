import asyncio

# Import all three agents that make up the disaster response system
from sensor_agent import SensorAgent
from coordinator_agent import CoordinatorAgent
from rescue_agent import RescueAgent


async def main():

    print("Starting Disaster Response System...")

    # Create each agent with their XMPP login credentials
    sensor = SensorAgent("sensor2000@xmpp.jp", "sensor123")
    coordinator = CoordinatorAgent("coordinator2000@xmpp.jp", "123Qwerty")
    rescue = RescueAgent("rescue2000@xmpp.jp", "rescue123")

    # Start all agents so they begin running their behaviours
    await sensor.start()
    await coordinator.start()
    await rescue.start()

    print("All agents running...")

    try:
        # Keep the system alive until the user manually stops it
        while True:
            await asyncio.sleep(1)
    except KeyboardInterrupt:
        # Gracefully shut down all agents when Ctrl+C is pressed
        print("Shutting down agents...")
        await sensor.stop()
        await coordinator.stop()
        await rescue.stop()


if __name__ == "__main__":
    asyncio.run(main())