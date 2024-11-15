
def read_to_table(filename):
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

def find_name_by_year(actresses, year):
    for row in actresses:
        if row[0] == year:
            return row[1]

def find_youngest_actress(actresses):
    # Initialize the first actress as the youngest for comparison
    youngest_row = actresses[0]

    # Iterate through each actress record
    for row in actresses:
        # Check if the current actress is younger than the current youngest
        if row[3] < youngest_row[3]:  # Assuming age is at index 3
            youngest_row = row

    # Return the data of the youngest actress
    return youngest_row

def main():
    # Lecture note 26
    a_table = read_to_table("actresses.txt")

    print(f'first ten winners {a_table[:10]}')

    print(f'last ten winners {a_table[-10:]}')

    print(f'20th to 40th winners {a_table[19:40]}')

    print(f'Winners reversed {a_table[::-1]}')
    print()

    print(f'Year of the first best actress is: {a_table[0][0]}')
    print(f'Name of the winner of the 4th best actress is: {a_table[3][1]}')
    print()

    print('Age of all actresses')
    for row in a_table:
        print(row[3], end=' ')
    print()
    for i in range(len(a_table)):
        print(a_table[i][3], end=' : ')
    print('\n')

    # Lecture note 27
    year = 1932
    name = find_name_by_year(a_table, year)
    print(f'The name of the winner of the {year} best actress is {name}')
    youngest_actress_data = find_youngest_actress(a_table)
    youngest_actress_name = youngest_actress_data[1]
    youngest_actress_age = youngest_actress_data[3]
    print(f'{youngest_actress_name} is the youngest actress to win oscar at the age of {youngest_actress_age}')

main()