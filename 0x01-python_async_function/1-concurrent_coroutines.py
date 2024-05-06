#!/usr/bin/env python3
"""
This module contains an asynchronous coroutine that waits for a random delay
between 0 and max_delay seconds, and another coroutine to spawn multiple
instances of wait_random.
"""


import asyncio
from typing import List


wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """
    Asynchronous routine that spawns wait_random n times with the specified
    max_delay and returns a list of all the delays in ascending order.

    Args:
        n (int): Number of times to spawn wait_random.
        max_delay (int): Maximum delay in seconds for wait_random.

    Returns:
        List[float]: List of delays in ascending order.
    """
    wait_times = await asyncio.gather(
        *tuple(map(lambda _: wait_random(max_delay), range(n)))
    )
    return sorted(wait_times)
