import time


def slow(x=1, delay=0.1):
    """some blocking test function
    """
    time.sleep(delay)
    return x*2
