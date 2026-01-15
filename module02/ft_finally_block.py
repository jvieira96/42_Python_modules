#!/usr/bin/env python3

def water_plants(plant_list):
    print("Opening watering system")
    try:
        for plant in plant_list:
            if plant is None:
                raise ValueError("invalid plant!")
            print(f"Watering {plant}")
    except ValueError:
        print("Error: Cannot water None - invalid plant!")
    finally:
        print("Closing watering system (cleanup)")


def main():
    plant_list = [
        "tomato",
        "lettuce",
        "carrots"
    ]

    print("=== Garden Watering System ===\n")
    print("Testing normal watering...")
    water_plants(plant_list)
    print("Watering completed successfully!\n")

    plant_list_error = [
        "tomato",
        None
    ]

    print("Testing with error...")
    water_plants(plant_list_error)
    print("\nCleanup always happens, even with errors!")


if __name__ == "__main__":
    main()
