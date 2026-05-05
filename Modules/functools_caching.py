from functools import lru_cache
import time

@lru_cache(maxsize=None)  # Cache results of the function
def func(n):
    print(f"Calculating for {n}...")
    time.sleep(4)  # Simulate a time-consuming calculation
    return n * n
print(func(4))  # First call, will take time
print(func(5))  # First call, will take time
print(func(4))  # Second call, will be fast due to caching