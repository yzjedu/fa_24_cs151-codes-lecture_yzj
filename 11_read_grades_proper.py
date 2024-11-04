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

def read_file_to_list_split(filename):
    # Open the file for reading
    file_data = open(filename, 'r')
    grades = []

    # Read each line, convert to integer, and append to the grades list
    for line in file_data:
        line = line.split()
        line = map(int, line)
        grades.extend(line)

    # Close the file
    file_data.close()

    # Return the list of grades
    return grades

def main():
    # Read the contents of 'grades.txt' and store them in the grades list
    grades = read_file_to_list_int("grades.txt")
    #grades = read_file_to_list_split("grades_one_line.txt")
    print(grades)
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