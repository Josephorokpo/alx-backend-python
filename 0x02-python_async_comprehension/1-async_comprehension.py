#!/usr/bin/env python3
"""Task 2
"""
from typing import List
from importlib import import_module as using


# Importing async_generator from the previous task
async_generator = using('0-async_generator').async_generator


async def async_comprehension() -> List[int]:
    '''Collects 10 random numbers using an async comprehension
    over async_generator.

    Returns:
        List[int]: List of 10 random numbers.
    '''
    return [num async for num in async_generator()]
