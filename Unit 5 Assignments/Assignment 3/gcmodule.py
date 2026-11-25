import gc
import time
import tracemalloc

class Demo:
    def __init__(self):
        self.ref = None

def create_objects(n):
    for i in range(n):
        obj1 = Demo()
        obj2 = Demo()

        obj1.ref = obj2
        obj2.ref = obj1

def memory_usage():
    current, peak = tracemalloc.get_traced_memory()

    print("Current Memory:", round(current / 1024, 2), "KB")
    print("Peak Memory:", round(peak / 1024, 2), "KB")

def main():

    print("GARBAGE COLLECTION EXPERIMENT")

    tracemalloc.start()

    print("\n--- Automatic Garbage Collection ---")

    gc.enable()

    start = time.time()
    create_objects(100000)
    end = time.time()

    print("Execution Time:", round(end - start, 4), "seconds")

    memory_usage()

    print("\n--- Manual Garbage Collection ---")

    gc.disable()

    start = time.time()
    create_objects(100000)
    end = time.time()

    print("Object Creation Time:", round(end - start, 4), "seconds")

    print("\nMemory Before Manual Collection:")
    memory_usage()

    start = time.time()

    collected = gc.collect()

    end = time.time()

    print("\nObjects Collected:", collected)
    print("Garbage Collection Time:",
          round(end - start, 4), "seconds")

    print("\nMemory After Manual Collection:")
    memory_usage()

    gc.enable()

    print("\nAutomatic Garbage Collection Enabled:",
          gc.isenabled())

    tracemalloc.stop()

if __name__ == "__main__":
    main()
