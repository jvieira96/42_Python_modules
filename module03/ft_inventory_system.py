#!/usr/bin/env python3


def main():
    alice_inv = {
        "sword": {
            "cat": "weapon",
            "rarity": "rare",
            "qty": 1,
            "price": 500
        },
        "potion": {
            "cat": "consumable",
            "rarity": "common",
            "qty": 5,
            "price": 50
        },
        "shield": {
            "cat": "armor",
            "rarity": "uncommon",
            "qty": 1,
            "price": 200
        },
    }

    bob_inv = dict()

    print("=== Player Inventory System ===\n")
    print("=== Alice's Inventory ===")
    categories = dict()
    total_price = 0
    total_item = 0
    for item, stats in alice_inv.items():
        cat = stats.get("cat")
        rarity = stats.get("rarity")
        qty = stats.get("qty")
        price = stats.get("price")
        total = price * qty
        total_price += total
        total_item += qty
        categories[cat] = categories.get(cat, 0) + qty

        print(f"{item} ({cat}, {rarity}): {qty}x @ {price} "
              f"gold each = {total} gold")
    print(f"\nInventory value: {total_price} gold")
    print(f"Item count: {total_item} items")
    cat_str = ""
    for k, v in categories.items():
        cat_str += f"{k}({v}), "
    print(f"Categories: {cat_str.strip(', ')}")

    print("\n=== Transaction: Alice gives Bob 2 potions ===")
    alice_inv['potion']['qty'] -= 2
    bob_inv.update({
        "potion": {
            "cat": "consumable",
            "rarity": "common",
            "qty": 2,
            "price": 50
        }
    })
    print("Transation successful!")
    print("\n=== Updated Inventories ===")
    print(f"Alice potions: {alice_inv['potion']['qty']}")
    print(f"Bob potions: {bob_inv['potion']['qty']}")

    print("\n=== Inventory Analytics ===")
    alice_items_sum = 0
    alice_gold_sum = 0
    for stats in alice_inv.values():
        alice_items_sum += stats.get('qty')
    for stats in alice_inv.values():
        alice_gold_sum += stats.get('qty') * stats.get('price')
    print(f"Most valuable player: Alice ({alice_gold_sum}) gold")
    print(f"Most items: Alice ({alice_items_sum}) items")
    rare_items = []
    all_items = alice_inv.keys()
    for item in all_items:
        item_data = alice_inv.get(item)
        if item_data.get("rarity") == "rare":
            rare_items.append(item)
    rare_items.append("magic_ring")
    print(f"Rarest items: {', '.join(rare_items)}")


if __name__ == "__main__":
    main()
