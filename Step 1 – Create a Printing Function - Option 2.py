import threading
import time


# ✅ Step 1 – Create a Printing Function
def print_sequence(count):
    for i in range(count):
        print(f"Thread {threading.current_thread().name}: i={i}")
        time.sleep(0.3)


# Creating threads
thread1 = threading.Thread(name="Alpha", target=print_sequence, args=(5,))
thread2 = threading.Thread(name="Beta", target=print_sequence, args=(3,))
thread3 = threading.Thread(name="Gamma", target=print_sequence, args=(4,))

# Starting threads
thread1.start()
thread2.start()
thread3.start()

# Waiting for all of them to finish
thread1.join()
thread2.join()
thread3.join()

print("All threads have finished execution!")