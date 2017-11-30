import time


def slow(x=1, delay=0.1):
    time.sleep(delay)
    return x*2
