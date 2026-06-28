import time #Import time for calculating performance test
# CLASS Transaction:
#     PROPERTIES:
#         transaction_id    // Integer
#         customer_name     // String
#         product_name      // String
#         amount            // Decimal
#         transaction_date  // String (e.g., "YYYY-MM-DD")
#
#     CONSTRUCTOR(transaction_id, customer_name, product_name, amount, transaction_date):
#         self.transaction_id = transaction_id
#         self.customer_name = customer_name
#         self.product_name = product_name
#         self.amount = amount
#         self.transaction_date = transaction_date
#
#     //GETTER
#
#     //SETTER

class Transaction:
    def __init__(self, transaction_id, customer_name, product_name, amount, transaction_date):
        self.transaction_id = transaction_id
        self.customer_name = customer_name
        self.product_name = product_name
        self.amount = amount
        self.transaction_date = transaction_date

    def get_id(self):
        return self.transaction_id

    def get_customer(self):
        return self.customer_name

    def get_product(self):
        return self.product_name

    def get_amount(self):
        return self.amount

    def get_date(self):
        return self.transaction_date

    def set_id(self, transaction_id):
        self.transaction_id = transaction_id

    def set_customer(self, customer_name):
        self.customer_name = customer_name

    def set_product(self, product_name):
        self.product_name = product_name

    def set_amount(self, amount):
        self.amount = amount

    def set_date(self, transaction_date):
        self.transaction_date = transaction_date

# FUNCTION merge_sort(array_list, attribute)
#     // Access and increment the global tracker for recursive calls
#     GLOBAL recursion_count
#     SET recursion_count = recursion_count + 1
#
#     // Base Case: If the array has 1 or 0 elements, it is already sorted
#     IF LENGTH(array_list) <= 1 THEN
#         RETURN array_list
#     ENDIF
# 1. Merge Sort (DIVIDE and CONQUER)
def merge_sort(array_list, attribute):
    global recursion_count
    recursion_count += 1

    if len(array_list) <= 1:
        return array_list

    # Step 1: DIVIDE
    # Split the array into two halves around the midpoint.
    # mid = LENGTH(array_list) / 2  (Integer Division)
    # left_array = array_list[0 TO mid - 1]
    # right_array = array_list[mid TO LENGTH(array_list) - 1]
    mid = len(array_list) // 2
    left_array = array_list[:mid]
    right_array = array_list[mid:]

    # Step 2: CONQUER
    # Recursively solve the sub-problems by sorting both halves.
    # sorted_left = merge_sort(left_array)
    # sorted_right = merge_sort(right_array)
    sorted_left = merge_sort(left_array, attribute)
    sorted_right = merge_sort(right_array, attribute)

    # Step 3: MERGE
    #     RETURN merge(sorted_left, sorted_right)
    # ENDFUNCTION
    return merge(sorted_left, sorted_right, attribute)


# FUNCTION merge(left, right)
#     results = EMPTY LIST
#     i = 0
#     j = 0
def merge(left, right, attribute):
    # Initialize the merged list and compare key
    results = []
    i = 0
    j = 0

    # Compare elements from both sub-arrays and build the sorted list
    # WHILE i < LENGTH(left) AND j < LENGTH(right) DO
    while i < len(left) and j < len(right):

        # IF attribute == "amount" THEN
        #     SET left_value = CALL left[i].get_amount()
        #     SET right_value = CALL right[j].get_amount()
        if attribute == "amount":
            left_value = left[i].get_amount()
            right_value = right[j].get_amount()

        # ELSE IF attribute == "id" THEN
        #     SET left_value = CALL left[i].get_id()
        #     SET right_value = CALL right[j].get_id()
        elif attribute == "id":
            left_value = left[i].get_id()
            right_value = right[j].get_id()

        # ELSE
        #     PRINT "Attribute Value Not Assigned"
        #     RETURN -1
        # ENDIF
        else:
            print("Attribute Value Not Assigned")
            return -1

    #     IF left[i] <= right[j] THEN
    #         APPEND left[i] TO results
    #         i = i + 1
    #     ELSE
    #         APPEND right[j] TO results
    #         j = j + 1
    #     ENDIF
    # ENDWHILE
        if left_value <= right_value:
            results.append(left[i])
            i += 1
        else:
            results.append(right[j])
            j += 1

    # Append any remaining elements left over from either array
    #     APPEND ALL ELEMENTS FROM left[i TO END] TO results
    #     APPEND ALL ELEMENTS FROM right[j TO END] TO results
    #
    #     RETURN results
    # ENDFUNCTION
    results.extend(left[i:])
    results.extend(right[j:])

    return results


