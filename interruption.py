import time

def interrupt_seconds(delay):
    def decorator(func):
        last_executed = 0

        def wrapper(*args, **kwargs):
            nonlocal last_executed
            current_time = time.time()
            if current_time - last_executed >= delay:
                last_executed = current_time
                return func(*args, **kwargs)

        return wrapper

    return decorator