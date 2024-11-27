from Vehicle import Vehicle


class Bus(Vehicle):
    def __init__(self, registration_number, capacity,passenger_list, current_location = (0,0)):
        self.registration_number = registration_number
        self.current_location = current_location
        self.capacity = capacity
        self.max_distance = 800
        self.fuel_cost_per_km = 1.25
        self.passenger_weight_factor = 0.02
        self.passenger_list = passenger_list

        if capacity<len(passenger_list):
            raise ValueError("Za duzo ludzi na pokladzie")

    def move(self, destination):
        distance = ((destination[0] - self.current_location[0]) ** 2 + (
                destination[1] - self.current_location[1]) ** 2) ** 0.5
        if distance > self.max_distance:
            print("Byq za daleko troche")
        self.current_location = destination

    def calculate_fuel_cost(self, distance):
        return distance * (self.fuel_cost_per_km + self.passenger_weight_factor * len(self.passenger_list))

    def get_info(self):
        return f"Bus {self.registration_number} z ludzmi {self.passenger_list} na pokladzie, aktualna lokalizacja: {self.current_location}"
