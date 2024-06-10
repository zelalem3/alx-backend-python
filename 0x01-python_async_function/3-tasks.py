#!/usr/bin/env python3
"""Python and Async asyncio Task"""
import asyncio

wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:
    """returns an asyncio Task"""
    return asyncio.create_task(wait_random(max_delay))
