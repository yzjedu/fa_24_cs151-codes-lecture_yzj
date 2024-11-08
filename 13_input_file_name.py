import os

def read_file_to_list_int(filename):
    # Open the file for reading
    file_data = open(filename, 'r')
    grades = []

    # Read each line, convert to integer, and append to the grades list
    for line in file_data:
        line = int(line.strip())  # Convert each line to an integer and strip any whitespace/newline
        grades.append(line)

    # Close the file
    file_data.close()

    # Return the list of grades
    return grades

def read_filename():
    # Prompt user for the filename to read
    name = input("What file do you want to read? ")

    # Check if the file exists, and if not, ask again until a valid file is entered
    while not os.path.isfile(name):
        print("That file does not exist. Please try again.")
        name = input("What file do you want to read? ")

    # Return the valid filename
    return name

def main():
    # Read the contents of 'grades.txt' and store them in the grades list
    file_name = read_filename()
    grades = read_file_to_list_int(file_name)

    # Calculate the average, minimum, and maximum of the grades
    average = sum(grades) / len(grades)
    minimum = min(grades)
    maximum = max(grades)

    # Print the results
    print(f"Average grade: {average:.2f}")
    print(f"Minimum grade: {minimum}")
    print(f"Maximum grade: {maximum}")

# Call the main function to execute the code
main()