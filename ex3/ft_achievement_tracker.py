#!/usr/bin/env python3

import random


def gen_player_achievements(achievements: list[str]) -> set[str]:
    count = random.randint(10, 15)
    return set(random.sample(achievements, count))


def ft_achievement_tracker() -> None:
    players = ["Alice", "Bob", "Charlie", "Dylan"]
    achievements = [
        "First Steps",
        "Boss Slayer",
        "Speed Runner",
        "Collector Supreme",
        "World Savior",
        "Master Explorer",
        "Untouchable",
        "Strategist",
        "Crafting Genius",
        "Survivor",
        "Sharp Mind",
        "Treasure Hunter",
        "Unstoppable",
        "Hidden Path Finder",
        "Dragon Slayer",
        "Night Owl",
        "Early Bird",
        "Pacifist",
        "Completionist",
        "Ghost",
        "Iron Will",
        "Lucky Shot",
        "Combo King",
        "Legend",
        "Shadow Walker",
        "Pathfinder",
        "Tactician",
        "Demolisher",
        "Lone Wolf",
        "Team Player"
    ]

    # Generate achievements
    print("=== Achievement Tracker System ===\n")
    player_achievements = {}
    for player in players:
        player_achievements[player] = gen_player_achievements(achievements)
    for player, ach in player_achievements.items():
        print(f"Player {player}: {ach}")

    # Union
    all_achievements: set[str] = set()
    for ach in player_achievements.values():
        all_achievements = all_achievements.union(ach)
    print(f"\nAll distinct achievements: {all_achievements}\n")

    # Intersection
    common_achievements = set(achievements)
    for ach in player_achievements.values():
        common_achievements = common_achievements.intersection(ach)
    print(f"Common achievements: {common_achievements}\n")

    # Difference
    for player, ach in player_achievements.items():
        others: set[str] = set()
        for other_player, other_achievements in player_achievements.items():
            if other_player != player:
                others = others.union(other_achievements)
        unique = ach.difference(others)
        print(f"Only {player} has: {unique}")

    print()
    # Missing
    full_set = set(achievements)
    for player, ach in player_achievements.items():
        missing = full_set.difference(ach)
        print(f"{player} is missing: {missing}\n")


if __name__ == "__main__":
    ft_achievement_tracker()
