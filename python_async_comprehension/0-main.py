#!/usr/bin/env python3
"""
This module contains the coroutine async_generator.
"""

import asyncio
import random
from typing import AsyncGenerator

async def async_generator() -> AsyncGenerator[float, None]:
    """
    Coroutine that asynchronously generates 10 random numbers between 0 and 10,
    waiting 1 second between each number.

    Yields:
        float: A random floating-point number between 0 and 10.
    """
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
