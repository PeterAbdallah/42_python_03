#!/usr/bin/env python3

import random


def ft_data_alchemist() -> None:
    print("=== Game Data Alchemist ===")
    players = ["Alice", "bob", "Charlie", "dylan", "Emma",
               "Gregory", "john", "kevin", "Liam"]

    print(f"\nInitial list of players: {players}")

    # ALL names capitalized
    capitalized = [name.capitalize() for name in players]
    print(f"New list of all names capitalized: {capitalized}")

    # Only capitalized names
    only_caps = [name for name in players if name == name.capitalize()]
    print(f"New list capitalized names only: {only_caps}")

    # Dictionaries
    scores = {key: random.randint(0, 1000) for key in capitalized}
    print(f"\nScore dict: {scores}")
    avg = sum(scores.values()) / len(scores)
    print(f"Score average: {avg:.2f}")
    high_scores = {name: score for name, score
                   in scores.items() if score > avg}
    print(f"High scores: {high_scores}")


if __name__ == "__main__":
    ft_data_alchemist()
