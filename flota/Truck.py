from Vehicle import Vehicle


class Truck(Vehicle):
    def __init__(self, registration_number, capacity, cargo, current_location=(0, 0)):
        self.registration_number = registration_number
        self.current_location = current_location
        self.capacity = capacity
        self.max_distance = 800
        self.fuel_cost_per_km = 1.5
        self.extra_cargo_per_km = 0.05
        self.cargo = cargo

        if capacity<len(cargo):
            raise ValueError("Za duzo towaru")


    def move(self, destination):
        distance = ((destination[0] - self.current_location[0]) ** 2 + (
                destination[1] - self.current_location[1]) ** 2) ** 0.5
        if distance > self.max_distance:
            print("Byq za daleko troche")
        self.current_location = destination

    def calculate_fuel_cost(self, distance):
        return distance * (self.fuel_cost_per_km + self.extra_cargo_per_km * len(self.cargo))

    def get_info(self):
        return f"Truck {self.registration_number} z towarem {self.cargo} na pokladzie, aktualna lokalizacja: {self.current_location}"
