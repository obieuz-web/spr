from Vehicle import Vehicle

class FleetManager:
    def __init__(self):
        self.fleet = []

    def add_vehicle(self, vehicle):
        if not isinstance(vehicle, Vehicle):
            raise TypeError("Dodawany obiekt musi być instancją klasy pochodnej od Vehicle.")
        self.fleet.append(vehicle)

    def dispatch(self, vehicle_id, destination):
        for i in self.fleet:
            if i.registration_number == vehicle_id:
                i.move(destination)
                break

    def get_summary(self):
        print("Podsumowanie floty:")
        for i in self.fleet:
            print(i.get_info())

    def calculate_total_fuel_cost(self, distance):
        total_cost = 0

        for vehicle in self.fleet:
            total_cost += vehicle.calculate_fuel_cost(distance)

        print(f"Całkowity koszt paliwa dla dystansu {distance} km: {total_cost:.2f} jednostek.")
        return total_cost