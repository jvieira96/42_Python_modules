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

    rose = Plant("Rose", 25, 30)
    print("=== Day 1 ===")
    rose.get_info()
    rose.grow(6)
    rose.age(6)
    print("=== Day 7 ===")
    rose.get_info()
