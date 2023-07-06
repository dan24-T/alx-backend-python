#!/usr/bin/env python3
""" tring and int/float to tuple"""
from typing import Callable, Iterator, Union, Optional, List, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """
    string k and an int 
    tuple.
    """

    return (k, v**2)
