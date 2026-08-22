class Vehicle:
    def __init__(self, make, model):
        self.make = make
        self.model = model

    def moves(self):
        print("Moves Forward....")

    def get_make_model(self):
        print(f"I'm a {self.make} {self.model}.")


my_car = Vehicle("BMW", "M5 COMP")

# print(my_car.make)
# print(my_car.model)
my_car.get_make_model()
my_car.moves()
your_car = Vehicle("Porche", "911 GTRS")
your_car.get_make_model()
your_car.moves()


class Airplane(Vehicle):
    def __init__(self, make, model, faa_id):
        super().__init__(make, model)
        self.faa_id = faa_id

    def moves(self):
        print("Flies away...")


class Truck(Vehicle):
    def moves(self):
        print("Grunts away...")


class GolfCart(Vehicle):
    pass


cessna = Airplane("Cessna", "Sky Hawk", "HC-1254")
rivian = Truck("Rivian", "R1T")
golfwagan = GolfCart("Yamaha", "GC100")

cessna.get_make_model()
cessna.moves()
rivian.get_make_model()
rivian.moves()
golfwagan.get_make_model()
golfwagan.moves()

print("\n\n")

for x in (my_car, your_car, cessna, rivian, golfwagan):
    x.get_make_model()
    x.moves()
