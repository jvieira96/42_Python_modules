#!/usr/bin/env python3

def check_temperature(temp_str):
    try:
        temp = int(temp_str)
        if temp < 0:
            print(f"Error: {temp}°C it too cold for plants (min 0°C)\n")
        elif temp > 40:
            print(f"Error: {temp}°C it too hot for plants (max 40°C)\n")
        else:
            print(f"Temperature {temp}°C is perfect for plants\n")
    except ValueError:
        print(f"Error: '{temp_str}\' is not a valid number\n")


def main():
    print("=== Garden Temperature Checker ===\n")
    values = ["25", "abc", "100", "-50"]
    for value in values:
        print(f"testing temperature: {value}")
        check_temperature(value)
    print("All tests completed - program didn't crash!")


if __name__ == "__main__":
    main()
