#!/usr/bin/env python3

import sys

def main():
    args = sys.argv
    argc = len(args)

    print("=== Command Quest ===")
    if argc == 1:
        print("No arguments provided!")
        print(f"Program name: {args[0]}")
        print("Total arguments: 1")
    else:
        print(f"Program name: {args[0]}")
        print(f"Arguments received: {argc - 1}")
        for i in range(1, argc):
            print(f"Argument {i}: {args[i]}")
        print(f"Total arguments: {argc}")

if __name__ == "__main__":
    main()