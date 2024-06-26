#!/usr/bin/env python3
'''
This module contains a function to create an asyncio.Task for wait_n function.
'''import asyncio
from typing import List


task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    '''
    Asynchronous routine that spawns task_wait_random n times
    with the specified max_delay and returns a list of all
    the delays in ascending order.

    Args:
        n (int): Number of times to spawn task_wait_random.
        max_delay (int): Maximum delay in seconds for task_wait_random.

    Returns:
        List[float]: List of delays in ascending order.
    '''
    wait_times = await asyncio.gather(
        *tuple(map(lambda _: task_wait_random(max_delay), range(n)))
    )
    return sorted(wait_times)
