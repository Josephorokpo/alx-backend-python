#!/usr/bin/env python3
"""
Async Generator Module
----------------------

This module defines an asynchronous generator coroutine that
yields random numbers between 0 and 10 after waiting for 1
second asynchronously.

"""


import asyncio
import random


async def async_generator() -> 'AsyncGenerator[int, None]':
    """
    Generate random numbers asynchronously.

    This coroutine loops 10 times, each time asynchronously waits for 1 second,
    then yields a random number between 0 and 10.

    Yields:
        int: Random number between 0 and 10.

    """
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.randint(0, 10)
