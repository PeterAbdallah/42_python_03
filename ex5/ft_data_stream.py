#!/usr/bin/env python3

import typing
import random


# Generate event
def gen_event() -> typing.Generator[tuple[str, str], None, None]:
    players = ["bob", "alice", "dylan", "charlie"]
    actions = ["run", "swim", "climb", "move", "eat",
               "sleep", "grab", "release"]
    while True:
        yield (random.choice(players), random.choice(actions))


# Remove event and yield it
def consume_event(events: list[tuple[str, str]]) -> typing.Generator[
     tuple[str, str], None, None]:
    while events:
        i = random.randrange(len(events))
        yield events.pop(i)


# MAIN PROGRAM
def ft_data_stream() -> None:
    print("=== Game Data Stream Processor ===")

    # Generate 1000 events
    g = gen_event()
    for i in range(1000):
        t = next(g)
        print(f"Event {i}: Player {t[0]} did action {t[1]}")

    # Build list of 10 events
    lst = [next(g) for _ in range(10)]
    print(f"Built list of 10 events: {lst}")

    # Consume events
    for event in consume_event(lst):
        print(f"\nGot event from list: {event}")
        print(f"Remains in list: {lst}")


if __name__ == "__main__":
    ft_data_stream()
