#!/usr/bin/env python3

def check_plant_health(plant_name, water_level, sunlight_hours):
    if not plant_name:
        raise ValueError("Error: Plant name cannot be empty!")
    if water_level < 1:
        raise ValueError(f"Error: Water level "
                         f"{water_level} is too low (min 1)\n")
    if water_level > 10:
        raise ValueError(f"Error: Water level "
                         f"{water_level} is too high (max 10)\n")
    if sunlight_hours < 2:
        raise ValueError(f"Error: Sunlight hours "
                         f"{sunlight_hours} is too low (min 2)\n")
    if sunlight_hours > 12:
        raise ValueError(f"Error: Sunlight hours "
                         f"{sunlight_hours} is too high (max 12)\n")
    return f"Plant '{plant_name}' is healthy!\n"


def test_plant_checks():
    print("=== Garden Plant Health Checker ===\n")

    print("Testing good values...")
    try:
        print(check_plant_health("tomato", 3, 2))
    except ValueError as e:
        print(e)

    print("Testing low water level...")
    try:
        print(check_plant_health("tomato", 0, 2))
    except ValueError as e:
        print(e)

    print("Testing high water level...")
    try:
        print(check_plant_health("tomato", 13, 2))
    except ValueError as e:
        print(e)

    print("Testing low sunlight hours...")
    try:
        print(check_plant_health("tomato", 3, 1))
    except ValueError as e:
        print(e)

    print("Testing high sunlight hours...")
    try:
        print(check_plant_health("tomato", 3, 22))
    except ValueError as e:
        print(e)

    print("All error raising tests completed!")


if __name__ == "__main__":
    test_plant_checks()
