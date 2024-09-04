def print_space(space):
    if space > 0:
        print(" ", end="")
        print_space(space - 1)

def print_star(star):
    if star > 0:
        print("*", end="")
        print_star(star - 1)

def print_pyramid(n, current_row=1):
    if current_row > n:
        return

    spaces = n - current_row
    stars = 2 * current_row - 1

    # Print spaces
    print_space(spaces)

    # Print stars
    print_star(stars)

    # Move to the next line for the next row
    print()

    # Print the pyramid for the next row
    print_pyramid(n, current_row + 1)

# Set the number of rows for the pyramid
n = 5

# Print the pyramid pattern
print_pyramid(n)
##new program using alphabets
n = 5
alph = 65
for i in range(0, n):
    print(" " * (n-i), end=" ")
    for j in range(0, i+1):
        print(chr(alph), end=" ")
        alph += 1
    alph = 65
    print()
## program to print the pattern with numbers
def print_number_pyramid(rows):
    for i in range(1, rows + 1):
        # Print spaces
        for j in range(rows - i):
            print(" ", end="")
        # Print numbers
        for j in range(2 * i - 1):
            print(j + 1, end="")
        # Move to the next line after each row
        print()

# Example usage
num_rows = 5
print_number_pyramid(num_rows)
## python program to print the inverted pyramid
# Function to print inverted full pyramid pattern
def inverted_full_pyramid(n):
    # Outer loop for the number of rows
    for i in range(n, 0, -1):
        # Inner loop for leading spaces in each row
        for j in range(n - i):
            print(" ", end="")
        # Inner loop for printing asterisks in each row
        for k in range(2*i - 1):
            print("*", end="")
        # Move to the next line after each row
        print("")

# Set the value of n (number of rows)
n = 5

# Call the function to print the inverted full pyramid
inverted_full_pyramid(n)
# program to print the hallow pyramid
def hollow_pyramid(n):
    for i in range(1, n + 1):
        for j in range(1, 2 * n):
            if j == n - i + 1 or j == n + i - 1 or i == n:
                print("*", end="")
            else:
                print(" ", end="")
        print()

# Set the number of rows for the pyramid
rows = 5

# Call the function with the specified number of rows
hollow_pyramid(rows)



