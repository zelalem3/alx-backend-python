#!/usr/bin/env python3
"""Python and Async functions"""
import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """returns a delayed value"""
    delayed_value = random.uniform(0, max_delay)
    await asyncio.sleep(delayed_value)
    return delayed_value
