import time

def time_it(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"Time taken to execute {func.__name__}: {(end_time - start_time)*1000} seconds")
        return result

    return wrapper
