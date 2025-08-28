# --------------------------------------------------------
# Python OOP Assignment
# Author: Bikila Keneni
# --------------------------------------------------------

# ---------------------------
# Activity 1: Design Your Own Class
# ---------------------------

class Smartphone:
    def __init__(self, brand, model, storage):
        self.brand = brand
        self.model = model
        self.__storage = storage   # private attribute (encapsulation)

    def phone_info(self):
        return f"{self.brand} {self.model} with {self.__storage}GB storage"

    def make_call(self, number):
        return f"📞 Calling {number} from {self.model}..."

    def get_storage(self):
        # Getter for private attribute
        return self.__storage

    def set_storage(self, new_storage):
        # Setter with simple validation
        if new_storage > 0:
            self.__storage = new_storage
        else:
            print("Storage must be positive!")


# Child class (inheritance)
class SmartWatch(Smartphone):
    def __init__(self, brand, model, storage, strap_color):
        super().__init__(brand, model, storage)
        self.strap_color = strap_color

    # Method overriding (polymorphism)
    def phone_info(self):
        return f"{self.brand} SmartWatch ({self.model}) with strap color {self.strap_color}"


# ---------------------------
# Activity 2: Polymorphism Challenge
# ---------------------------

class Vehicle:
    def move(self):
        pass   # Abstract-like method to be overridden


class Car(Vehicle):
    def move(self):
        return "🚗 Driving on the road"


class Plane(Vehicle):
    def move(self):
        return "✈️ Flying in the sky"


class Boat(Vehicle):
    def move(self):
        return "⛵ Sailing on the water"


# ---------------------------
# Testing Section
# ---------------------------
if __name__ == "__main__":

    print("----- Activity 1: Smartphone Example -----")
    phone1 = Smartphone("Samsung", "Galaxy S25", 256)
    print(phone1.phone_info())
    print(phone1.make_call("+251911223344"))

    watch1 = SmartWatch("Apple", "Watch X", 32, "Black")
    print(watch1.phone_info())

    print("\n----- Activity 2: Polymorphism Challenge -----")
    vehicles = [Car(), Plane(), Boat()]
    for v in vehicles:
        print(v.move())
