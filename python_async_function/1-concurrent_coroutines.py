#!/usr/bin/env python3
""" asynchronous routine to spawn wait_random
n times with specified max_delay """
import asyncio
from typing import List
from random import uniform
from asyncio import create_task

wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """Spawns wait_random n times with specified max_delay."""
    delays = [create_task(wait_random(max_delay)) for _ in range(n)]
    return sorted([await delay for delay in delays])
