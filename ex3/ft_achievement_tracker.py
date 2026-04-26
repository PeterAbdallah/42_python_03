#!/usr/bin/env python3

import random


def gen_player_achievements(ACHIEVEMENTS) -> set:
    count = random.randint(5, 10)
    return set(random.sample(ACHIEVEMENTS, count))


def ft_achievement_tracker() -> None:
    PLAYERS = ["Alice", "Bob", "Charlie", "Dylan"]
    ACHIEVEMENTS = [
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
    for player in PLAYERS:
        player_achievements[player] = gen_player_achievements(ACHIEVEMENTS)
    for player, achievements in player_achievements.items():
        print(f"Player {player}: {achievements}")

    # Union
    all_achievements: set[str] = set()
    for achievements in player_achievements.values():
        all_achievements = all_achievements.union(achievements)
    print(f"\nAll distinct achievements: {all_achievements}\n")

    # Intersection
    common_achievements = set(ACHIEVEMENTS)
    for achievements in player_achievements.values():
        common_achievements = common_achievements.intersection(achievements)
    print(f"Common achievements: {common_achievements}\n")

    # Difference
    for player, achievements in player_achievements.items():
        others: set[str] = set()
        for other_player, other_achievements in player_achievements.items():
            if other_player != player:
                others = others.union(other_achievements)
        unique = achievements.difference(others)
        print(f"Only {player} has: {unique}")

    print()
    # Missing
    full_set = set(ACHIEVEMENTS)
    for player, achievements in player_achievements.items():
        missing = full_set.difference(achievements)
        print(f"{player} is missing: {missing}\n")


if __name__ == "__main__":
    ft_achievement_tracker()
