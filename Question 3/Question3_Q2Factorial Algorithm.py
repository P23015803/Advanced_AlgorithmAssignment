import time

def calculate_factorial(n):
    """
    Calculates the factorial of a given number n iteratively.

    PRIMITIVE OPERATIONS COUNT:
    - Line 1: 1 assignment (result = 1) -> Cost: 1
    - Line 2: Loop initialization, n+1 comparisons, and n increments -> Cost: 2n + 2
    - Line 3: n multiplications and n assignments -> Cost: 2n
    - Line 4: 1 return statement -> Cost: 1
    """

    # SET result TO 1
    # FOR i FROM 1 TO n DO
    #     result = result * i
    # END FOR
    # RETURN result
    result = 1  # 1 operation (executed once)
    for i in range(1, n + 1):  # 2n + 2 operations (executed n times + exit check)
        result = result * i  # 2 operations (executed n times)
    return result  # 1 operation (executed once)

# Use to prove Big O Notation in Python Program
def main():
    # Test the factorial function with an input
    input_number = 5
    factorial_result = calculate_factorial(input_number)

    print(f"Calculation Result: The factorial of {input_number} is {factorial_result}\n")

    print("==================================================")
    print("      PROVING O(n) FOR CALCULATE_FACTORIAL        ")
    print("==================================================")

    # Testing sizes that double each time
    # SET test_sizes TO [4000, 8000, 16000]
    # SET previous_time TO NULL
    test_size = [4000, 8000, 16000]
    previous_time = None

    # FOR EACH size IN test_sizes DO
    #     SET start_time TO GET_CURRENT_TIME()
    #
    #     // Execute the factorial calculation for the current size
    #     CALL calculate_factorial(size)
    #
    #     SET duration TO GET_CURRENT_TIME() - start_time
    for size in test_size:
        start_time = time.time()
        calculate_factorial(size)
        duration = time.time() - start_time

        # IF previous_time IS NOT NULL THEN
        #         SET multiplier TO duration / previous_time
        #         PRINT "Input Size (n): " + size + " | Time: " + duration + "s | Grew by: " + multiplier + "x"
        #     ELSE
        #         PRINT "Input Size (n): " + size + " | Time: " + duration + "s | (Baseline)"
        #     END IF
        #
        #     // Update the baseline for the next iteration
        #     SET previous_time TO duration
        # END FOR
        if previous_time is not None:
            multiplier = duration / previous_time
            print(f"Input Size (n): {size:6,} | Time: {duration:.4f}s | Grew by: {multiplier:.2f}x")
        else:
            print(f"Input Size (n): {size:6,} | Time: {duration:.4f}s | (Baseline)")

        previous_time = duration

    print("==================================================")
    print("Expected Verdict: In a pure O(n) loop, doubling data (2x) doubles time (~2.00x).")
    print("==================================================")

if __name__ == "__main__":
    main()