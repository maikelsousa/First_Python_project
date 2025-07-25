class Flight:
    def __init__(self, capacity):
        try:
            self.capacity = int(capacity)
            if self.capacity <= 0:
                raise ValueError("Capacity needs more than zero")
            self.passenger = []
        except ValueError as e:
            print(f"Erro na inicialização: {e}")
            raise

    def add_passengers(self, name):
        try:
            if not isinstance(name, str):
                raise TypeError("Passenger's name needs be string")
            if not name.strip():
                raise ValueError("Passenger's name can't be empty")
            if not self.open_seats():
                return False
            self.passenger.append(name)
            return True
        except (TypeError, ValueError) as e:
            print(f"Erro add passenger: {e}")
            return False

    def open_seats(self):
        try:
            return self.capacity - len(self.passenger)
        except Exception as e:
            print(f"Error to calculate open seats: {e}")
            return 0

try:
    flight = Flight(3)
    people = ["harrison", "bigs", "snoopDog", "Mia"]
    
    for person in people:
        try:
            success = flight.add_passengers(person)
            if success:
                print(f"Added {person} to Flight successfully")
            else:
                print(f"No more seats available for {person}")
        except Exception as e:
            print(f"Erro to proced passenger{person}: {e}")

except Exception as e:
    print(f"Erro general: {e}")
    SystemExit