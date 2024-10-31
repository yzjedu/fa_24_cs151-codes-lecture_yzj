def write_list_to_file(my_list, filename):
    # Open the file for writing
    fd = open(filename, "w")

    # Write each item in the list to the file
    for item in my_list:
        fd.write(str(item))

    # Close the file
    fd.close()

def main():
    fruit_list = ['Apple', 'Orange', 'Banana', 'Blueberry']
    write_list_to_file(fruit_list, "fruit_list.txt")

main()