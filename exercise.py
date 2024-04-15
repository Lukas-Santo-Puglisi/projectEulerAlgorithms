# Task: Demonstrate the use of the @staticmethod decorator in a Python class. Create a class named TemperatureConverter that contains two static methods: celsius_to_fahrenheit and fahrenheit_to_celsius. Each method should take a temperature value as an argument and return the converted temperature. Also, demonstrate how these methods would be called without creating an instance of the class.

class TemperatureConverter:
    @staticmethod
    def celsius_to_fahrenheit(temperature):
        return temperature * 9/5) + 32 
    @staticmethod
    def fahrenheit_to_celsius(temperature):
        return (temperature - 32)* 5/9
    
print(TemperatureConverter.celsius_to_fahrenheit(TemperatureConverter.fahrenheit_to_celsius(0)))
    