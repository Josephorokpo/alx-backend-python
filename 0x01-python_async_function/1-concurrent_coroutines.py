#!/usr/bin/env python3

"""
This module contains an asynchronous coroutine that waits for a random delay
between 0 and max_delay seconds, and another coroutine to spawn multiple
instances of wait_random.
"""


import asyncio
from typing import List
from random_delay import wait_random


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
    delays = await asyncio.gather(*(wait_random(max_delay) for _ in range(n)))
    delays.sort()  # Sort the delays in ascending order
    return delays

if __name__ == "__main__":
    asyncio.run(wait_n(5, 10))
