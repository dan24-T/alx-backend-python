#!/usr/bin/env python3
"""async"""
from typing import List
import asyncio
task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """Spawns wait_random n"""
    fut = [task_wait_random(max_delay) for _ in range(n)]
    fut = asyncio.as_completed(fut)
    de = [await future for future in fut]
    return de
