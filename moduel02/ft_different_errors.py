#!/usr/bin/env python3

def garden_operations():
    print("Testing ValueError...")
    try:
        int("abc")
    except ValueError as e:
        print(f"Caught ValueError: {e}\n")

    print("Testing ZeroDivisionError...")
    try:
        result = 3 / 0
        print(result)
    except ZeroDivisionError as e:
        print(f"Caught ZeroDivisionError: {e}\n")

    print("Testing FileNotFound...")
    try:
        with open("missing.txt", "r"):
            pass
    except FileNotFoundError as e:
        print(f"Caught FileNotFound: {e}\n")

    print("Testing KeyError...")
    try:
        plants = {"Rose": "Red", "Lily": "White"}
        print(plants["Cactus"])
    except KeyError as e:
        print(f"Caught KeyError: {e}\n")

    print("Testing multiple errors together...")
    try:
        int("lol")
    except (ValueError, ZeroDivisionError, KeyError, FileNotFoundError):
        print("Caught an error, but program continues!\n")


def main():
    print("=== Garden Error Types Demo ===\n")
    garden_operations()
    print("All error types tested succefully!")


if __name__ == "__main__":
    main()
