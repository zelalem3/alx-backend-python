#!/usr/bin/env python3
"""
This module contains a coroutine, async_generator, with no arguments looping
 10 times, each time asynchronously wait 1 second, then yield a random number
 between 0 and 10. random module is used.
"""
import asyncio
from typing import Generator
import random


async def async_generator() -> Generator[float, None, None]:
    """
    async generator loops x10, each time asynchronously wait 1 second, then
    yield a random number
    """
    for i in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
