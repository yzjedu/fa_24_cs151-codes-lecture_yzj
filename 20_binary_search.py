def binary_search(my_list, target):

    start_index = 0
    end_index = len(my_list) - 1

    while end_index >= start_index:
        middle = (start_index + end_index) // 2

        if my_list[middle] == target:
            return middle  # Target found
        elif my_list[middle] > target:
            end_index = middle - 1  # Search in the left half
        else:
            start_index = middle + 1  # Search in the right half

    return -1  # Target not found


def main():
    # Sample unsorted list
    test_list = [15, 3, 9, 11, 1, 13, 7, 19, 5, 17]

    # Display the unsorted list to the user
    print("Unsorted list:", test_list)

    # Sort the list
    test_list.sort()
    print("Sorted list for binary search:", test_list)

    # Prompt the user for the target value
    target = int(input("Enter the number to search for: "))

    # Perform the binary search
    index = binary_search(test_list, target)

    # Output the result
    if index != -1:
        print(f"The number {target} was found at index {index}.")
    else:
        print(f"The number {target} was not found in the list.")


# Call the main function to run the program
main()