import matplotlib.pyplot as plt
import string

def plot_nationality_distribution(nationality_dict):

    # Data to display on the graph
    xdata = nationality_dict.keys()  # Nationalities as x-axis data
    ydata = nationality_dict.values()  # Counts as y-axis data

    # Create a bar graph using xdata for x-axis and ydata for y-axis
    plt.bar(xdata, ydata)

    # Add labels for x and y axes
    plt.xlabel("Nationality")
    plt.ylabel("Count")

    # Rotate x-axis labels to make them readable
    plt.xticks(rotation=45, ha="right")  # Rotate labels by 45 degrees
    plt.title("Nationality Distribution")
    # Display the plot
    plt.savefig("nationality_distribution.png")
    plt.show()

    plt.show()

def read_nationalities_in_file(filename):
    nationalities = []
    try:
        file_data = open(filename, "r")

        for line in file_data:
            nationality = line.split()[4]
            nationalities.append(nationality)
        file_data.close()
        return nationalities

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
    nationalities_list = read_nationalities_in_file("actresses.txt")

    # Find frequency and store in frequency_dict
    frequency_dict = word_frequency(nationalities_list)

    # Output the result
    plot_nationality_distribution(frequency_dict)

# Run the main function
main()