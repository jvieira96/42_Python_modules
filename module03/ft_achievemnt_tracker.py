#!/usr/bin/env python3


def main():
    alice_achiev = {"first_kill",
                    "level_10",
                    "treasure_hunter",
                    "speed_demon"}

    bob_achiev = {"first_kill",
                  "level_10",
                  "boss_slayer",
                  "collector"}

    charlie_achiev = {"level_10",
                      "treasure_hunter",
                      "boss_slayer",
                      "speed_demon",
                      "perfectionist"}

    print("=== Achievement Tracker System ===\n")
    print(f"Player alice achievements: {alice_achiev}")
    print(f"Player bob achievements: {bob_achiev}")
    print(f"Player charlie achievements: {charlie_achiev}")

    print("\n=== Achievement Analytics ===")
    print(f"All unique achievements: "
          f"{alice_achiev.union(bob_achiev, charlie_achiev)}")
    print(f"Total unique achievements: "
          f"{len(alice_achiev.union(bob_achiev, charlie_achiev))}")


    print(f"\nCommon to all players: "
          f"{alice_achiev.intersection(bob_achiev, charlie_achiev)}")
    only_alice = alice_achiev.difference(bob_achiev.union(charlie_achiev))
#   print(f"only_alice: {only_alice}")
    only_bob = bob_achiev.difference(alice_achiev.union(charlie_achiev))
#   print(f"only_bob: {only_bob}")
    only_charlie = charlie_achiev.difference(bob_achiev.union(alice_achiev))
#   print(f"only_charlie: {only_charlie}")
    print(f"Rare achievements (1 player:) "
          f"{only_alice.union(only_bob, only_charlie)}")

    print(f"\nAlice vs Bob common: {alice_achiev.intersection(bob_achiev)}")
    print(f"Alice unique: {alice_achiev.difference(bob_achiev)}")
    print(f"Bob unique: {bob_achiev.difference(alice_achiev)}")


if __name__ == "__main__":
    main()
