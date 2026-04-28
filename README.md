_This project has been created as part of the 42 curriculum by pabdalla_

# Data Quest - Mastering Python Collections

## Evaluator Instructions

### Running the scripts
Replace with necessary values
```bash
python3 {exercise.py} [arguments]
# or directly if the shebang is set:
./{exercise_path.py} [arguments]
```

### Checking code standards
```bash
flake8      # style linter
mypy ./     # type checker
```

---

## Overview

This project builds a game analytics platform using Python's core collection types.
Starting from command-line argument parsing and progressing through lists, tuples, sets,
dictionaries, generators, and comprehensions, each exercise introduces a new data structure
and demonstrates why choosing the right container matters both for correctness and performance.

---

## Concepts Covered

- Accessing and iterating over `sys.argv` as a list
- Storing and processing ordered data with lists
- Using tuples to represent fixed, immutable records (e.g. 3D coordinates)
- Leveraging sets for unique-element collections and set operations (union, intersection, difference)
- Mapping key-value data with dictionaries and operating on their keys and values
- Writing generator functions with `yield` to produce data on demand
- Using `next()` and `for..in` with generators
- Transforming and filtering collections concisely with list and dictionary comprehensions
- Type hints and code standards with `mypy` and `flake8`

---

## Key Python Concepts

### Lists
- Ordered, indexed, and mutable — elements can be added, removed, or changed
- Accessed by index: `my_list[0]`
- `sys.argv` is itself a list — the first entry is the program name, the rest are user arguments
- Useful built-ins: `len()`, `sum()`, `max()`, `min()`

### Tuples
- Ordered like lists, but **immutable** — once created, their contents cannot change
- Ideal for fixed records such as coordinates: `(x, y, z)`
- Can be unpacked: `x, y, z = my_tuple`
- Hashable, so they can be used as dictionary keys or stored in sets

### Sets
- Unordered collections of **unique** elements — duplicates are discarded automatically
- Support mathematical set operations:
  - `union()` — all elements from both sets
  - `intersection()` — only elements present in all sets
  - `difference()` — elements in one set but not another
- An empty set must be created with `set()`, not `{}` (which creates an empty dict)

### Dictionaries
- Store data as **key-value pairs**: `{"sword": 1, "potion": 5}`
- Keys must be unique, values can be any type
- Access values by key: `my_dict["sword"]`
- Useful methods: `dict.keys()`, `dict.values()`, `dict.update()`
- Insertion order is preserved in Python 3.7+

### Generators
- Functions that use `yield` instead of `return` to produce values **one at a time**
- Do not store all values in memory — ideal for large or infinite data streams
- Each call to `next()` resumes the function from where it last yielded
- Can be iterated directly with `for item in my_generator()`
- Type hint: `typing.Generator`

### Comprehensions
- Compact, single-line syntax for building new collections from existing ones
- **List comprehension**: `[expr for item in iterable if condition]`
- **Dict comprehension**: `{key: value for item in iterable if condition}`
- **Set comprehension**: `{expr for item in iterable}`
- Each comprehension should fit on one line unless it exceeds the line length limit

---

## Exercise Summary

| Exercise | File | Data Structure | Concepts |
|----------|------|----------------|----------|
| 0 | `ex0/ft_command_quest.py` | List (`sys.argv`) | Accessing command-line arguments |
| 1 | `ex1/ft_score_analytics.py` | List | Building lists, stats, error handling |
| 2 | `ex2/ft_coordinate_system.py` | Tuple | Immutable records, 3D distance calculation |
| 3 | `ex3/ft_achievement_tracker.py` | Set | Union, intersection, difference operations |
| 4 | `ex4/ft_inventory_system.py` | Dictionary | Key-value parsing, `.keys()`, `.values()`, `.update()` |
| 5 | `ex5/ft_data_stream.py` | Generator | `yield`, `next()`, `for..in` with generators |
| 6 | `ex6/ft_data_alchemist.py` | Comprehensions | List and dict comprehensions, filtering, transforming |

---