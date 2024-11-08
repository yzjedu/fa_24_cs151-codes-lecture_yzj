import string
import random
# Problem 1
def read_file_to_list(filename):
    data = []
    try:
        # Open the file for reading
        file_data = open(filename, "r")

        # Read all lines from the file into a list
        data = file_data.readlines()

        # Close the file after reading
        file_data.close()

        # Return the list of data
        return data
    except:
        # Ensure the file is closed in case of an error
        file_data.close()

        # Print an error message and return an empty list
        print("Error reading file")
        return data

def main():
    # Read the contents of 'grades.txt' into the 'grades' list
    names = read_file_to_list('names.txt')

    # Print random names
    index = random.randint(0, len(names)-1)
    again = 'y'

    while again == 'y':
        print(names[index].strip())
        index = random.randint(0, len(names) - 1)
        again = input("Would you like to play again? (y/n) ").lower().strip()

    para = read_file_to_list('simple.txt')
    print(len(para))


# Call the main function to execute the code
main()