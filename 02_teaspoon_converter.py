# This program converts tablespoon into teaspoon

# Prompt user to enter the amount of tablespoon
tbsp_str=input('Enter the number of tablespoons: ')
tbsp_int = int(tbsp_str)

# Find out how many teaspoons
teaspoon = 3 * tbsp_int

# Display the numer of teaspoons
print('You need ' , teaspoon, 'teaspoon')
