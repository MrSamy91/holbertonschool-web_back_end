#!/usr/bin/env python3
"""parallel comprehensions"""
import asyncio
import time

async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """parallel comprehensions"""
    time1 = time.perf_counter()
    tasks = [async_comprehension() for _ in range(4)]
    await asyncio.gather(*tasks)
    time2 = time.perf_counter()
    return time2 - time1
