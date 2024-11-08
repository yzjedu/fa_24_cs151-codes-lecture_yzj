def read_file_to_list(filename):
    # Open the file for reading
    file_data = open(filename, 'r')

    # Read all lines from the file and store them as a list of strings
    values = file_data.readlines()

    # Close the file
    file_data.close()

    # Return the list of lines from the file
    return values


def main():
    # Read the contents of 'grades.txt' into the 'grades' list
    grades = read_file_to_list('grades.txt')

    # Print the number of elements in the 'grades' list
    print(len(grades))

    total = sum(grades)

    # Print the first 10 elements of the 'grades' list
    print(grades[:10])


# Call the main function to execute the code
main()