#!/usr/bin/env python3

class GardenError(Exception):
    """Base class for all garden errors"""
    def __init__(self, message):
        super().__init__(message)


class PlantError(GardenError):
    """class for PlantErrors"""
    def __init__(self, message):
        super().__init__(message)

class WaterError(GardenError):
    """class for WaterErrors"""
    def __init__(self, message):
        super().__init__(message)

def  raise_errors():
    print("Testing PlantError...")
    try:
        raise PlantError("The tomato plant is wilting!")
    except PlantError as e:
        print(f"Caught PlantError: {e}\n")

    print("Testing WatertError...")
    try:
        raise WaterError("Not enough water in the tank!")
    except WaterError as e:
        print(f"Caught WaterError: {e}\n")

    print("Testing catching all garden errors...")
    try:
        raise WaterError("Not enough water in the tank!")
    except GardenError as e:
        print(f"Caught GardenError: {e}")
    try:
        raise PlantError("The tomato plant is wilting!")
    except PlantError as e:
        print(f"Caught GardenError: {e}\n")


def main():
    print("=== Custom Garden Errors Demo ===\n")
    raise_errors()
    print("All custom error types work correctly!")

if __name__ == "__main__":
    main()

