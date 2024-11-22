def read_file_to_dict(filename):
    morse_dict = {}
    morse_data = open(filename, 'r')
    for line in morse_data:
        items = line.strip().split()
        key = items[1]
        value = items[0]
        morse_dict[key] = value
    morse_data.close()
    return morse_dict

def main():
    morse_dictionary = read_file_to_dict('morsecode.txt')
    for key in morse_dictionary:
        print(key, ' : ', morse_dictionary[key])
main()