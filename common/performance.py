import time


def measure_performance(f):
    def wrapper():
        time_started = time.perf_counter()
        f()
        time_elapsed = time.perf_counter() - time_started
        print(f"Completed execution in {time_elapsed:.2f}s")
    return wrapper
