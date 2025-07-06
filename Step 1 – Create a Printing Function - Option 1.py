import threading
import time


# ✅ Step 1 – Create a Printing Function


def print_sequence(name, count):
    for i in range(count):
        print(f"Thread {name}: i={i}")
        time.sleep(0.3)


# Creating threads
thread1 = threading.Thread(target=print_sequence, args=("Alpha", 5))
thread2 = threading.Thread(target=print_sequence, args=("Beta", 3))
thread3 = threading.Thread(target=print_sequence, args=("Gamma", 4))

# Starting threads
thread1.start()
thread2.start()
thread3.start()

# Waiting for all of them to finish
thread1.join()
thread2.join()
thread3.join()

print("All threads have finished execution!")