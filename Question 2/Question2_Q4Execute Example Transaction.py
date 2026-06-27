import time # For Q4
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


# 1. Merge Sort (DIVIDE and CONQUER)
# FUNCTION merge_sort(array_list)
#     // Base Case: If the list has 0 or 1 elements, it's already sorted
#     IF LENGTH(array_list) <= 1 THEN
#         RETURN array_list
#     ENDIF
def merge_sort(array_list):
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

    # Optional: Showing the recursive separation step
    print(f"[Recursive Split] Left IDs: {[t.get_id() for t in left_array]} | Right IDs: {[t.get_id() for t in right_array]}")

    # Step 2: CONQUER
    # Recursively solve the sub-problems by sorting both halves.
    # sorted_left = merge_sort(left_array)
    # sorted_right = merge_sort(right_array)
    sorted_left = merge_sort(left_array)
    sorted_right = merge_sort(right_array)

    # Step 3: MERGE
    #     RETURN merge(sorted_left, sorted_right)
    # ENDFUNCTION
    return merge(sorted_left, sorted_right)


# FUNCTION merge(left, right)
#     results = EMPTY LIST
#     i = 0
#     j = 0
def merge(left, right):
    # Initialize the merged list and compare key
    results = []
    i = 0
    j = 0

    # Compare elements from both sub-arrays and build the sorted list
    # WHILE i < LENGTH(left) AND j < LENGTH(right) DO
    #     IF left[i] <= right[j] THEN
    #         APPEND left[i] TO results
    #         i = i + 1
    #     ELSE
    #         APPEND right[j] TO results
    #         j = j + 1
    #     ENDIF
    # ENDWHILE
    while i < len(left) and j < len(right):
        if left[i].get_id() <= right[j].get_id():
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
def binary_search(array_list, low, high, target):
    # Check is the target value inside the list or not
    if low > high:
        print("The target wasn't inside the list")
        return -1 # Makes it failed safely

    # Step 1: DIVIDE
    # Split the array into two halves around the midpoint.
    # mid = (low + high) / 2  (Integer Division)
    mid = (low + high) // 2

    # Step 2: CONQUER
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
        return binary_search(array_list, low, mid - 1, target)

    # If the target is larger, recursively narrow the search to the right half
    # ELSE IF array_list[mid] < target THEN
    #     RETURN binary_search(array_list, mid + 1, high, target)
    elif array_list[mid].get_id() < target:
        return binary_search(array_list, mid + 1, high, target)

    # ELSE
    #         PRINT "Some error occurred when search"
    #         RETURN
    #     ENDIF
    # ENDFUNCTION
    else:
        print("Some error occurred when search")
        return -1 # Makes it failed safely


def main():
    # Make minimum 10 and maximum 30 transaction sample
    unsorted_array = [
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

    # Q4 Part A: Merge Sort Execution
    print("=== MERGE SORT OPERATIONS ===")
    # Print Original Array
    print("Original Unsorted Array (IDs):")
    print([t.get_id() for t in unsorted_array])
    print("\nTracing Recursive Calls:")

    # Sort the array
    start_sort = time.perf_counter()
    sorted_array = merge_sort(unsorted_array)
    end_sort = time.perf_counter()

    merge_sort_time = end_sort - start_sort

    # Show the sorted array
    print("\nSorted Array (IDs):")
    print([t.get_id() for t in sorted_array])
    print(f"--> Merge Sort Execution Time: {merge_sort_time:.8f} seconds\n")

    # Q4 Part B: Binary Search Cases
    print("=== BINARY SEARCH OPERATIONS ===")
    # Case 1: Searching for an existing transaction
    target_exist = 104
    print(f"\n[Case 1] Searching for EXISTING ID: {target_exist}")

    start_exist_search = time.perf_counter()
    index_exist = binary_search(sorted_array, 0, len(sorted_array) - 1, target_exist)
    end_exist_search = time.perf_counter()

    search_time_exist = end_exist_search - start_exist_search

    if index_exist != -1:
        match = sorted_array[index_exist]
        print(f"Success: Transaction found at sorted index {index_exist}!")
        print(f"Details: {match.get_customer()} bought a {match.get_product()} (${match.get_amount()})")
    else:
        print("Alert: Transaction ID not found.")
    print(f"--> Execution Time: {search_time_exist:.8f} seconds")

    # Case 2: Searching for a non-existing transaction
    target_missing = 999
    print(f"\n[Case 2] Searching for NON-EXISTING ID: {target_missing}")

    start_non_exist_search = time.perf_counter()
    index_missing = binary_search(sorted_array, 0, len(sorted_array) - 1, target_missing)
    end_non_exist_search = time.perf_counter()

    search_time_missing = end_non_exist_search - start_non_exist_search

    if index_missing != -1:
        print(f"Success: Transaction found at sorted index {index_missing}!")
    else:
        print(f"Alert: The target transaction ID {target_missing} wasn't inside the list.")
    print(f"--> Execution Time: {search_time_missing:.8f} seconds\n")

if __name__ == "__main__":
    main()