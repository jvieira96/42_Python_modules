#!/usr/bin/env python3

class Plant:
    def __init__(self, name, height, age):
        self.name = name
        self.height = height
        self.plant_age = age
        self.last_growth = 0

    def grow(self, amount):
        self.last_growth = amount
        self.height += amount

    def age(self, amount):
        self.plant_age += amount

    def get_info(self):
        print(f"{self.name}: {self.height}cm, {self.plant_age} days old")
        if self.last_growth:
            print(f"Growth this week: +{self.last_growth}cm")


if __name__ == "__main__":
    garden = [
        Plant("Rose", 25, 30),
        Plant("Oak", 200, 365),
        Plant("Cactus", 5, 90),
        Plant("Sunflower", 80, 45),
        Plant("Fern", 15, 120)
    ]

    amount = 0
    for plant in garden:
        plant.get_info()
        amount += 1

    print(f"\nTotal plants created: {amount}")
