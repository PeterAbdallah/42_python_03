#!/usr/bin/env python3

import sys


def ft_inventory_system():
    print("=== Inventory System Analysis ===")

    inventory = {}
    argc = len(sys.argv)

    # Read arguments and create dictionary
    for i in range(1, argc):
        try:
            error = 0
            split_str = sys.argv[i].split(':')
            # Wrong syntax
            if len(split_str) != 2:
                raise ValueError(f"Error - invalid parameter '{sys.argv[i]}'")

            key = split_str[0]
            # Duplicate handling
            if key in inventory:
                raise ValueError(f"Redundant item '{key}'\
 - discarding")
            # Adding to dictionary
            error = 1
            quantity = int(split_str[1])
            inventory.update({split_str[0]: quantity})
        except ValueError as e:
            if error == 1:
                print(f"Quantity error for '{split_str[0]}': {e}")
            else:
                print(e)

    # Operate on dict
    key_list = list(inventory.keys())
    value_list = list(inventory.values())
    print(f"Got inventory: {inventory}")
    print(f"Item list: {key_list}")
    total_items = sum(inventory.values())
    print(f"Total quantity of the {len(key_list)} items: {total_items}")
    try:
        min_item = max_item = key_list[0]
        min_qty = max_qty = value_list[0]
        for item, qty in inventory.items():
            print(f"Item {item} represents {(qty*100)/total_items:.1f}%")
            if qty > max_qty:
                max_qty = qty
                max_item = item
            if qty < min_qty:
                min_qty = qty
                min_item = item
        print(f"Item most abundant: {max_item} with quanity {max_qty}")
        print(f"Item least abundant: {min_item} with quanity {min_qty}")
    except IndexError:
        print("=== Error: empty inventory ===")
    inventory.update({"magic_item": 1})
    print(f"Updated inventory: {inventory}")


if __name__ == "__main__":
    ft_inventory_system()
