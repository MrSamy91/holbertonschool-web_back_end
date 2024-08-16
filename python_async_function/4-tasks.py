#!/usr/bin/env python3
""" create asyncio.Tasks for wait_random function """
import asyncio
from typing import List
task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """ create asyncio.Tasks for wait_random """
    tasks = []
    for _ in range(n):
        tasks.append(task_wait_random(max_delay))
    sorted_delays = await asyncio.gather(*tasks)
    return sorted(sorted_delays)
