#!/usr/bin/env python3
""" functions"""
from typing import Callable, Iterator, Union, Optional, List, Tuple


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """
    takes a float multiplier as argument
    """
    def f(i: float) -> float:
        """ float multiplier """
        return float(i * multiplier)

    return f
