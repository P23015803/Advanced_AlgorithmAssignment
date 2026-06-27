import time # For Q4
# CLASS Medicine:
#     PROPERTIES:
#         med_id      // Integer (acts as the Hash Key)
#         name        // String
#         item_type   // String (e.g., "Tablets", "Syrup")
#         price       // Decimal
#         stock       // Integer
#
#     CONSTRUCTOR(id, name, type, price, stock):
#         self.med_id = id
#         self.name = name
#         self.item_type = type
#         self.price = price
#         self.stock = stock
#
#     //GETTER
#
#     //SETTER

class Medicine:
    def __init__(self, med_id, med_name, item_type, price, med_stock):
        self.med_id = med_id
        self.med_name = med_name
        self.item_type = item_type
        self.price = price
        self.med_stock = med_stock

    def get_id(self):
        return self.med_id

    def get_name(self):
        return self.med_name

    def get_type(self):
        return self.item_type

    def get_price(self):
        return self.price

    def get_stock(self):
        return self.med_stock

    def set_id(self, med_id):
        self.med_id = med_id

    def set_name(self, med_name):
        self.med_name = med_name

    def set_type(self, item_type):
        self.item_type = item_type

    def set_price(self, price):
        self.price = price

    def set_stock(self, med_stock):
        self.med_stock = med_stock

# Fixed capacity chosen for the pharmacy store
# CONSTANT SIZE = 8
# Create an array 'hashTable' of SIZE
# Fill every slot in 'hashTable' with NULL

size = 8
hash_table = [None] * size

"""Added for Q4"""
one_dimensional_array = []

# 2. Hash Function
# Function hash(med_id):
#     RETURN med_id MODULO SIZE
def hash_function(med_id):
    return med_id % size

# 3. Insert Function
# Function insert(key):
# index = hash(key)
# original_index = index
def insert_medicine(medicine_object):
    key = medicine_object.get_id()
    index = hash_function(key)
    original_index = index

# WHILE hashTable[index] is NOT NULL AND hashTable[index] is NOT "DELETED":
# If the key is already there, we can update or ignore it
# IF hashTable[index] == key:
# return "Key already exists"
    while hash_table[index] is not None and hash_table[index] != 'DELETED':
        if hash_table[index].med_id == key:
            print("Error: Medicine ID already exists")
            return

# Move to the next slot and wrap around if at the end
# index = (index + 1) MODULO SIZE
        index = (index + 1) % size

# If we loop all the way back, the table is full
# IF index == original_index:
# return "Error: Hash Table is full"
        if index == original_index:
            print(f"Pharmacy Storage is Full, {key} can't be added")
            return

# Empty spot found!
# hashTable[index] = key
# return "Inserted successfully"
    hash_table[index] = medicine_object
    print(f"Medicine Successfully Inserted: {medicine_object.get_id()}")

# 4. Search Function
# Function search(key):
# index = hash(key)
# original_index = index
def search_medicine(target_id):
    index = hash_function(target_id)
    original_index = index

# WHILE hashTable[index] is NOT NULL:
# IF hashTable[index] == key:
# return "Found key at index " + index
    while hash_table[index] is not None:
        if hash_table[index] != 'DELETED':
            if hash_table[index].med_id == target_id:
                print(f"\n[Found Match at Slot {index}]")
                print(f"   Name : {hash_table[index].med_name}")
                print(f"   Type : {hash_table[index].item_type}")
                print(f"   Price: RM{hash_table[index].price:.2f}")
                print(f"   Stock: {hash_table[index].med_stock}")
                return

# index = (index + 1) MODULO SIZE
        index = (index + 1) % size

# IF index == original_index:
        if index == original_index:
            print(f"Medicine {target_id} is not found in pharmacy")
            return

# 5. Delete Function
# Function delete(key):
# index = hash(key)
# original_index = index
def delete_medicine(target_id):
    index = hash_function(target_id)
    original_index = index

