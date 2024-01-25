# implementing abstraction :

from abc import ABC,abstractmethod

class Vehicle(ABC):

    def __init__(self,make,model,year,color):
        self.make = make
        self.model = model
        self.year = year
        self.color = color
        self.is_running = False

    @abstractmethod
    def start_engine(self):
        pass

    @abstractmethod
    def stop_engine(self):
        pass

    def display_info(self):
        print(f"{self.year} {self.make} {self.model} ({self.color})")
        print("Status: Running" if self.is_running else "Status: Stopped")

class car(Vehicle):

    def start_engine(self):
         if not self.is_running:
            print(f"The {self.color} {self.year} {self.make} {self.model}'s engine is now running.")
            self.is_running = True
         else:
            print(f"The engine is already running.")

    def stop_engine(self):
         if self.is_running:
            print(f"The {self.color} {self.year} {self.make} {self.model}'s engine is now stopped.")
            self.is_running = False
         else:
            print("The engine is already stopped.")

# instantiation -
            
car1 = car("benz","s4",2024,"white")

car1.start_engine()
car1.display_info()
car1.stop_engine()









    


