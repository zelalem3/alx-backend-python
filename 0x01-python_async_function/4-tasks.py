import asyncio
import random

async def task_wait_random(max_delay: float) -> float:
    """
    Wait for a random delay between 0 and max_delay seconds, then return the waited time.
    """
    wait_time = random.uniform(0, max_delay)
    await asyncio.sleep(wait_time)
    return wait_time

async def task_wait_n(n: int, max_delay: float) -> list[float]:
    """
    Create n tasks that each wait for a random delay between 0 and max_delay seconds, then return the list of waited times.
    """
    delay_times = await asyncio.gather(*[task_wait_random(max_delay) for _ in range(n)])
    return delay_times
