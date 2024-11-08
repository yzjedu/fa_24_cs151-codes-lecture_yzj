import string

# Problem 3
def read_words(filename):
    words = []

    with open(filename, "r") as file_data:  # Automatically handles file closing
        for line in file_data:
            line = line.split()
            for word in line:
                # Strip punctuation from the word
                word = word.strip(string.punctuation)
                if len(word) > 0:  # Check if the word is not empty
                    words.append(word)

    return words

def main():

    words = read_words('simple.txt')
    print(words)


# Call the main function to execute the code
main()