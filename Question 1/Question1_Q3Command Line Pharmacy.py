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

def command_menu():
    # Command Pharmacy List System
    print("\n=================== PHARMACY INVENTORY STORAGE ===================")
    print("1. Display Inventory Storage")
    print("2. Insert New Medicine")
    print("3. Search Medicine by ID")
    print("4. Delete Medicine by ID")
    print("5. Exit System")
    print("==================================================================\n")

    choice = int(input("Select an option (1-5): "))

    while choice != 5:
        #Command Pharmacy List System
        print("\n=================== PHARMACY INVENTORY STORAGE ===================")
        print("1. Display Inventory Storage")
        print("2. Insert New Medicine")
        print("3. Search Medicine by ID")
        print("4. Delete Medicine by ID")
        print("5. Exit System")
        print("==================================================================\n")

        choice = int(input("Select an option (1-5): "))

        if choice == 1:
            medicine_list()

        elif choice == 2:
            print("\n--- Add New Medicine Detail ---")
            try:
                med_id = int(input("Enter Medicine ID (Integer Number):"))
                med_name = input("Enter Medicine Name:").strip()
                item_type = input("Enter Item Type: ").strip()
                price = float(input("Enter Unit Price (RM): "))
                med_stock = int(input("Enter Current Stock: "))

                # Check for clean inputs
                if med_name == "" or item_type == "":
                    print("Error: Name and Item Type cannot be blank.")
                    continue

                # Add the user entered new item into the pharmacy storage
                new_item = Medicine(med_id, med_name, item_type, price, med_stock)
                insert_medicine(new_item)

            except ValueError:
                print("System Input Error: ID, Price, and Stock must be valid numerical values.")

        elif choice == 3:
            print("\n--- Search Inventory ---")
            try:
                target_id = int(input("Find Medicine ID: "))
                search_medicine(target_id)
            except ValueError:
                print("System Input Error: ID must be an integer.")

        elif choice == 4:
            print("\n--- Delete Medicine ---")
            try:
                target_id = int(input("Enter Medicine ID to Delete: "))
                delete_medicine(target_id)
            except ValueError:
                print("System Input Error: ID must be an integer.")

        elif choice == 5:
            print("Exiting System")
            break

def main():
    # Create sample records matching different types
    med1 = Medicine(102, "Panadol Actifast", "Tablets", 13.80, 60)
    med2 = Medicine(205, "Bisolvon Syrup", "Syrup", 24.50, 25)
    med3 = Medicine(303, "Vitamin C 1000mg", "Supplements", 42.00, 40)

    #Insert into hash table
    insert_medicine(med1)
    insert_medicine(med2)
    insert_medicine(med3)

    #Command Pharmacy List System
    command_menu()

if __name__ == "__main__":
    main()