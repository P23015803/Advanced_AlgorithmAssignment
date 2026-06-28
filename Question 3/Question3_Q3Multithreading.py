import time
from time import perf_counter_ns
import threading


def calculate_factorial(n):

    # SET result TO 1
    # FOR i FROM 1 TO n DO
    #     result = result * i
    # END FOR
    # RETURN result
    # Calculates the factorial of n iteratively.
    result = 1  # 1 operation (executed once)
    for i in range(1, n + 1):  # 2n + 2 operations (executed n times + exit check)
        result = result * i  # 2 operations (executed n times)
    return result  # 1 operation (executed once)

# FUNCTION multithreading_round()
#     SET start_time TO GET_CURRENT_TIME_IN_NANOSECONDS()
def multithreading_round():

    # 1. Initialize 3 separate threads, 1 for each factorial operation
    thread1 = threading.Thread(target=calculate_factorial, args=(50,))
    thread2 = threading.Thread(target=calculate_factorial, args=(100,))
    thread3 = threading.Thread(target=calculate_factorial, args=(200,))

    # 2. Start time right before the first thread is fired off
    # Capture the starting system time in nanoseconds
    start_time = perf_counter_ns()

    # Start execution across all threads
    thread1.start()
    thread2.start()
    thread3.start()

    # 3. Use join() to force the main script to wait until all threads finish
    thread1.join()
    thread2.join()
    thread3.join()

    # 4. End time right as the final thread terminates
    # Capture the ending system time in nanoseconds
    #     SET end_time TO GET_CURRENT_TIME_IN_NANOSECONDS()
    end_time = perf_counter_ns()

    # Return the formula: T = t2 - t1
    # Return the total elapsed duration
    #     RETURN end_time - start_time
    # END FUNCTION
    return end_time - start_time

def main():

    rounds = 10
    round_duration = []

    # Print the table header beautifully
    print("==================================================")
    print("     Q3: MULTITHREADED FACTORIAL PERFORMANCE      ")
    print("==================================================")
    print(f"{'Round':<10} | {'Time Elapsed (T) in Nanoseconds':<35}")
    print("-" * 50)

    # FOR turn FROM 1 TO rounds DO
    #     SET time_duration TO CALL without_multithreading_round()
    #     APPEND time_duration TO round_duration
    #
    #     PRINT "Round " + turn + " | " + time_duration + " ns"
    for turn in range(1, rounds + 1):
        time_duration = multithreading_round()
        round_duration.append(time_duration)

        print(f"Round {turn:<5} | {time_duration:<35,} ns")

        #     SET average_time TO SUM(round_duration) / rounds
        #     PRINT "--------------------------------------------------"
        #     PRINT "Average T (10 Rounds): " + average_time + " ns"
        #     PRINT "=================================================="
        # END FOR
        # Calculate and display the running average for each iteration
        average_time = sum(round_duration) / rounds
        print("-" * 50)
        print(f"Average T (10 Rounds): {average_time:,.2f} ns")
        print("==================================================")

    print("------ Overall table (Average) ------")
    index = 0
    for duration in round_duration:
        index += 1
        print(f"{index:<3}: {duration:.2f} ns")

    print(f"Average T (10 Rounds): {average_time:,.2f} ns")
    print("==================================================")

if __name__ == "__main__":
    main()