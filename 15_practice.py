import string

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

# Problem 3
def readfile(filename):
    words = []
    try:
        with open(filename, "r") as fd:  # Automatically handles file closing
            for line in fd:
                line = line.split()
                for word in line:
                    # Strip punctuation from the word
                    word = word.strip(string.punctuation)
                    if len(word) > 0:  # Check if the word is not empty
                        words.append(word)
        return words
    except FileNotFoundError:
        print("Error: File not found.")
        return words
    except IOError:
        print("Error: An error occurred while reading the file.")
        return words

def main():
    # Read the contents of 'grades.txt' into the 'grades' list
    grades = read_file_to_list('grades.txt')

    # Print the number of elements in the 'grades' list
    print(len(grades))

    # Print the first 10 elements of the 'grades' list
    print(grades[:10])

    words = readfile('simple.txt')
    print(words)


# Call the main function to execute the code
main()