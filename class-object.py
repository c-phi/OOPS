class Car:
    def __init__(self, make, model, year, color):
        self.make = make   # 4 attributes
        self.model = model
        self.year = year
        self.color = color
        self.is_running = False

        # 3 methods 

    def start_engine(self):
        if not self.is_running:
            print(f"The {self.color} {self.year} {self.make} {self.model}'s engine is now running.")
            self.is_running = True
        else:
            print("The engine is already running.")

    def stop_engine(self):
        if self.is_running:
            print(f"The {self.color} {self.year} {self.make} {self.model}'s engine is now stopped.")
            self.is_running = False
        else:
            print("The engine is already stopped.")

    def display_info(self):
        print(f"{self.year} {self.make} {self.model} ({self.color})")
        print("Status: Running" if self.is_running else "Status: Stopped")

# Creating instances of the Car class   # 2 instances
car1 = Car("Toyota", "Camry", 2020, "Blue")
car2 = Car("Honda", "Accord", 2021, "Red")
# Create another instance
car3 = Car("Mercedes", "Benz", 2023, "white")

# Accessing attributes and calling methods
car1.start_engine()
car2.start_engine()
car1.display_info()
car2.display_info()
car1.stop_engine()
car2.stop_engine()
