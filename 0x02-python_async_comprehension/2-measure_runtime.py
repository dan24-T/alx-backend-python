#!/usr/bin/env python3

""" Comprehensions """

from asyncio import gather
from time import time

async_c = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """ parallel comprehensions """
    start = time()
    tasks = [async_c() for i in range(4)]
    await gather(*tasks)
    end = time()
    return (end - start)
