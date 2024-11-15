def write_from_table(table, output_filename):
    outfile = open(output_filename, 'w')  # Open file for writing

    for row in table:

        # Calculate birth year and title length
        birth_year = row[0] - row[3]
        title_length = len(row[2])

        # Add the birth year and title length to row
        row.append(birth_year)
        row.append(title_length)

        # Create a line to the row
        line = ''
        for item in row:
            line += str(item) + ' '

        # Write line to the output file
        outfile.write(line + '\n')

    outfile.close()  # Close the file

def read_to_file(filename):
    table = []

    try:
        file = open(filename, "r")
        for line in file:
            row = line.split()
            row[0] = int(row[0])  # Convert year to integer
            row[3] = int(row[3])  # Convert age to integer
            table.append(row)

        file.close()  # Close the file after reading

    except FileNotFoundError:
        print("File doesn’t exist")

    return table

def main():
    table = read_to_file("actresses.txt")
    write_from_table(table, "actresses_updated.txt")

main()