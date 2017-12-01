import asyncio


async def slow(x=1, delay=0.1):
    """some async test function
    """
    await asyncio.sleep(delay)
    return x*2
