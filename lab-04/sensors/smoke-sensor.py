from .base_sensor import BaseSensor

class SmokeSensor(BaseSensor):
    def __init__(self):
        # ppm levels
        super().__init__(min_value=0, max_value=300, max_delta=5)

    def update(self):
        super().update()
