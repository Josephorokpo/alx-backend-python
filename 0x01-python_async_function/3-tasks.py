#!/usr/bin/env python3

'''
This module contains a function to create an asyncio.
Task for wait_random function.
'''


import asyncio


wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:
    '''
    Creates an asyncio.Task for the wait_random function.

    Args:
        max_delay (int): Maximum delay in seconds for wait_random.

    Returns:
        asyncio.Task: A task representing the execution of wait_random.
    '''
    return asyncio.create_task(wait_random(max_delay))
