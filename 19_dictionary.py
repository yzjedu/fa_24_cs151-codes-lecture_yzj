import string

# This function should be implemented to read from the file and return a list of words.
def read_words_in_file(filename):
    words = []
    try:
        file_data = open(filename, "r")

        for line in file_data:
            line_words = line.split()
            for word in line_words:
                word = word.strip().strip(string.punctuation).lower()
                if word != "":
                    words.append(word)

        file_data.close()
        return words

    except FileNotFoundError:
        print("Sorry, the file does not exist")
        return []

# Function to count word frequencies in a list of words
def word_frequency(wordlist):
    word_dict = {}
    for word in wordlist:
        if word in word_dict:
            word_dict[word] += 1
        else:
            word_dict[word] = 1
    return word_dict

# Function to print the word frequencies
def print_dictionary(dictionary):
    for key in dictionary:
        print(key, ":", dictionary[key])

# Main function to read the file, calculate word frequencies, and print results
def main():
    # Read file and store returned list in words_list
    words_list = read_words_in_file("gettysburg.txt")

    # Find frequency and store in frequency_dict
    frequency_dict = word_frequency(words_list)

    # Output the result
    print_dictionary(frequency_dict)

    # Output the number of unique words
    print("The number of unique words is", len(frequency_dict))

# Run the main function
main()