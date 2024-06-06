#!/usr/bin/env python3
""" Takes float, returns func that multiplies """

from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """ Returns multiplier function """
    return (lambda x: multiplier*x)
