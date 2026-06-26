# 1. Initialization
# Create an array 'hashTable' of a fixed 'SIZE'
# Fill every slot in 'hashTable' with NULL

size = 5
hash_table = [None] * size

# 2. Hash Function
# Function hash(key):
# return key MODULO SIZE
def hash_function(key):
    return key % size

# 3. Insert Function
# Function insert(key):
# index = hash(key)
# original_index = index
def insert(key):
    index = hash_function(key)
    original_index = index

# WHILE hashTable[index] is NOT NULL AND hashTable[index] is NOT "DELETED":
# If the key is already there, we can update or ignore it
# IF hashTable[index] == key:
# return "Key already exists"
    while hash_table[index] is not None and hash_table[index] != 'DELETED':
        if hash_table[index] == key:
            print("Key already exists")
            return

# Move to the next slot and wrap around if at the end
# index = (index + 1) MODULO SIZE
        index = (index + 1) % size

# If we loop all the way back, the table is full
# IF index == original_index:
# return "Error: Hash Table is full"
        if index == original_index:
            print(f"Hash Table is Full, {key} can't be added")
            return

# Empty spot found!
# hashTable[index] = key
# return "Inserted successfully"
    hash_table[index] = key
    print("Key Successfully Inserted")
    print(key)

# 4. Search Function
# Function search(key):
# index = hash(key)
# original_index = index
def search(key):
    index = hash_function(key)
    original_index = index

# WHILE hashTable[index] is NOT NULL:
# IF hashTable[index] == key:
# return "Found key at index " + index
    while hash_table[index] is not None:
        if hash_table[index] == key:
            print(f"Found key at index: {index}")
            return

# index = (index + 1) MODULO SIZE
        index = (index + 1) % size

# IF index == original_index:
        if index == original_index:
            print(f"Key {key} is not found in hash table")
            return

# 5. Delete Function
# Function delete(key):
# index = hash(key)
# original_index = index
def delete(key):
    index = hash_function(key)
    original_index = index

# WHILE hashTable[index] is NOT NULL:
# IF hashTable[index] == key:
# return hashTable[index] in NULL
    while hash_table[index] is not None:

        if hash_table[index] == key:
            hash_table[index] = 'DELETED'
            return

# index = (index + 1) MODULO SIZE
        index = (index + 1) % size

# IF index == original_index:
        if index == original_index:
            print(f"Key {key} is not found in hash table, cant be delete")
            return

def main():

    #Insert into hash table
    insert(1)
    insert(5)
    insert(7)
    insert(10)
    insert(15)

    #Test Repeating key
    print("\nRepeat the key")
    insert(10)

    #Test Full table
    print("\nAdding more to full hash table")
    insert(16)

    #Search Key
    print("\nSearch key")
    search(10)

    #Delete the key
    print("\nDelete Key")
    delete(10)

    print("\nAfter delete")
    print(hash_table)

    #Add key into the deleted key index
    print("\nAdd 20 to hash table")
    insert(20)


    print("\nAfter adding")
    print(hash_table)

if __name__ == "__main__":
    main()