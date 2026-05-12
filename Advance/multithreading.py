import threading
import time


def func(seconds):
    print(f"Function started, will take {seconds} seconds")
    time.sleep(seconds)
    print(f"Function completed after {seconds} seconds")

t1 = time.perf_counter()  # Start timer
# func(4)  
# Create threads
th1 = threading.Thread(target=func, args=[4])
print("Thread created, starting now...")
th1.start()  # Start the thread to run the function in parallel
print("\nMain thread continues to run while the function is executing...")
t2 = time.perf_counter()  # End timer
print(f"Time taken to execute the function: {t2 - t1} seconds")