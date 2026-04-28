#!/usr/bin/env python3

import sys


def ft_command_quest() -> None:
    argc = len(sys.argv)
    print("=== Command Quest ===")
    print(f"Program name: {sys.argv[0]}")
    if argc < 2:
        print("No arguments provided!")
    else:
        print(f"Arguments received: {argc - 1}")
    for i in range(1, argc):
        print(f"Argument {i}: {sys.argv[i]}")

    # Method 2
    # i = 1
    # for arg in sys.argv[1:]:
    #     print(f"Argument {i}:  {arg}")

    print(f"Total arguments: {argc}")


if __name__ == "__main__":
    ft_command_quest()