# 2. Binary Search (DIVIDE and CONQUER)
# FUNCTION binary_search(array_list, low, high, target)
#     // Check if the target value inside the list or not
#     IF low > high THEN
#         PRINT "The target wasn't inside the list"
#         RETURN
#     ENDIF
def binary_search(array_list, low, high, target, attribute):
    # Check is the target value inside the list or not
    if low > high:
        print("The target wasn't inside the list")
        return -1 # Makes it failed safely

    # Step 1: DIVIDE
    # Split the array into two halves around the midpoint.
    # mid = (low + high) / 2  (Integer Division)
    mid = (low + high) // 2

    # Step 2: CONQUER
    # IF attribute == "id" THEN
    if attribute == "id":

        # IF array_list[mid] == target THEN
        #     PRINT "Target value located at index: " + mid
        #     RETURN mid
        if array_list[mid].get_id() == target:
            print(f"Target value located at index: {mid}")
            return mid

        # If the target is smaller, recursively narrow the search to the left half.
        # ELSE IF array_list[mid] > target THEN
        #     RETURN binary_search(array_list, low, mid - 1, target)
        elif array_list[mid].get_id() > target:
            return binary_search(array_list, low, mid - 1, target, attribute)

        # If the target is larger, recursively narrow the search to the right half
        # ELSE IF array_list[mid] < target THEN
        #     RETURN binary_search(array_list, mid + 1, high, target)
        elif array_list[mid].get_id() < target:
            return binary_search(array_list, mid + 1, high, target, attribute)

        # ELSE
        #         PRINT "Some error occurred when search"
        #         RETURN
        #     ENDIF
        # ENDFUNCTION
        else:
            print("Some error occurred when search")
            return -1 # Makes it failed safely

    # ELSE IF attribute == "amount" THEN
    elif attribute == "amount":
        # IF array_list[mid] == target THEN
        #     PRINT "Target value located at index: " + mid
        #     RETURN mid
        if array_list[mid].get_amount() == target:
            print(f"Target value located at index: {mid}")
            return mid

        # If the target is smaller, recursively narrow the search to the left half.
        # ELSE IF array_list[mid] > target THEN
        #     RETURN binary_search(array_list, low, mid - 1, target)
        elif array_list[mid].get_amount() > target:
            return binary_search(array_list, low, mid - 1, target, attribute)

        # If the target is larger, recursively narrow the search to the right half
        # ELSE IF array_list[mid] < target THEN
        #     RETURN binary_search(array_list, mid + 1, high, target)
        elif array_list[mid].get_amount() < target:
            return binary_search(array_list, mid + 1, high, target, attribute)

        # ELSE
        #         PRINT "Some error occurred when search"
        #         RETURN
        #     ENDIF
        # ENDFUNCTION
        else:
            print("Some error occurred when search")
            return -1  # Makes it failed safely
    else:
        print("Error Occurred During Searching")
        return -1

