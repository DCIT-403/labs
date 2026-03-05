import random

class BaseSensor:
    def __init__(self, min_value, max_value, max_delta):
        self.min_value = min_value
        self.max_value = max_value
        self.max_delta = max_delta
        self.value = random.uniform(min_value, max_value)

    def update(self):
        """Apply bounded incremental change"""
        change = random.uniform(-self.max_delta, self.max_delta)
        self.value += change

        # Clamp within physical bounds
        self.value = max(self.min_value, min(self.value, self.max_value))

    def read(self):
        return round(self.value, 2)
