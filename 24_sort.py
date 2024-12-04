#CS151 FA23 Sorting Timing

import random
import time


# Uses the builtin python sort to sort
# Parameters: alist - the list to sort
# Returns: nothing
def builtin_sort(alist):
  alist.sort()


# Uses bubble sort
# Parameters: alist - the list to sort
# Returns: nothing
def bubble_sort(alist):
  i = 0
  while i < len(alist):
    end = len(alist) - i
    j = 0
    while j < end - 1:
      if alist[j] > alist[j + 1]:
        temp = alist[j]
        alist[j] = alist[j + 1]
        alist[j + 1] = temp
      j += 1
    i += 1


# Uses insertion sort code from the book
# Parameters: alist - the list to sort
# Returns: nothing
def insertion_sort(numbers):
  for i in range(1, len(numbers)):
      j = i
      # Insert numbers[i] into sorted part
      # stopping once numbers[i] in correct position
      while j > 0 and numbers[j] < numbers[j - 1]:
          # Swap numbers[j] and numbers[j - 1]
          temp = numbers[j]
          numbers[j] = numbers[j - 1]
          numbers[j - 1] = temp
          j = j - 1


# Uses selection sort code from the book
# Parameters: alist - the list to sort
# Returns: nothing
def selection_sort(numbers):
  for i in range(len(numbers) - 1):
      # Find index of smallest remaining element
      index_smallest = i
      for j in range(i + 1, len(numbers)):
          if numbers[j] < numbers[index_smallest]:
              index_smallest = j

      # Swap numbers[i] and numbers[index_smallest]
      temp = numbers[i]
      numbers[i] = numbers[index_smallest]
      numbers[index_smallest] = temp


# Finds how long it takes to sort a list ITERATIONS times
# Parameters:   sort_name - which sort to time
#               size - how big a list to sort
# Returns: total time taken for all sorts
def time_sort(sort_name, size):

  ITERATIONS = 10000  # DO NOT EDIT

  # Total time spent
  totaltime = 0

  # Sorted list to start with
  mylist = list(range(size))

  # Loop a lot to figure out how long a single sort takes
  for i in range(ITERATIONS):

    # shuffle the list so we have a new version to try to sort that isn't in order
    random.shuffle(mylist)

    # Perform sort on list, timing how long it takes
    start = time.process_time()
    sort_name(mylist)
    totaltime += time.process_time() - start

  return totaltime


def time_all(size):
  print("Running bubble...")
  totalb = time_sort(bubble_sort, size)
  print("Running built-in...")
  totalsort = time_sort(builtin_sort, size)
  print("Running insertion...")
  totali = time_sort(insertion_sort, size)
  print("Running selection...")
  totals = time_sort(selection_sort, size)

  print("The results from running all four are:")
  print("Sort\t\tTime")
  print(f"Bubble\t\t{totalb}")
  print(f"Insertion\t{totali}")
  print(f"Selection\t{totals}")
  print(f"Built-in\t{totalsort}\n")

  return totalb + totali + totals + totalsort


# Get type safe integer input from the user
# Parameters: Message to display to the user
# Returns: int typed in by the user
def input_int(msg):

  # Ask user for an integer using parameter as prompt
  candidate = input(msg)

  # while the user hasn't provided an integer, ask again
  while not candidate.isdigit():
    print("Sorry, please enter an integer")
    candidate = input(msg)

  # Return user's input, typecast to an int
  return int(candidate)


# Get menu selection from the user
# Parameters: none
# Returns: int of menu choice
def menu():
  # Create list of menu options to output to user
  menuoptions = "\t1. Bubble Sort\n" +\
                "\t2. Insertion Sort\n" +\
                "\t3. Selection Sort\n" +\
                "\t4. Python's sort function\n" +\
                "\t5. Run all and compare\n" +\
                "\t0. Exit"

  # Output options with nice formatting
  print("-" * 40)
  print("Please select what you would like to time:")
  print(menuoptions)
  print("-" * 40)

  # Ask user for choice using int input function, until they provide a valid value
  choice = input_int("Your selection: ")
  while choice > 5:
    print("That is not an option. As a reminder, your options are: ")
    print(menuoptions)
    choice = input_int("Your selection: ")

  return choice  # Return user's choice as an int (typecasted above)


# Finds out how long it takes to perform tasks recursively and looping
# Parameters: none
# Returns: none
def main():

  print(
      "Welcome! This program will tell you how long it will take to perform various tasks."
  )

  # Get user's choices
  choice = menu()

  # while the user hasn't chosen to quit, do their choice and ask again for a choice
  while choice != 0:

    # Initialize variables for next run.
    total = 0
    n = input_int("How big a list would you like to test? ")

    if choice == 1:  # bubble sort
      total = time_sort(bubble_sort, n)

    elif choice == 2:  # insertion sort
      total = time_sort(builtin_sort, n)

    elif choice == 3:  # selection sort
      total = time_sort(insertion_sort, n)

    elif choice == 4:  # built-in sort
      total = time_sort(selection_sort, n)
    else:
      total = time_all(n)

    print("That took", total,
          "seconds.")  # Output timing results from whichever option ran

    choice = menu()  # Ask user to choose again


main()  # Run the program
