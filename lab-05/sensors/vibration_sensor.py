from .base_sensor import BaseSensor

class VibrationSensor(BaseSensor):
    def __init__(self):
        super().__init__(min_value=0, max_value=10, max_delta=0.3)

    def update(self):
        super().update()
