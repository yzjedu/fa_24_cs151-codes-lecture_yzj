import matplotlib.pyplot as plt
import random

def plot_chart(sum_rolls):

    # Data to display on the graph
    xdata = list(range(2, 13))  # Creates a list from 2 to 12 to represent possible sums of two dice rolls
    ydata = sum_rolls  # y-axis data already given as the rolls list

    # Create a bar graph by giving x and y data
    plt.plot(xdata, ydata)  # Argument #1 is x-axis data; #2 is y-axis data

    # Label the x and y axes
    plt.xlabel("Die Roll Sum")  # What to write under the x-axis
    plt.ylabel("Count of Occurrence")  # What to write next to the y-axis

    # Save the plot to a file for later viewing
    plt.savefig("graph.png")  # Save as an image file

    # Show the plot for immediate feedback
    plt.show()

def read_rolls(prompt):
    rolls = input(prompt)
    while not rolls.isdigit() or int(rolls) < 0:
        rolls = input(prompt)
    return int(rolls)

def roll_two_dices():
    return random.randint(1, 6) + random.randint(1, 6)

def roll_distribution(num_rolls):
    # Initialize a list with 11 zeros to store counts of sums (2 to 12)
    sums_count = [0] * 11

    # Roll dice num_rolls times and count occurrences of each sum
    for i in range(num_rolls):
        dice_sum = roll_two_dices()
        sums_count[dice_sum - 2] += 1  # Map sum 2-12 to index 0-10

    return sums_count

# Purpose: Main function to control the flow of the program.
# Parameters: None
# Return: None
def main():
    print('\n\nThis program plots the normal distribution of rolling two dices\n')
    num_rolls = read_rolls("How many times would you like to roll the dice? ")
    sums_count = roll_distribution(num_rolls)
    print()
    print(f'The list is: {sums_count} \n')
    plot_chart(sums_count)
    print('\nThank you for using this program\n\n')

main()