# FUNCTION linear_search(array_list, target, attribute)
#     IF attribute == "id" THEN
#         // Iterate through the list by index
#         FOR index = 0 TO LENGTH(array_list) - 1 DO
#             IF CALL array_list[index].get_id() == target THEN
#                 RETURN index // Target found
#             ENDIF
#         ENDFOR
#         RETURN -1 // Target not found safely matches the menu logic
def linear_search(array_list, target, attribute):

    if attribute == "id":

        for index in range(len(array_list)):
            if array_list[index].get_id() == target:
                return index
        return -1

    # ELSE IF attribute == "amount" THEN
    #         // Iterate through the list by index
    #         FOR index = 0 TO LENGTH(array_list) - 1 DO
    #             IF CALL array_list[index].get_amount() == target THEN
    #                 RETURN index // Target found
    #             ENDIF
    #         ENDFOR
    #         RETURN -1 // Target not found safely matches the menu logic
    elif attribute == "amount":

        for index in range(len(array_list)):
            if array_list[index].get_amount() == target:
                return index
        return -1

    # ELSE
    #         PRINT "Error Occurred During Searching"
    #         RETURN -1
    #     ENDIF
    # ENDFUNCTION
    else:
        print("Error Occurred During Searching")
        return -1

# Helper function to print transaction records clearly
def display_all_transactions(transactions):
    print(f"\n{'Index':<6} | {'ID':<6} | {'Customer':<12} | {'Product':<12} | {'Amount':<10} | {'Date':<10}")
    print("-" * 65)
    # Loop using an integer range
    for index in range(len(transactions)):
        trans = transactions[index]
        print(f"{index:<6} | {trans.get_id():<6} | {trans.get_customer():<12} | {trans.get_product():<12} | ${trans.get_amount():<9.2f} | {trans.get_date():<10}")

# FUNCTION display_complexity_table(metrics)
#     PRINT "\n===================================== TIME COMPLEXITY ANALYSIS TABLE ======================================"
#     PRINT "Algorithm Operation       | Dataset Size   | Actual Execution Time   | Theoretical Complexity"
#     PRINT "-----------------------------------------------------------------------------------------------------------"
# Advanced Feature (d): Transformed into a dynamic execution tracking metrics board
def display_complexity_table(metrics):
    print(
        "\n===================================== TIME COMPLEXITY ANALYSIS TABLE ======================================")
    print(
        f"{'Algorithm Operation':<25} | {'Dataset Size':<14} | {'Actual Execution Time':<23} | {'Theoretical Complexity':<22}")
    print("-" * 107)

    # // Iterate through the historical benchmark tracking map
    #     FOR EACH algorithm_name, data IN metrics DO
    for algorithm_name, data in metrics.items():

        # // Format the execution time output column
        # IF data["time"] IS A FLOAT THEN
        #     SET execute_time = data["time"] formatted to 8 decimal places + " sec"
        # ELSE
        #     SET execute_time = data["time"]
        # ENDIF
        execute_time = f"{data['time']:.8f} sec" if isinstance(data['time'], float) else data['time']

        # // Format the dataset size output column
        #         IF data["size"] > 0 THEN
        #             SET size_string = CONVERT_TO_STRING(data["size"])
        #         ELSE
        #             SET size_string = "N/A"
        #         ENDIF
        size_string = str(data['size']) if data['size'] > 0 else "N/A"

        # // Print aligned metrics data record row
        #         PRINT algorithm_name + " | " + size_string + " | " + execute_time + " | " + data["theory"]
        #     ENDFOR
        #
        #     PRINT "==========================================================================================================="
        # ENDFUNCTION
        print(f"{algorithm_name:<25} | {size_string:<14} | {execute_time:<23} | {data['theory']:<22}")
    print("===========================================================================================================")

# FUNCTION check_transaction_id(array_list, target_id)
# Check if the input already inside the transaction list
def check_transaction_id(array_list, target_id):

    #     // Sequentially scan database records to look for existing ID collisions
    #     FOR EACH transaction IN array_list DO
    #         IF CALL transaction.get_id() == target_id THEN
    #             RETURN TRUE // Collision detected! ID already exists
    #         ENDIF
    #     ENDFOR
    for transaction in array_list:
        if transaction.get_id() == target_id:
            return True  # Found a duplicate

    #     RETURN FALSE // ID is entirely safe and unique to use
    # ENDFUNCTION
    return False  # The ID is unique and safe to use

