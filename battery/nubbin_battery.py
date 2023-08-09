
from battery import battery

class NubbinBattery(battery):
    def __init__(self, last_service_date, current_date):
        super().__init__(last_service_date)
        self.last_service_date = last_service_date
        self.current_date = current_date

    def needs_service(self):
        return self.current_date < self.last_service_date.replace(year=self.last_service_date.year + 4)
