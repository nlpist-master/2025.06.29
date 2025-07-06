# Step 2 – Thread Pool


import time
from concurrent.futures import ThreadPoolExecutor


def print_sequence(name, count):
    for i in range(count):
        print(f"Thread {name}: i={i}")
        time.sleep(0.3)


with ThreadPoolExecutor(max_workers=2) as executor:
    values = [("Alpha", 5), ("Beta", 3), ("Gamma", 4)]
    for name, value in values:
        executor.submit(print_sequence, name, value)

print("All threads have finished execution!")