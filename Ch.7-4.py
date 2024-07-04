##Robert Fernandez
##Complete
##This program will ask the user to enter a value into each of the columns and rows that will create a 2-D table of each integer the user selected and calculate the total sum of the elements. 


# Define the number of rows and columns
rows, cols = 4, 3

# This creates the 2D list with 4 rows and 3 columns
two_d_list = [[0 for _ in range(cols)] for _ in range(rows)]

# Get an integer value from the user for each element in the list
for i in range(rows):
    for j in range(cols):
        two_d_list[i][j] = int(input(f'Enter an integer for element [{i}][{j}]: '))

# Print the 2D list to verify its structure
print("2D List:")
for row in two_d_list:
    print(row)

# Sum and display each element in the list and print the total of all elements
total_sum = 0
for i in range(rows):
    for j in range(cols):
        total_sum += two_d_list[i][j]

print(f'The sum of all elements is: {total_sum}')
