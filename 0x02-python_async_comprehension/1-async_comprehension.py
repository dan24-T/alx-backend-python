#!/usr/bin/env python3

""" Comprehensions """

from asyncio import sleep
from random import uniform
from typing import List

async_g = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """ Comprehensions  """
    ac = [i async for i in async_g()]
    return ac
