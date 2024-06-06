#!/usr/bin/env python3
"""A module for task 2"""


def floor(n: float) -> int:
    """floor: calculates the floor for a number"""
    if n >= 0:
        return int(n - (n % 1))
    else:
        return int(n - (1 - (n % 1)))
