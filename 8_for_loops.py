

def print_by_line(my_list):
    # Iterate through each item in the list and print it on a new line
    for item in my_list:
        print(item)

def find_first(name_list, char):
    # Iterate through each name in the list
    for name in name_list:
        # Check if the first character of the name matches the given character
        if name[0] == char:
            return name  # Return the name if found

    return "not found"  # Return "not found" if no matching name is found

def main():
    fruit_list = ['Apple', 'Orange', 'Banana', 'Blueberry']
    print_by_line(fruit_list)
    name = find_first(fruit_list, 'B')
    print('-' * 40)
    print(f'The first name that starts with B is: {name}')

main()