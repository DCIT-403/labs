from sensors.smoke_sensor import SmokeSensor
from sensors.vibration_sensor import VibrationSensor
from acl_specification import ACLMessage


class SensorAgent:
    def __init__(self, name):
        self.name = name
        self.smoke_sensor = SmokeSensor()
        self.vibration_sensor = VibrationSensor()

    def receive(self, message):
        """Handle incoming ACL message"""
        print(f"[{self.name}] Received {message.performative} from {message.sender}: {message.content}")

        if message.performative == "REQUEST":
            return self.handle_request(message)

    def handle_request(self, message):
        """Process REQUEST messages and send INFORM reply"""

        # Update sensors before reading (simulate time passing)
        self.smoke_sensor.update()
        self.vibration_sensor.update()

        content = message.content.lower()

        if "smoke" in content:
            value = self.smoke_sensor.read()
            reply_content = f"Smoke level: {value} ppm"

        elif "vibration" in content:
            value = self.vibration_sensor.read()
            reply_content = f"Vibration level: {value} units"

        else:
            reply_content = "Unknown sensor request"

        reply = ACLMessage(
            performative="INFORM",
            sender=self.name,
            receiver=message.sender,
            content=reply_content
        )

        print(f"[{self.name}] Sending INFORM: {reply_content}")
        return reply
