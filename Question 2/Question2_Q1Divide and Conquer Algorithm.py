# 1. Merge Sort (DIVIDE and CONQUER)
from pygments.lexers import j


def merge_sort(array_list):

    if len(array_list) <= 1:
        return array_list

    # Step 1: DIVIDE
    # Split the array into two halves around the midpoint.
    mid = len(array_list) // 2
    left_array = array_list[:mid]
    right_array = array_list[mid:]

    #Step 2: CONQUER
    # Recursively solve the sub-problems by sorting both halves.
    sorted_left = merge_sort(left_array)
    sorted_right = merge_sort(right_array)

    #Step 3: MERGE
    return merge(sorted_left, sorted_right)

def merge(left, right):
    # Initialize the merged list and compare key
    results = []
    i = 0
    j = 0

    # Compare elements from both sub-arrays and build the sorted list
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            results.append(left[i])
            i += 1

        else:
            results.append(right[j])
            j += 1

    # Append any remaining elements left over from either array
    results.extend(left[i:])
    results.extend(right[j:])
    
    return results

# 2. Binary Search (DIVIDE and CONQUER)
def binary_search(array_list, low, high, target):
    # Check is the target value inside the list or not
    if low > high:
        print("The target wasn't inside the list")
        return

    # Step 1: DIVIDE
    # Split the array into two halves around the midpoint.
    mid = (low + high) // 2

    # Step 2: CONQUER
    if array_list[mid] == target:
        print(f"Target value located at index: {mid}")
        return mid

    # If the target is smaller, recursively narrow the search to the left half.
    elif array_list[mid] > target:
        return binary_search(array_list, low, mid - 1, target)

    # If the target is larger, recursively narrow the search to the right half
    elif array_list[mid] < target:
        return binary_search(array_list, mid + 1, high, target)

    else:
        print("Some error occurred when search")
        return

def main():
    # Make an unsorted array
    unsorted_array = [20, 30, 10, 2, 6, 35, 23, 40]

    #Print Original Array
    print("Original Unsorted Array: ")
    print(unsorted_array)

    # Sort the array
    sorted_array = merge_sort(unsorted_array)

    # Show the sorted array
    print("\nSorted Array: ")
    print(sorted_array)

    # Use binary search to search for target
    target = 2
    print(f"\nTarget Value: {target}")
    binary_search(sorted_array, 0, len(sorted_array) - 1, target)

if __name__ == "__main__":
    main()