def command_menu():
    global recursion_count

    # Initialize the default base dataset of 15 records
    dataset = [
        Transaction(112, "Alice", "Laptop", 1200.50, "2026-01-15"),
        Transaction(102, "Bob", "Smartphone", 800.00, "2026-02-20"),
        Transaction(115, "Charlie", "Headphones", 150.00, "2026-03-05"),
        Transaction(101, "David", "Keyboard", 75.25, "2026-01-10"),
        Transaction(109, "Eve", "Monitor", 300.99, "2026-04-12"),
        Transaction(106, "Frank", "Mouse", 25.00, "2026-02-14"),
        Transaction(114, "Grace", "Desk Chair", 189.99, "2026-05-22"),
        Transaction(103, "Heidi", "USB Drive", 15.50, "2026-01-18"),
        Transaction(110, "Ivan", "External HD", 110.00, "2026-03-30"),
        Transaction(105, "Judy", "Webcam", 65.00, "2026-02-28"),
        Transaction(113, "Mallory", "Microphone", 125.40, "2026-04-01"),
        Transaction(107, "Niah", "Router", 89.95, "2026-05-02"),
        Transaction(104, "Oscar", "Tablet", 450.00, "2026-03-11"),
        Transaction(111, "Peggy", "Printer", 175.00, "2026-04-19"),
        Transaction(108, "Sybil", "Smart Watch", 210.00, "2026-02-10")
    ]

    is_sorted = "None"  # Track state flag safely for Binary Search

    # Local performance history database
    performance_metrics = {
        "Merge Sort (by ID)": {"size": 0, "time": "No Run Record Yet", "theory": "O(N log N)"},
        "Merge Sort (by Amount)": {"size": 0, "time": "No Run Record Yet", "theory": "O(N log N)"},
        "Binary Search": {"size": 0, "time": "No Run Record Yet", "theory": "O(log N)"},
        "Linear Search": {"size": 0, "time": "No Run Record Yet", "theory": "O(N)"}
    }
    
    # Display Interactive Menu Options
    # PRINT "\n++++++++ TRANSACTION MANAGEMENT SYSTEM ++++++++"
    # PRINT "1. Display All Transaction"
    # PRINT "2. Insert New Transaction"
    # PRINT "3. Sort Transaction (Merge Sort)"
    # PRINT "4. Search Transaction (BINARY SEARCH)"
    # PRINT "5. Search Transaction (LINEAR SEARCH)"
    # PRINT "6. Show Time Complexity Benchmark Reference Table"
    # PRINT "6. Exit System"
    # PRINT "++++++++++++++++++++++++++++++++++++++++++++"

    # Command Transaction List System
    print("\n=================== TRANSACTION MANAGEMENT SYSTEM ===================")
    print("1. Display All Transaction")
    print("2. Insert New Transaction")
    print("3. Sort Transaction (Merge Sort)")
    print("4. Search Transaction (BINARY SEARCH)")
    print("5. Search Transaction (LINEAR SEARCH)")
    print("6. Show Time Complexity Benchmark Reference Table")
    print("7. Exit System")
    print("==================================================================\n")

    # INPUT choice
    # Trim whitespace from choice
    choice = input("Select an option (1-7): ").strip()

    #WHILE TRUE DO
    while choice != "7":
        # Display Interactive Menu Options
        # PRINT "\n++++++++ TRANSACTION MANAGEMENT SYSTEM ++++++++"
        # PRINT "1. Display All Transaction"
        # PRINT "2. Insert New Transaction"
        # PRINT "3. Sort Transaction (Merge Sort)"
        # PRINT "4. Search Transaction (BINARY SEARCH)"
        # PRINT "5. Search Transaction (LINEAR SEARCH)"
        # PRINT "6. Show Time Complexity Benchmark Reference Table"
        # PRINT "6. Exit System"
        # PRINT "++++++++++++++++++++++++++++++++++++++++++++"

        # Command Transaction List System
        print("\n=================== TRANSACTION MANAGEMENT SYSTEM ===================")
        print("1. Display All Transaction")
        print("2. Insert New Transaction")
        print("3. Sort Transaction (Merge Sort)")
        print("4. Search Transaction (BINARY SEARCH)")
        print("5. Search Transaction (LINEAR SEARCH)")
        print("6. Show Time Complexity Benchmark Reference Table")
        print("7. Exit System")
        print("==================================================================\n")

        # INPUT choice
        # Trim whitespace from choice
        choice = input("Select an option (1-7): ").strip()

        # Evaluate user choice from the interactive terminal interface
        # IF choice == "1" THEN
        #     OUTPUT "\n--- Current Dataset Storage ---"
        #     CALL display_all_transactions(dataset)
        if choice == "1":
            print("\n--- Current Dataset Storage ---")
            display_all_transactions(dataset)

        # ELSE IF choice == "2" THEN
        #     OUTPUT "\n--- Add New Transaction Record ---"
        #     TRY
        #         INPUT new_transaction_id (As Integer)
        #
        #         // Validate uniqueness of Transaction ID
        #         IF CALL check_transaction_id(dataset, new_transaction_id) == TRUE THEN
        #             OUTPUT "Input Error: A transaction with this ID already exists."
        #             CONTINUE LOOP // Skip to next menu loop iteration
        #         ENDIF
        elif choice == "2":
            print("\n--- Add New Transaction Record ---")
            try:
                new_transaction_id = int(input("Enter Transaction ID (Integer): "))

                if check_transaction_id(dataset, new_transaction_id):
                    print("Input Error: A transaction with this ID already exists.")
                    continue

                # INPUT customer
                # INPUT product
                # INPUT amount (As Float)
                # INPUT date
                customer = input("Enter Customer Name: ").strip()
                product = input("Enter Product Name: ").strip()
                amount = float(input("Enter Amount ($): "))
                date = input("Enter Date (YYYY-MM-DD): ").strip()

                # Validate text fields are clean
                #     IF customer == "" OR product == "" OR date == "" THEN
                #         OUTPUT "Input Error: Text fields cannot be left blank."
                #         CONTINUE LOOP
                #     ENDIF
                #
                #     // Instantiate transaction and append to dataset dynamically
                #     SET new_transaction = NEW Transaction(new_transaction_id, customer, product, amount, date)
                #     APPEND new_transaction TO dataset
                #     SET is_sorted = "None" // Flag reset as new data breaks sequence sorted state
                #
                #     OUTPUT "Success: Record " + new_transaction_id + " appended dynamically."
                if customer == "" or product == "" or date == "":
                    print("Input Error: Text fields cannot be left blank.")
                    continue

                new_transaction = Transaction(new_transaction_id, customer, product, amount, date)
                dataset.append(new_transaction)
                is_sorted = "None"

                print(f"Success: Record {new_transaction_id} appended dynamically.")

            # CATCH ValueError
            #     OUTPUT "System Input Error: ID and Amount must be correct numeric values"
            # ENDTRY
            except ValueError:
                print("System Input Error: ID and Amount must be correct numeric values")

        # ELSE IF choice == "3" THEN
        #     OUTPUT "\n--- Sort Dataset via Merge Sort ---"
        #     OUTPUT "Select Sorting Key Attribute:\nA. Sort by Transaction ID\nB. Sort by Transaction Amount"
        #     INPUT sub_choice
        #     SET sub_choice = uppercase(trim(sub_choice))
        elif choice == "3":
            print("\n--- Sort Dataset via Merge Sort ---")
            print("Select Sorting Key Attribute:")
            print("A. Sort by Transaction ID")
            print("B. Sort by Transaction Amount")
            sub_choice = input("Choice (A/B): ").strip().upper()

            # IF sub_choice == "A" THEN
            #         SET recursion_count = 0
            #         SET start_time = CALL time.perf_counter()
            #         SET dataset = CALL merge_sort(dataset, attribute="id")
            #         SET end_time = CALL time.perf_counter()
            #         SET is_sorted = "ID"
            #
            #         // Update benchmark analytics tracking storage metrics dynamically
            #         SET performance_metrics["Merge Sort (by ID)"]["time"] = end_time - start_time
            #         SET performance_metrics["Merge Sort (by ID)"]["size"] = LENGTH(dataset)
            #
            #         OUTPUT "\nSuccess: Dataset ordered by ID."
            #         OUTPUT "-> Total Recursive Calls Made: " + recursion_count
            #         OUTPUT "-> Performance Speed: " + (end_time - start_time) + " seconds."
            if sub_choice == "A":

                recursion_count = 0
                start_time = time.perf_counter()
                dataset = merge_sort(dataset, attribute="id")
                end_time = time.perf_counter()
                is_sorted = "ID"

                # Update tracking metrics dynamically
                performance_metrics["Merge Sort (by ID)"]["time"] = end_time - start_time
                performance_metrics["Merge Sort (by ID)"]["size"] = len(dataset)
                
                print(f"\nSuccess: Dataset ordered by ID.")
                print(f"-> Total Recursive Calls Made: {recursion_count}")
                print(f"-> Performance Speed: {(end_time - start_time):.8f} seconds.")

            # ELSE IF sub_choice == "B" THEN
            #         SET recursion_count = 0
            #         SET start_time = CALL time.perf_counter()
            #         SET dataset = CALL merge_sort(dataset, attribute="amount")
            #         SET end_time = CALL time.perf_counter()
            #         SET is_sorted = "Amount"
            #
            #         // Update benchmark analytics tracking storage metrics dynamically
            #         SET performance_metrics["Merge Sort (by Amount)"]["time"] = end_time - start_time
            #         SET performance_metrics["Merge Sort (by Amount)"]["size"] = LENGTH(dataset)
            #
            #         OUTPUT "\nSuccess: Dataset ordered by Amount."
            #         OUTPUT "-> Total Recursive Calls Made: " + recursion_count
            #         OUTPUT "-> Performance Speed: " + (end_time - start_time) + " seconds."
            elif sub_choice == "B":

                recursion_count = 0
                start_time = time.perf_counter()
                dataset = merge_sort(dataset, attribute="amount")
                end_time = time.perf_counter()
                is_sorted = "Amount"

                # Update tracking metrics dynamically
                performance_metrics["Merge Sort (by Amount)"]["time"] = end_time - start_time
                performance_metrics["Merge Sort (by Amount)"]["size"] = len(dataset)

                print(f"\nSuccess: Dataset ordered by Amount.")
                print(f"-> Total Recursive Calls Made: {recursion_count}")
                print(f"-> Performance Speed: {(end_time - start_time):.8f} seconds.")

            # ELSE
            #         OUTPUT "Invalid selection. Returning to main menu."
            #     ENDIF
            else:
                print("Invalid selection. Returning to main menu.")

        # ELSE IF choice == "4" THEN
        #     OUTPUT "\n--- Binary Search Engine ---"
        #
        #     // Prevent execution if dataset has not been explicitly pre-sorted
        #     IF is_sorted == "None" THEN
        #         OUTPUT "Warning: Binary Search requires the dataset to be sorted by ID first!"
        #         OUTPUT "Please run Option 3 (Sort by ID) before using this feature."
        #         CONTINUE LOOP
        #     ELSE
        elif choice == "4":
            print("\n--- Binary Search Engine ---")
            if is_sorted == "None":
                print("Warning: Binary Search requires the dataset to be sorted by ID first!")
                print("Please run Option 3 (Sort by ID) before using this feature.")
                continue

            else:

                # TRY
                #             OUTPUT "\n--- Search Dataset via Binary Search ---"
                #             OUTPUT "Select Sorting Key Attribute:\nA. Search by Transaction ID\nB. Search by Transaction Amount"
                #             INPUT sub_choice
                #             SET sub_choice = uppercase(trim(sub_choice))
                #
                #             SET result_index = -1  // Default structural fallback safely
                #             SET start_time = 0
                #             SET end_time = 0
                try:

                    print("\n--- Search Dataset via Binary Search ---")
                    print("Select Sorting Key Attribute:")
                    print("A. Search by Transaction ID")
                    print("B. Search by Transaction Amount")
                    sub_choice = input("Choice (A/B): ").strip().upper()

                    result_index = -1  # Default fallback flags to clear crash risks
                    start_time = 0
                    end_time = 0

                    # IF sub_choice == "A" AND is_sorted == "ID" THEN
                    #                 INPUT target (As Integer)
                    #                 SET start_time = CALL time.perf_counter()
                    #                 SET result_index = CALL binary_search(dataset, 0, LENGTH(dataset) - 1, target, attribute="id")
                    #                 SET end_time = CALL time.perf_counter()
                    if sub_choice == "A" and is_sorted == "ID":

                        target = int(input("Enter Transaction ID to find: "))
                        start_time = time.perf_counter()
                        result_index = binary_search(dataset, 0, len(dataset) - 1, target, attribute = "id")
                        end_time = time.perf_counter()

                    # ELSE IF sub_choice == "B" AND is_sorted == "Amount" THEN
                    #                 INPUT target (As Float)
                    #                 SET start_time = CALL time.perf_counter()
                    #                 SET result_index = CALL binary_search(dataset, 0, LENGTH(dataset) - 1, target, attribute="amount")
                    #                 SET end_time = CALL time.perf_counter()
                    elif sub_choice == "B" and is_sorted == "Amount":

                        target = float(input("Enter Transaction Amount to find: "))
                        start_time = time.perf_counter()
                        result_index = binary_search(dataset, 0, len(dataset) - 1, target, attribute = "amount")
                        end_time = time.perf_counter()

                    # ELSE
                    #                 OUTPUT "Invalid selection, Or Sorted Value Invalid. Returning to main menu."
                    #                 CONTINUE LOOP
                    #             ENDIF
                    #
                    #             // Update empirical run performance logs if data execution was successful
                    #             SET performance_metrics["Binary Search"]["time"] = end_time - start_time
                    #             SET performance_metrics["Binary Search"]["size"] = LENGTH(dataset)
                    #
                    #             // Print matching lookup results
                    #             IF result_index != -1 THEN
                    #                 SET match = dataset[result_index]
                    #                 OUTPUT "\nFound at Sorted Index [" + result_index + "]!"
                    #                 OUTPUT "Details: " + CALL match.get_customer() + " | " + CALL match.get_product() + " | $" + CALL match.get_amount()
                    #             ELSE
                    #                 OUTPUT "\nAlert: ID " + target + " is not present in the system."
                    #             ENDIF
                    #             OUTPUT "-> Search execution completed in " + (end_time - start_time) + " seconds."
                    #
                    #         CATCH ValueError
                    #             OUTPUT "Input Error: Target ID must be a numeric integer."
                    #         ENDTRY
                    #     ENDIF
                    else:
                        print("Invalid selection, Or Sorted Value Invalid. Returning to main menu.")
                        continue

                    # Log performance if valid run took place
                    performance_metrics["Binary Search"]["time"] = end_time - start_time
                    performance_metrics["Binary Search"]["size"] = len(dataset)

                    if result_index != -1:
                        match = dataset[result_index]
                        print(f"\nFound at Sorted Index [{result_index}]!")
                        print(f"Details: {match.get_customer()} | {match.get_product()} | ${match.get_amount()}")
                    else:
                        print(f"\nAlert: ID {target} is not present in the system.")
                    print(f"-> Search execution completed in {(end_time - start_time):.8f} seconds.")
                except ValueError:
                    print("Input Error: Target ID must be a numeric integer.")

        # ELSE IF choice == "5" THEN
        #     OUTPUT "\n--- Linear Search Engine ---"
        #     TRY
        #         OUTPUT "\n--- Search Dataset via Linear Search ---"
        #         OUTPUT "Select Sorting Key Attribute:\nA. Search by Transaction ID\nB. Search by Transaction Amount"
        #         INPUT sub_choice
        #         SET sub_choice = uppercase(trim(sub_choice))
        #
        #         SET result_index = -1
        #         SET start_time = 0
        #         SET end_time = 0
        elif choice == "5":
            print("\n--- Linear Search Engine ---")
            try:

                print("\n--- Search Dataset via Linear Search ---")
                print("Select Sorting Key Attribute:")
                print("A. Search by Transaction ID")
                print("B. Search by Transaction Amount")
                sub_choice = input("Choice (A/B): ").strip().upper()

                result_index = -1  # Default fallback flags to clear crash risks
                start_time = 0
                end_time = 0

                # IF sub_choice == "A" THEN
                #             INPUT target (As Integer)
                #             SET start_time = CALL time.perf_counter()
                #             SET result_index = CALL linear_search(dataset, target, attribute="id")
                #             SET end_time = CALL time.perf_counter()
                if sub_choice == "A":
                    target = int(input("Enter Transaction ID to find: "))
                    start_time = time.perf_counter()
                    result_index = linear_search(dataset, target, attribute="id")
                    end_time = time.perf_counter()

                # ELSE IF sub_choice == "B" THEN
                #             INPUT target (As Float)
                #             SET start_time = CALL time.perf_counter()
                #             SET result_index = CALL linear_search(dataset, target, attribute="amount")
                #             SET end_time = CALL time.perf_counter()
                elif sub_choice == "B":
                    target = float(input("Enter Transaction Amount to find: "))
                    start_time = time.perf_counter()
                    result_index = linear_search(dataset, target, attribute="amount")
                    end_time = time.perf_counter()

                # ELSE
                #             OUTPUT "Invalid selection. Returning to main menu."
                #             CONTINUE LOOP
                #         ENDIF
                else:
                    print("Invalid selection. Returning to main menu.")
                    continue

                # // Record metrics to analysis layout history
                #         SET performance_metrics["Linear Search"]["time"] = end_time - start_time
                #         SET performance_metrics["Linear Search"]["size"] = LENGTH(dataset)
                #
                #         IF result_index != -1 THEN
                #             SET match = dataset[result_index]
                #             OUTPUT "\nFound at Current Index [" + result_index + "]!"
                #             OUTPUT "Details: " + CALL match.get_customer() + " | " + CALL match.get_product() + " | $" + CALL match.get_amount()
                #         ELSE
                #             OUTPUT "\nAlert: ID " + target + " is not present in the system."
                #         ENDIF
                #         OUTPUT "-> Search execution completed in " + (end_time - start_time) + " seconds."
                #
                #     CATCH ValueError
                #         OUTPUT "Input Error: Target ID must be a numeric integer."
                #     ENDTRY

                # Log performance data
                performance_metrics["Linear Search"]["time"] = end_time - start_time
                performance_metrics["Linear Search"]["size"] = len(dataset)

                if result_index != -1:
                    match = dataset[result_index]
                    print(f"\nFound at Current Index [{result_index}]!")
                    print(f"Details: {match.get_customer()} | {match.get_product()} | ${match.get_amount()}")
                else:

                    print(f"\nAlert: ID {target} is not present in the system.")
                print(f"-> Search execution completed in {(end_time - start_time):.8f} seconds.")

            except ValueError:
                print("Input Error: Target ID must be a numeric integer.")

        # ELSE IF choice == "6" THEN
        #     CALL display_complexity_table(performance_metrics)
        elif choice == "6":
            display_complexity_table(performance_metrics)

        # ELSE IF choice == "7" THEN
        #     OUTPUT "Exiting System"
        #     BREAK LOOP
        #
        # ENDIF
        elif choice == "7":
            print("Exiting System")
            break

    #     ELSE
    #     PRINT "Selection Error: Invalid choice! Please type a number between 1 and 7."
    #     ENDIF
    #
    # ENDWHILE
        else:
            print("Please enter option between (1 to 7)")

def main():

    command_menu()

if __name__ == "__main__":
    main()