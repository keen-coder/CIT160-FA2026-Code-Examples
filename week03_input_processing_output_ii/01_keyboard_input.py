# ------------------------------------------------------------------------------
# Examples on using the input() function to read user input from the keyboard.
# Keep in mind, the input() function returns a string so all values must be 
# converted to their correct data types unless you actually want a string.
# Always assign the input function to a variable, this will capture the user
# input and store it.
# 
# Syntax: input(<prompt>)
#   <prompt> is the string that you want to display to the user.
# ------------------------------------------------------------------------------

def main():
    # Read the user's name
    name = input('Enter your name: ')

    # Read the person's age and convert it to an integer
    # The int() function is used to convert strings into numbers. Only works if the
    # string contains only valid numeric data. Notice how the input function can
    # be passed to the int() function.
    age = int(input('Enter your age: '))

    # Read the dollar amount and convert it to a float
    # Use the float() function to convert the string.
    income = float(input('What is your income? : '))

    print('Name\t\t',name)
    print('Age:\t\t',age)
    print('Savings:\t', income)
    
if __name__ == '__main__':
    main()