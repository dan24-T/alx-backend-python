#!/usr/bin/env python3
""" all basic"""

import asyncio
from typing import List

wait_rr = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """spawn delay.
    """
    tasks = [asyncio.create_task(wait_rr(max_delay)) for _ in range(n)]
    return [await task for task in asyncio.as_completed(tasks)]
