#!/usr/bin/env python3

class SecurePlant:
    def __init__(self, name, height, age):
        self._name = name
        self._height = 0
        self._age = 0
        print(f"Plant created: {name}")
        self.set_height(height)
        self.set_age(age)

    def set_height(self, height):
        if height < 0:
            print(f"Invalid operation attempted: height {height}cm [REJECTED]")
            print("Security: Negative height rejected")
        else:
            self._height = height
            print(f"Height: updated: {height}cm [OK]")

    def set_age(self, age):
        if age < 0:
            print(f"Invalid operation attempted: age {age} days [REJECTED]")
            print("Security: Negative age rejected")
        else:
            self._age = age
            print(f"Age: updated: {age} days [OK]")

    def get_height(self):
        return self._height

    def get_age(self):
        return self._age

    def get_name(self):
        return self._name


if __name__ == "__main__":
    print("=== Garden Security System ===")
    rose = SecurePlant("Rose", 25, 30)
    print("\n")
    rose.set_height(-5)
    print("\n")
    print(f"Current plant: {rose.get_name()} "
          f"({rose.get_height()}cm, {rose.get_age()} days)")
