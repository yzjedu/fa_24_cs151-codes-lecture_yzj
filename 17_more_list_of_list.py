def read_file(filename):
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

def find_oldest_actress(actresses):
    oldest_row = actresses[0]

    for row in actresses:
        if row[3] > oldest_row[3]:  # Assuming age is at index 3
            oldest_row = row

    return oldest_row

def find_average_age(actresses):
    total_age = 0
    count = 0

    for row in actresses:
        total_age += row[3]  # Assuming age is at index 3
        count += 1

    return total_age / count if count > 0 else 0

def find_actresses_by_nationality(actresses, nationality):
    results = []

    for row in actresses:
        if row[4].lower() == nationality.lower():  # Assuming nationality is at index 4
            results.append(row)

    return results

def find_actresses_by_age(actresses, age):
    results = []

    for row in actresses:
        if row[3] == age:  # Assuming age is at index 3
            results.append(row)

    return results

def find_movie_with_longest_name(actresses):
    longest_movie_row = actresses[0]

    for row in actresses:
        if len(row[2]) > len(longest_movie_row[2]):  # Assuming movie title is at index 2
            longest_movie_row = row

    return longest_movie_row

def find_movie_with_shortest_name(actresses):
    shortest_movie_row = actresses[0]

    for row in actresses:
        if len(row[2]) < len(shortest_movie_row[2]):  # Assuming movie title is at index 2
            shortest_movie_row = row

    return shortest_movie_row

def find_actresses_with_letter_in_name(actresses, letter):
    results = []

    for row in actresses:
        if letter.lower() in row[1].lower():  # Assuming actress name is at index 1
            results.append(row)

    return results

def find_actresses_with_letter_in_last_name(actresses, letter):
    results = []

    for row in actresses:
        last_name = row[1].split('_')[-1]  # Assuming actress name is at index 1 and last name follows '_'
        if last_name.lower().startswith(letter.lower()):
            results.append(row)

    return results

def find_actresses_by_age(actresses, age):
    results = []

    for row in actresses:
        if row[3] == age:  # Assuming age is at index 3
            results.append(row)

    return results

def main():
    table = read_file("actresses.txt")


    # Find the oldest actress and display her information
    oldest_actress_data = find_oldest_actress(table)
    oldest_actress_name = oldest_actress_data[1]  # Assuming actress name is at index 1
    oldest_actress_age = oldest_actress_data[3]  # Assuming age is at index 3
    print(f'{oldest_actress_name} is the oldest actress to win an Oscar at the age of {oldest_actress_age}')

    # Using the function to find the average age
    average_age = find_average_age(table)
    print(f"The average age of the actresses is {average_age:.2f} years.")

    # Using the function to find the longest movie name
    longest_movie_name_data = find_movie_with_longest_name(table)
    longest_movie_name = longest_movie_name_data[2]
    print(f"The movie with the longest name is '{longest_movie_name}'.")

    # Call other function and experiment

main()