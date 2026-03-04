import time
from sensors.smoke_sensor import SmokeSensor
from sensors.vibration_sensor import VibrationSensor

smoke = SmokeSensor()
vibration = VibrationSensor()

print("Starting Sensor Simulation...\n")

for _ in range(15):
    smoke.update()
    vibration.update()

    print(f"Smoke Level: {smoke.read()} ppm | Vibration Level: {vibration.read()} units")
    time.sleep(0.5)
