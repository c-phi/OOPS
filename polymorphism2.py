# implementation of Method overriding ->



class Car:
    def __init__(self,make,model,year,color):
        self.make = make
        self.model = model
        self.year = year
        self.color = color
        self.is_running = False

    def start_engine(self, key_note=None):
        if not self.is_running:
            if key_note == "smart":
                print(f"The {self.color} {self.year} {self.make} {self.model}'s engie is started with smart key")
            elif key_note == "traditional":
                print(f"The {self.color} {self.year} {self.make} {self.model}'s engine is started with traditional key.")
            else:
                print(f"The {self.color} {self.year} {self.make} {self.model}'s engine is now started")
        else:
            print(f"The {self.color} {self.year} {self.make} {self.model}'s engine is already running.")
    

    def stop_engine(self):
        if self.is_running:
            print(f"The {self.color} {self.year} {self.make} {self.model}'s engine is now stopped.")
            self.is_running = False
        else:
            print("The engine is already stopped.")

    def display_info(self):
        print(f"{self.year} {self.make} {self.model} ({self.color})")
        print("Status: Running" if self.is_running else "Status: Stopped")

class ElectricCar(Car):
    def __init__(self,make,model,year,color,battery_capacity):
        super().__init__(make,model,year,color)
        self.battery_capacity = battery_capacity
        self.is_charging = False

    def start_engine(self):
        if not self.is_charging:
            print(f"The {self.color} {self.year} {self.make} {self.model}'s battery is now charging.")
            self.is_charging = True
        else:
            print("The battery is already charging.")
    
    def stop_engine(self):
        if self.is_charging:
            print(f"The {self.color} {self.year} {self.make} {self.model}'s battery has stopped charging")
        else:
            print("The battery is charged")
    

# let us create instances of ElectricCar
            
car1 = ElectricCar("Audi","S3",2024,"white",500)
car2 = ElectricCar("benz","S4",2024,"black",600)

car1.start_engine()

car1.display_info()

car1.stop_engine()

car2.start_engine()

car1.start_engine()

