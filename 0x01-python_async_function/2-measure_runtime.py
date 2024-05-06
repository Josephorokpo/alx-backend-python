#!/usr/bin/env python3

'''
This module contains a function to measure the runtime of wait_n function.
'''

import asyncio
import time
from typing import Callable

wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_runtime(n: int, max_delay: int) -> float:
    '''
    Measures the total execution time for wait_n(n, max_delay) and returns
    total_time / n.

    Args:
        n (int): Number of times to spawn wait_random.
        max_delay (int): Maximum delay in seconds for wait_random.

    Returns:
        float: Average execution time per call to wait_random.
    '''
    start_time = time.time()
    asyncio.run(wait_n(n, max_delay))
    end_time = time.time()
    total_time = end_time - start_time
    return total_time / n


if __name__ == "__main__":
    n = 5
    max_delay = 10
    avg_runtime = measure_runtime(n, max_delay)
    print(f"Average runtime per call: {avg_runtime} seconds")