# WHILE hashTable[index] is NOT NULL:
# IF hashTable[index] == key:
# return hashTable[index] in NULL
    while hash_table[index] is not None:

        if hash_table[index] != 'DELETED':
            if hash_table[index].med_id == target_id:
                print(f" Removing {hash_table[index].med_id}: {hash_table[index].med_name} from {index}")
                hash_table[index] = 'DELETED'
                print("Medicine Successfully Deleted")
                return

# index = (index + 1) MODULO SIZE
        index = (index + 1) % size

# IF index == original_index:
        if index == original_index:
            print(f"Medicine {target_id} is not found in pharmacy, can't be delete")
            return

# Print Pharmacy List
def medicine_list():
    print("\n=================== PHARMACY INVENTORY STORAGE ===================")
    for i in range(size):
        if hash_table[i] is None:
            print(f"Slot {i}: [Empty]")
        elif hash_table[i] == "DELETED":
            print(f"Slot {i}: [DELETED]")
        else:
            print(f"Slot {i}: [ID: {hash_table[i].med_id}] {hash_table[i].med_name:<20} | Type: {hash_table[i].item_type:<18} | Price: RM{hash_table[i].price:<10.2f} | Stock: {hash_table[i].med_stock}")
    print("==================================================================\n")

"""Q4 Performance Test Function"""
# FUNCTION performance_test_hash_search(target_id)
#     // Compute the initial hash index
#     index <- CALL hash_function(target_id)
#     original_index <- index
def performance_test_hash_search(target_id):
    index = hash_function(target_id)
    original_index = index

    # WHILE hashTable[index] is NOT NULL:
    # IF hashTable[index] == key:
    # return "Found key at index " + index
    while hash_table[index] is not None:
        if hash_table[index] != 'DELETED':
            if hash_table[index].med_id == target_id:
                return hash_table[index]

        # index = (index + 1) MODULO SIZE
        index = (index + 1) % size

        # IF index == original_index:
        if index == original_index:
            return None
    return None

# FUNCTION performance_test_array_search(target_id)
#     // Perform sequential linear search through the 1D array
#     FOR EACH medicine IN one_dimensional_array DO
#         IF medicine IS NOT NULL AND medicine.med_id == target_id THEN
#             RETURN medicine // Found object match
#         ENDIF
#     ENDFOR
#
#     RETURN NULL // Target not found
# ENDFUNCTION
def performance_test_array_search(target_id):
    for medicine in one_dimensional_array:
        if medicine is not None and medicine.med_id == target_id:
            return medicine
    return None

# FUNCTION run_performance_test()
#     iterations <- 10000
#
#     PRINT "\n========= Q4 PERFORMANCE TESTING ENGINE ========="
#     PRINT "Running search operations " + iterations + " times in a background loop..."
#
#     existing_id <- 205      // Test Case 1: Existing key
#     non_existing_id <- 999  // Test Case 2: Non-existing key
def run_performance_test():
    iterations = 10000

    print("\n========= Q4 PERFORMANCE TESTING ENGINE =========")
    print(f"Running search operations {iterations:,} times in a background loop...")

    existing_id = 205  # Test Case 1: Existing key
    non_existing_id = 999  # Test Case 2: Non-existing key

    # Benchmark 1: Existing Key Search
    # start <- CALL get_perf_counter()
    # FOR i <- 0 TO iterations - 1 DO
    #     CALL performance_test_hash_search(existing_id)
    # ENDFOR
    # hash_exist_time <- CALL get_perf_counter() - start
    start = time.perf_counter()
    for i in range(iterations):
        performance_test_hash_search(existing_id)
    hash_exist_time = time.perf_counter() - start

    # start <- CALL get_perf_counter()
    # FOR i <- 0 TO iterations - 1 DO
    #     CALL performance_test_array_search(existing_id)
    # ENDFOR
    # array_exist_time <- CALL get_perf_counter() - start
    start = time.perf_counter()
    for i in range(iterations):
        performance_test_array_search(existing_id)
    array_exist_time = time.perf_counter() - start

    # Benchmark 2: Non-Existing Key Search (Worst Case)
    # start <- CALL get_perf_counter()
    # FOR i <- 0 TO iterations - 1 DO
    #     CALL performance_test_hash_search(non_existing_id)
    # ENDFOR
    # hash_non_exist_time <- CALL get_perf_counter() - start
    start = time.perf_counter()
    for i in range(iterations):
        performance_test_hash_search(non_existing_id)
    hash_non_exist_time = time.perf_counter() - start

    # start <- CALL get_perf_counter()
    # FOR i <- 0 TO iterations - 1 DO
    #     CALL performance_test_array_search(non_existing_id)
    # ENDFOR
    # array_non_exist_time <- CALL get_perf_counter() - start
    start = time.perf_counter()
    for i in range(iterations):
        performance_test_array_search(non_existing_id)
    array_non_exist_time = time.perf_counter() - start

    # Display Results Table
