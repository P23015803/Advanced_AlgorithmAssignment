import time
from time import perf_counter_ns


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

# FUNCTION without_multithreading_round()
#     SET start_time TO GET_CURRENT_TIME_IN_NANOSECONDS()
def without_multithreading_round():

    # Capture the starting system time in nanoseconds
    start_time = perf_counter_ns()

    # Execute the factorial calculations sequentially
    #     CALL calculate_factorial(50)
    #     CALL calculate_factorial(100)
    #     CALL calculate_factorial(150)
    calculate_factorial(50)
    calculate_factorial(100)
    calculate_factorial(150)

    # Capture the ending system time in nanoseconds
    #     SET end_time TO GET_CURRENT_TIME_IN_NANOSECONDS()
    end_time = perf_counter_ns()

    # Return the total elapsed duration
    #     RETURN end_time - start_time
    # END FUNCTION
    return end_time - start_time

def main():

    rounds = 10
    round_duration = []

    # Print the table header beautifully
    print("==================================================")
    print("      Q4: SEQUENTIAL FACTORIAL PERFORMANCE        ")
    print("==================================================")
    print(f"{'Round':<10} | {'Time Elapsed (T) in Nanoseconds':<35}")
    print("-" * 50)

    # FOR turn FROM 1 TO rounds DO
    #     SET time_duration TO CALL without_multithreading_round()
    #     APPEND time_duration TO round_duration
    #
    #     PRINT "Round " + turn + " | " + time_duration + " ns"
    for turn in range(1, rounds + 1):
        time_duration = without_multithreading_round()
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