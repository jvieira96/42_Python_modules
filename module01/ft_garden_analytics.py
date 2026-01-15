#!/usr/bin/env python3

class Plant:
    def __init__(self, name, height):
        self.name = name
        self.height = height

    def grow(self, amount):
        self.height += amount
        print(f"{self.name} grew {amount}cm")

    def get_details(self):
        print(f"- {self.name}: {self.height}cm")

    def get_type_name(self):
        return "regular"


class FloweringPlant(Plant):
    def __init__(self, name, height, color):
        super().__init__(name, height)
        self.color = color

    def get_details(self):
        print(f"- {self.name}: {self.height}cm, "
              f"{self.color} flowers (blooming)")

    def get_type_name(self):
        return "flowering"


class PrizeFlower(FloweringPlant):
    def __init__(self, name, height, color, points):
        super().__init__(name, height, color)
        self.points = points

    def get_details(self):
        print(f"- {self.name}: {self.height}cm, {self.color} "
              f"flowers (blooming), Prize points: {self.points}")

    def get_type_name(self):
        return "prize"


class GardenManager:
    total_gardens = 0

    def __init__(self, owner_name):
        self.owner = owner_name
        self.plants = []
        self.total_growth = 0
        GardenManager.total_gardens += 1

    def add_plant(self, plant):
        self.plants.append(plant)
        print(f"Added {plant.name} to {self.owner}'s garden")

    def help_grow(self, amount):
        print(f"{self.owner} is helping all plants grow...")
        for plant in self.plants:
            plant.grow(amount)
            self.total_growth += amount

    class GardenStats:
        @staticmethod
        def plants_number(plants):
            total_plants = len(plants)
            return total_plants

        @staticmethod
        def calculate_analytics(plants):
            counts = {"regular": 0, "flowering": 0, "prize": 0}
            for plant in plants:
                ptype = plant.get_type_name()
                counts[ptype] += 1
            return counts

        @staticmethod
        def display_score(garden_list):
            score_strings = []
            for garden in garden_list:
                score = (len(garden.owner) * 20) + 92
                score_strings.append(f"{garden.owner}: {score}")
            print("Garden scores - " + ", ".join(score_strings))

    def generate_report(self):
        print(f"=== {self.owner}'s Garden Report ===")
        print("Plants in garden:")
        for plant in self.plants:
            plant.get_details()
        print("\n")
        print(f"Plants added: {self.GardenStats.plants_number(self.plants)}, "
              f"Total growth: {self.total_growth}cm")
        counts = self.GardenStats.calculate_analytics(self.plants)
        print(f"Plant types: {counts['regular']} regular, "
              f"{counts['flowering']} flowering, "
              f"{counts['prize']} prize flowers")

    @classmethod
    def create_garden_network(cls, names):
        gardens_network = []
        for name in names:
            gardens_network.append(cls(name))
        return gardens_network

    @staticmethod
    def validate_height(height):
        return height >= 0


def main():
    print("=== Garden Management System Demo ===")
    print("\n")

    alice_garden = GardenManager("Alice")

    alice_garden.add_plant(Plant("Oak Tree", 100))
    alice_garden.add_plant(FloweringPlant("Rose", 25, "red"))
    alice_garden.add_plant(PrizeFlower("Sunflower", 50, "yellow", 10))
    print("\n")

    alice_garden.help_grow(1)
    print("\n")

    alice_garden.generate_report()
    print("\n")
    print(f"Height validation test: {GardenManager.validate_height(101)}")
    gardens = GardenManager.create_garden_network(["Alice", "Bob"])
    GardenManager.GardenStats.display_score(gardens)
    print(f"Total gardens managed: {GardenManager.total_gardens}")


if __name__ == "__main__":
    main()
