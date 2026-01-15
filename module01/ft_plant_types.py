#!/usr/bin/env python3

class Plant:
    def __init__(self, name, height, age):
        self.name = name
        self.height = height
        self.age = age


class Flower(Plant):
    def __init__(self, name, height, age, color):
        super().__init__(name, height, age)
        self.color = color

    def bloom(self):
        print(f"{self.name} is blooming beautifully!")


class Tree(Plant):
    def __init__(self, name, height, age, trunk_diameter):
        super().__init__(name, height, age)
        self.trunk_diameter = trunk_diameter

    def produce_shade(self):
        shade = self.trunk_diameter * 1.56
        print(f"{self.name} provides {int(shade)} square meters of shade")


class Vegetable(Plant):
    def __init__(self, name, height, age, harvest_season, nutritional_value):
        super().__init__(name, height, age)
        self.harvest_season = harvest_season
        self.nutritional_value = nutritional_value


def main():
    print("=== Garden Plant Types ===")
    print("\n")

    rose = Flower("Rose", 25, 30, "red")
    lily = Flower("Lily", 30, 15, "white")

    oak = Tree("Oak", 500, 1825, 50)
    pine = Tree("Pine", 300, 1000, 30)

    tomato = Vegetable("Tomato", 80, 90, "summer", "vitamin C")
    carrot = Vegetable("Carrot", 20, 60, "winter", "vitamin A")

    print(f"{rose.name} (Flower): {rose.height}cm, "
          f"{rose.age} days, {rose.color} color")
    rose.bloom()
    print(f"{lily.name} (Flower): {lily.height}cm, "
          f"{lily.age} days, {lily.color} color")
    lily.bloom()
    print("\n")

    print(f"{oak.name} (Tree): {oak.height}cm, "
          f"{oak.age} days, {oak.trunk_diameter}cm diameter")
    oak.produce_shade()
    print(f"{pine.name} (Tree): {pine.height}cm, "
          f"{pine.age} days, {pine.trunk_diameter}cm diameter")
    pine.produce_shade()
    print("\n")

    print(f"{tomato.name} Vegetable): {tomato.height}cm, "
          f"{tomato.age} days, {tomato.harvest_season} harvest")
    print(f"{tomato.name} is rich in {tomato.nutritional_value}")
    print(f"{carrot.name} (Vegetable): {carrot.height}cm, "
          f"{carrot.age} days, {carrot.harvest_season} harvest")
    print(f"{carrot.name} is rich in {carrot.nutritional_value}")


if __name__ == "__main__":
    main()
