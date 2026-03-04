import asyncio

# Import all three agents that make up the disaster response system
from sensor_agent import SensorAgent
from coordinator_agent import CoordinatorAgent
from rescue_agent import RescueAgent


async def main():

    print("Starting Disaster Response System...")

    # Create each agent with their XMPP login credentials
    sensors = [SensorAgent(f"sensor{2000+i}@xmpp.jp", "sensor123") for i in range(8)]
    coordinator = CoordinatorAgent("coordinator2000@xmpp.jp", "123Qwerty")
    rescue_agents = [RescueAgent(f"rescue{2000+i}@xmpp.jp", "rescue123") for i in range(3)]

    # Start all agents so they begin running their behaviours
    await coordinator.start()
    await asyncio.sleep(3)  
    for sensor in sensors:
        await sensor.start()
    for rescue in rescue_agents:
        await rescue.start()
    await asyncio.sleep(2)  

    print("All agents running...")

    try:
        # Keep the system alive until the user manually stops it
        while True:
            await asyncio.sleep(1)
    except KeyboardInterrupt:
        # Gracefully shut down all agents when Ctrl+C is pressed
        print("Shutting down agents...")
        for sensor in sensors:
            await sensor.stop()
        await coordinator.stop()
        for rescue in rescue_agents:
            await rescue.stop()

if __name__ == "__main__":
    asyncio.run(main())