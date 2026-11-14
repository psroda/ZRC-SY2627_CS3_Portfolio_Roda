
from abc import ABC, abstractmethod


# Abstract Base Class
class Sensor(ABC):

    @abstractmethod
    def get_reading(self):
        pass


# Child Class: pH Sensor
class PHSensor(Sensor):

    def get_reading(self):
        print("[pH Sensor] Reading: 7.2 pH (Neutral)")


# Child Class: Temperature Sensor
class TempSensor(Sensor):

    def get_reading(self):
        print("[Temperature Sensor] Reading: 24.5°C")


# Main Program
print("--- Lab Inventory System ---")

ph_sensor = PHSensor()
temp_sensor = TempSensor()

ph_sensor.get_reading()
temp_sensor.get_reading()

print("----------------------------")


# Task 5: Uncomment this line to test the error
# my_sensor = Sensor()
