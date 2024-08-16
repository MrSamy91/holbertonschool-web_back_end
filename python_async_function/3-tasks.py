#!/usr/bin/env python3
""" create an asyncio.Task for wait_random function """
import asyncio
wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:
    """ create asyncio.Task for wait_random """
    task = asyncio.create_task(wait_random(max_delay))
    return task