#     ------------------------------------------------------------
#     Display Results Summary Table
#     ------------------------------------------------------------
#     PRINT "\n[RESULTS] Execution Times (Seconds):"
#     PRINT "------------------------------------------------------------"
#     PRINT "Search Scenario | Hash Table (Probing) | 1D Array (Linear Search)"
#     PRINT "------------------------------------------------------------"
#     PRINT "Existing ID     | " + hash_exist_time + " | " + array_exist_time
#     PRINT "Non-Existing ID | " + hash_non_exist_time + " | " + array_non_exist_time
#     PRINT "------------------------------------------------------------"
    print("\n[RESULTS] Execution Times (Seconds):")
    print("-" * 60)
    print(f"Search Scenario | Hash Table (Probing) | 1D Array (Linear Search)")
    print("-" * 60)
    print(f"Existing ID     | {hash_exist_time:<20.5f} | {array_exist_time:.5f}")
    print(f"Non-Existing ID | {hash_non_exist_time:<20.5f} | {array_non_exist_time:.5f}")
    print("-" * 60)

#     // Guard against potential division by zero using a small epsilon fallback
#     speed_factor <- array_non_exist_time / MAX(hash_non_exist_time, 0.000000001)
#     PRINT "Analysis: For missing keys, Hash Table lookup is ~" + speed_factor + "x speed difference.\n"
# ENDFUNCTION
    speed_factor = array_non_exist_time / max(hash_non_exist_time, 1e-9)
    print(f"Analysis: For missing keys, Hash Table lookup is ~{speed_factor:.1f}x speed difference.\n")

