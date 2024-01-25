# Implementing encapsulation by creating two protected attributes.
# Implementing encapsulation by creating two private attributes.
class Car:
    def __init__(self, make, model, year, color):
        # Encapsulation requires an underscore.
        self._make = make   # 4 attributes
        self._model = model
        self.__year = year
        self.__color = color
        self.is_running = False

        # 3 methods 

    def start_engine(self):
        if not self.is_running:
            print(f"The {self.__color} {self.__year} {self._make} {self._model}'s engine is now running.")
            self.is_running = True
        else:
            print("The engine is already running.")

    def stop_engine(self):
        if self.is_running:
            print(f"The {self.__color} {self.__year} {self._make} {self._model}'s engine is now stopped.")
            self.is_running = False
        else:
            print("The engine is already stopped.")

    def display_info(self):
        print(f"{self.__year} {self._make} {self._model} ({self.__color})")
        print("Status: Running" if self.is_running else "Status: Stopped")

    




# Creating instances of the Car class   # 2 instances
car1 = Car("Toyota", "Camry", 2020, "Blue")
car2 = Car("Honda", "Accord", 2021, "Red")





# Accessing attributes and calling methods
car1.start_engine()
car2.start_engine()
car1.display_info()
car2.display_info()
car1.stop_engine()
car2.stop_engine()


