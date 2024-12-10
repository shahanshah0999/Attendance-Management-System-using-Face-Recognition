import time

def debounce(func, wait):
    last_called = 0

    def wrapper(*args, **kwargs):
        nonlocal last_called
        now = time.time()
        if now - last_called > wait:
            last_called = now
            return func(*args, **kwargs)

    return wrapper