def command_menu():
    # Display Interactive Menu Options
    # PRINT "\n++++++++ PHARMACY INVENTORY SYSTEM ++++++++"
    # PRINT "1. Display Inventory Storage"
    # PRINT "2. Insert New Medicine"
    # PRINT "3. Search Medicine by ID"
    # PRINT "4. Delete Medicine by ID"
    # PRINT "5. Performance Benchmark"
    # PRINT "6. Exit System"
    # PRINT "++++++++++++++++++++++++++++++++++++++++++++"

    # Command Pharmacy List System
    print("\n=================== PHARMACY INVENTORY STORAGE ===================")
    print("1. Display Inventory Storage")
    print("2. Insert New Medicine")
    print("3. Search Medicine by ID")
    print("4. Delete Medicine by ID")
    print("5. Performance Benchmark")
    print("6. Exit System")
    print("==================================================================\n")

    # INPUT choice
    # Trim whitespace from choice
    choice = input("Select an option (1-6): ").strip()

    #WHILE TRUE DO
    while choice != "6":
        # Display Interactive Menu Options
        # PRINT "\n++++++++ PHARMACY INVENTORY SYSTEM ++++++++"
        # PRINT "1. Display Inventory Storage"
        # PRINT "2. Insert New Medicine"
        # PRINT "3. Search Medicine by ID"
        # PRINT "4. Delete Medicine by ID"
        # PRINT "5. Performance Benchmark"
        # PRINT "6. Exit System"
        # PRINT "++++++++++++++++++++++++++++++++++++++++++++"

        #Command Pharmacy List System
        print("\n=================== PHARMACY INVENTORY STORAGE ===================")
        print("1. Display Inventory Storage")
        print("2. Insert New Medicine")
        print("3. Search Medicine by ID")
        print("4. Delete Medicine by ID")
        print("5. Performance Benchmark")
        print("6. Exit System")
        print("==================================================================\n")

        # INPUT choice
        # Trim whitespace from choice
        choice = input("Select an option (1-6): ").strip()

        # Evaluate user choice
        # IF choice == "1" THEN
        #     CALL medicine_list()
        if choice == "1":
            medicine_list()

        # ELSE IF choice == "2" THEN
        # PRINT "\n--- Add New Medicine Details ---"
        # TRY
        #     INPUT med_id
        #     INPUT med_name
        #     INPUT item_type
        #     INPUT price
        #     INPUT med_stock
        elif choice == "2":
            print("\n--- Add New Medicine Detail ---")
            try:
                med_id = int(input("Enter Medicine ID (Integer Number):"))
                med_name = input("Enter Medicine Name:").strip()
                item_type = input("Enter Item Type: ").strip()
                price = float(input("Enter Unit Price (RM): "))
                med_stock = int(input("Enter Current Stock: "))

                # Validation check for empty strings
                # IF med_name is empty OR item_type is empty THEN
                #     PRINT "Error: Name and Item Type cannot be blank."
                #     CONTINUE // Skip back to the start of the menu loop
                # ENDIF
                # Check for clean inputs
                if med_name == "" or item_type == "":
                    print("Error: Name and Item Type cannot be blank.")
                    continue

                # Instantiate object and pass it to your Q2 algorithm
                # new_item = NEW Medicine(med_id, med_name, item_type, price, med_stock)
                # CALL insert_medicine(new_item)
                # Add the user entered new item into the pharmacy storage
                new_item = Medicine(med_id, med_name, item_type, price, med_stock)
                insert_medicine(new_item)

            # CATCH ValueError
            #     PRINT "System Input Error: ID, Price, and Stock must be valid numerical values."
            # ENDTRY
            except ValueError:
                print("System Input Error: ID, Price, and Stock must be valid numerical values.")

        # ELSE IF choice == "3" THEN
        # PRINT "\n--- Search Inventory ---"
        # TRY
        #     INPUT target_id
        #     CALL search_medicine(target_id)
        # CATCH ValueError
        #     PRINT "System Input Error: ID must be an integer."
        # ENDTRY
        elif choice == "3":
            print("\n--- Search Inventory ---")
            try:
                target_id = int(input("Find Medicine ID: "))
                search_medicine(target_id)
            except ValueError:
                print("System Input Error: ID must be an integer.")

        # ELSE IF choice == "4" THEN
        # PRINT "\n--- Remove Product ---"
        # TRY
        #     INPUT target_id
        #     CALL delete_medicine(target_id)
        # CATCH ValueError
        #     PRINT "System Input Error: ID must be an integer."
        # ENDTRY
        elif choice == "4":
            print("\n--- Delete Medicine ---")
            try:
                target_id = int(input("Enter Medicine ID to Delete: "))
                delete_medicine(target_id)
            except ValueError:
                print("System Input Error: ID must be an integer.")

        # ELSE IF choice == "5" THEN
        # CALL run_performance_test()
        elif choice == "5":
            run_performance_test()

        # ELSE IF choice == "6" THEN
        # PRINT "\nThank you for using the Local Pharmacy Inventory System. Goodbye!"
        # BREAK // Force exit the infinite loop
        elif choice == "6":
            print("Exiting System")
            break

    #     ELSE
    #     PRINT "Selection Error: Invalid choice! Please type a number between 1 and 6."
    #     ENDIF
    #
    # ENDWHILE
        else:
            print("Please enter option between (1 to 6)")

def main():
    # Create sample records matching different types
    med1 = Medicine(102, "Panadol Actifast", "Tablets", 13.80, 60)
    med2 = Medicine(205, "Bisolvon Syrup", "Syrup", 24.50, 25)
    med3 = Medicine(303, "Vitamin C 1000mg", "Supplements", 42.00, 40)

    # Insert into hash table
    insert_medicine(med1)
    insert_medicine(med2)
    insert_medicine(med3)

    # Insert one dimensional array for testing
    one_dimensional_array.append(med1)
    one_dimensional_array.append(med2)
    one_dimensional_array.append(med3)

    #Command Pharmacy List System
    command_menu()

if __name__ == "__main__":
    main()