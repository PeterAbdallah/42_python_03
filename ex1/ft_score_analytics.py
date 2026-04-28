#!/usr/bin/env python3
import sys


def ft_score_analytics() -> None:
    print("=== Player Score Analytics ===")

    argc = len(sys.argv)
    if argc < 2:
        print("No scores provided. Usage: python3\
 ft_score_analytics.py <score1> <score2> ...")
    else:
        scores = []
    for score in sys.argv[1:]:
        try:
            scores.append(int(score))
        except ValueError:
            print(f"Invalid parameter: '{score}'")
    if len(scores) == 0:
        print("No scores provided. Usage: python3\
 ft_score_analytics.py <score1> <score2> ...")
    else:
        print(f"Scores processed: {scores}")
        print(f"Total players: {len(scores)}")
        print(f"Total score: {sum(scores)}")
        print(f"Average score: {sum(scores) / len(scores)}")
        print(f"High score: {max(scores)}")
        print(f"Low score: {min(scores)}")
        print(f"Score range: {max(scores) - min(scores)}")


if __name__ == "__main__":
    ft_score_analytics()
