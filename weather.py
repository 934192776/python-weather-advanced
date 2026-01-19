class Weather:
    def __init__(self, city):
        self.city = city
        self.temperature = None
        self.condition = None

    def set_weather(self, temperature, condition):
        self.temperature = temperature
        self.condition = condition

    def display_weather(self):
        print(f"city: {self.city}")
        print(f"Temperature: {self.temperature}")
        print(f"Condition: {self.condition}")