from car_factory import CarFactory

class servicable():
    def __init__(self):
        model = input("Enter type: ")
        currentDate = input("Enter date: ")
        lastServiceDate = input("Enter last service date: ")
        currentMileage = input ("Enter current mileage: ")
        lastServiceMileage = input("Emter last service mileage: ")
        warningLightOn = input("Is warning light on? (1/0): ")
        if model == "calliope":
            inCar = CarFactory.create_calliope(self, currentDate, lastServiceDate, currentMileage, lastServiceMileage)
        elif model == "glissade": 
            inCar = CarFactory.create_glissade(self, currentDate, lastServiceDate, currentMileage, lastServiceMileage)
        elif model == "palindrome":
            inCar = CarFactory.create_palindrome(self, currentDate, lastServiceDate, warningLightOn)
        elif model == "rorschach":
            inCar = CarFactory.create_rorschach(self, currentDate, lastServiceDate, currentMileage, lastServiceMileage)
        elif model == "thovex":
            inCar = CarFactory.create_thovex(self, currentDate, lastServiceDate, currentMileage, lastServiceMileage)