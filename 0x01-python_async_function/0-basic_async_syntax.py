#!/usr/bin/env python3

"""
This module contains an asynchronous coroutine that waits for a random delay
between 0 and max_delay seconds.
"""

import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """
    Asynchronous coroutine that waits for a random delay between 0
    and max_delay seconds and eventually returns it.

    Args:
        max_delay (int): Maximum delay in seconds. Defaults to 10.

    Returns:
        float: Random delay between 0 and max_delay seconds.
    """
    delay = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay

if __name__ == "__main__":
    asyncio.run(wait_random())
