# Making a python program, test whether multithreading in python is Concurrent or Parallel

import time
import threading

# FUNCTION cpu_bound_task()
#     SET count TO 0
#     FOR i FROM 1 TO 20000000 DO
#         INCREMENT count BY 1
#     END FOR
# END FUNCTION
# Make a heavy task
def cpu_bound_task():
    count = 0

    for i in range(20000000):
        count += 1

# FUNCTION main()
#     // --- 1. Running Sequentially ---
#     PRINT "--- 1. Running Sequentially ---"
#     SET start_time TO GET_CURRENT_TIME()
def main():
    print("--- 1. Running Sequentially ---")
    start_time = time.time()

    # Run two task sequentially
    #     CALL cpu_bound_task()
    #     CALL cpu_bound_task()
    cpu_bound_task()
    cpu_bound_task()

    # SET end_time TO GET_CURRENT_TIME()
    # SET sequential_duration TO end_time - start_time
    # PRINT "Sequential Time: " + sequential_duration + " seconds"
    end_time = time.time()
    sequential_duration = end_time - start_time
    print(f"Sequential Time: {sequential_duration:.2f} seconds\n")

    # // --- 2. Running Concurrently using Multithreading ---
    #     PRINT "--- 2. Running Concurrently using Multithreading ---"
    #
    #     // Initialize two separate threads targeting the task
    #     SET thread1 TO INITIALIZE_THREAD(target=cpu_bound_task)
    #     SET thread2 TO INITIALIZE_THREAD(target=cpu_bound_task)
    #
    #     SET start_time TO GET_CURRENT_TIME()
    print("--- 2. Running Concurrently using Multithreading ---")
    thread1 = threading.Thread(target=cpu_bound_task)
    thread2 = threading.Thread(target=cpu_bound_task)

    start_time = time.time()

    # Make two task run, to check if two task run at the same time or concurrently
    # START thread1
    # START thread2
    thread1.start()
    thread2.start()

    # Wait for both threads to finish before moving forward
    # JOIN thread1
    # JOIN thread2
    thread1.join()
    thread2.join()

    # SET end_time TO GET_CURRENT_TIME()
    #     SET threaded_duration TO end_time - start_time
    #     PRINT "Multithreaded Time: " + threaded_duration + " seconds"
    # END FUNCTION
    end_time = time.time()
    threaded_duration = end_time - start_time
    print(f"Multithreaded Time: {threaded_duration:.2f} seconds\n")

    # 3. The Automated Proof Logic
    print("=" * 50)
    print("PROVING CONCURRENCY VS PARALLELISM:")
    print(f"Multithreaded time is {threaded_duration:.2f}s vs Sequential time {sequential_duration:.2f}s.")

    # If multithreading saves substantial time (at least 15% faster), it's parallel.
    # Otherwise, if it's near or slower than sequential, it's concurrent.
    if threaded_duration < (sequential_duration * 0.85):
        print("\nPARALLEL PROCESSING")
        print("Reason: The output time is significantly lesser than sequential. ")
        print("The CPU cores worked simultaneously on both tasks.")
    else:
        print("\nCONCURRENT PROCESSING")
        print("Reason: The output time is nearly the same (or slower) than sequential.")
        print("The threads were forced to share a single core due to Python's GIL.")
    print("=" * 50)

if __name__ == "__main__":
    main()