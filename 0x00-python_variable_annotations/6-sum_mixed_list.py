#!/usr/bin/env python3

""" mixed """
from typing import Union, List


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """  sum as a float. """
    return float(sum(mxd_lst))
