from engine import capulet_engine, sternman_engine, willoughby_engine
from battery import spindler_battery, nubbin_battery
from car import Car


class CarFactory:
    
    def create_calliope(self, current_date, last_service_date, current_mileage, last_service_mileage):
        engine = capulet_engine(last_service_date, current_mileage, last_service_mileage)
        battery = spindler_battery(last_service_date, current_date)
        return Car(last_service_date, battery, engine)
    
    def create_glissade(self, current_date, last_service_date, current_mileage, last_service_mileage):
        engine = willoughby_engine(last_service_date, current_mileage, last_service_mileage)
        battery = spindler_battery(last_service_date, current_date)
        return Car(last_service_date, battery, engine)
    
    def create_palindrome(self, current_date, last_service_date, warning_light_on):
        engine = sternman_engine(last_service_date, warning_light_on)
        battery = spindler_battery(last_service_date, current_date)
        return Car(last_service_date, battery, engine)

    def create_rorschach(self, current_date, last_service_date, current_mileage, last_service_mileage):
        engine = willoughby_engine(last_service_date, current_mileage, last_service_mileage)
        battery = nubbin_battery(last_service_date, current_date)
        return Car(last_service_date, battery, engine)

    def create_thovex(self, current_date, last_service_date, current_mileage, last_service_mileage):
        engine = capulet_engine(last_service_date, current_mileage, last_service_mileage)
        battery = nubbin_battery(last_service_date, current_date)
        return Car(last_service_date, battery, engine)