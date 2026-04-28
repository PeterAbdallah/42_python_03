#!/usr/bin/env python3
import math


def get_player_pos() -> tuple:
    input_message = "Enter new coordinates as floats in format 'x,y,z': "
    while True:
        try:
            user_input = input(input_message)
            split_str = user_input.split(',')
            if len(split_str) != 3:
                raise ValueError("Invalid syntax")
            result = []
            for value in split_str:
                try:
                    result.append(float(value))
                except ValueError as e:
                    print(f"Error on parameter {value}: {e}")
                    raise
            return (result[0], result[1], result[2])
        except ValueError as e:
            if (str(e) == "Invalid syntax"):
                print(e)


def ft_coordinate_system() -> None:
    print("=== Game coordinate System ===")

    # Get first tuple
    print("\nGet a first set of coordinates")
    tuple = get_player_pos()
    print(f"Got a first tuple: {tuple}")
    print(f"It includes: X={tuple[0]}, Y={tuple[1]}, Z={tuple[2]}")
    distance_center = math.sqrt(tuple[0]**2 + tuple[1]**2 + tuple[2]**2)
    print(f"Distance to center: {distance_center:.4f}")

    # Get second tuple
    print("\nGet a second set of coordinates")
    tuple2 = get_player_pos()
    distance_center = math.sqrt((tuple2[0] - tuple[0])**2 +
                                (tuple2[1] - tuple[1])**2 +
                                (tuple2[2] - tuple[2])**2)
    print(f"Distance between the 2 sets of coordinates: {distance_center:.4f}")


if __name__ == "__main__":
    ft_coordinate_system()
