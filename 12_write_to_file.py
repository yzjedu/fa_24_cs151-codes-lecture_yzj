def write_list_to_file(my_list, filename):
    # Open the file for writing
    fd = open(filename, "w")

    # Write each item in the list to the file
    for item in my_list:
        fd.write(str(item))

    # Close the file
    fd.close()

def main():
    fruit_list = []
    SENTINEL = 'quit'
    user_input = ''
    while user_input != SENTINEL:
        user_input = input('Enter fruit or type (quit) to end the program: ').lower().strip()
        if user_input != '' and user_input != SENTINEL:
            fruit_list.append(user_input)

    if len(fruit_list) != 0:
        write_list_to_file(fruit_list, "fruit_list.txt")

main()