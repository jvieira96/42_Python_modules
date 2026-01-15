#!/usr/bin/env python3

import math


def calculate_distance(pos1, pos2):
    x1, y1, z1 = pos1
    x2, y2, z2 = pos2

    distance = math.sqrt((x2 - x1)**2 + (y2 - y1)**2 + (z2 - z1)**2)
    return distance


def main():
    print("=== Game Coordinate System ===\n")

    p1 = (0, 0, 0)
    p2 = (10, 20, 5)
    d1 = calculate_distance(p1, p2)
    print(f"Position created: {p2}")
    print(f"Distance between {p1} and {p2}: {d1:.2f}\n")

    coord_string = "3,4,0"
    print(f"Parsing coordinates: \"{coord_string}\"")
    splited = coord_string.split(",")
    try:
        p3 = (int(splited[0]), int(splited[1]), int(splited[2]))
        print(f"Parsed position: {p3}")
        d2 = calculate_distance(p1, p3)
        print(f"Distance between {p1} and {p3}: {d2:.1f}\n")
    except ValueError as e:
        print(f"Error parsing coordinates: {e}")

    bad_string = "abc,def,ghi"
    print(f"Parsing invalid coordinates: \"{bad_string}\"")
    bad_splited = bad_string.split(",")
    try:
        p4 = (int(bad_splited[0]), int(bad_splited[1]), int(bad_splited[2]))
        print(f"Parsed position: {p4}")
        d3 = calculate_distance(p1, p4)
        print(f"Distance between {p1} and {p4}: {d3:.1f}\n")
    except ValueError as e:
        print(f"Error parsing coordinates: {e}")
        print(f"Error details - Type: ValueError, Args: {e.args}\n")

    print("Unpacking demonstration:")
    x3, y3, z3 = p3
    print(f"Player at x={x3}, y={y3}, z={z3}")
    print(f"Coordinates: X={x3}, Y={y3}, Z={z3}")


if __name__ == "__main__":
    main()
