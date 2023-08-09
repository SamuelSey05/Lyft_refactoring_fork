from abc import ABC, abstractmethod

from datetime import datetime

from car_factory import CarFactory

from battery import battery
from engine import engine

class Car(ABC):
    def __init__(self, last_service_date, battery: battery, engine: engine):
        self.last_service_date = last_service_date
        self.battery = battery
        self.engine = engine

    def needs_service(self):
        return battery.needs_service(self.battery) or engine.needs_service(self.engine)