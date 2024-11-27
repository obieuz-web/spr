from Bus import Bus
from Truck import Truck
from FleetManager import FleetManager


if __name__ == "__main__":
    # Tworzenie pojazdów
    bus = Bus(registration_number="BUS123", capacity=50, passenger_list=["Jan", "Anna", "Kasia"])
    truck = Truck(registration_number="TRK456", capacity=10, cargo=["Towar1", "Towar2"])

    # Tworzenie menedżera floty
    manager = FleetManager()

    # Dodawanie pojazdów do floty
    manager.add_vehicle(bus)
    manager.add_vehicle(truck)

    # Wyświetlanie podsumowania floty
    manager.get_summary()

    # Przemieszczanie pojazdów
    manager.dispatch(vehicle_id="BUS123", destination=(50, 60))
    manager.dispatch(vehicle_id="TRK456", destination=(100, 200))

    # Obliczanie kosztów paliwa
    manager.calculate_total_fuel_cost(distance=100)
