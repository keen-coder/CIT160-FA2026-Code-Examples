def main():
    # Store the Menu Options as Named Constants.
    # This is best practice.

    ADD_CHOICE = 1
    SUB_CHOICE = 2
    MUL_CHOICE = 3
    DIV_CHOICE = 4

    # Store the text of your menu in a string
    # NOTE: THe use of \ to break up the string over multiple lines

    MENU_TEXT = '\nWelcome to the Simple Calculator!\n' \
                '1. Addition\n' \
                '2. Subtraction\n' \
                '3. Multiplication\n' \
                '4. Division\n'

    # Print the menu
    print(MENU_TEXT)

    # get the user's choice
    user_choice = int(input('Enter your choice (1-4): '))

    # Make sure to validate the user's choice
    # Later on we will see how to do this with a loop so the user doesn't 
    # have to rerun the program.
    if user_choice < 1 or user_choice > 4:
        print('MENU CHOICE ERROR!')
        print('Menu choice can only be a number between 1 and 4.')
        print('Program will now exit!')
        exit(1)

    # Request two numbers to calculate
    num1 = float(input('Enter number 1: '))
    num2 = float(input('Enter number 2: '))

    print()

    # Create your if/elif/else structure for all the choices
    if user_choice == ADD_CHOICE:
        sum = num1 + num2
        print(f'{num1} + {num2} = {sum}')
    elif user_choice == SUB_CHOICE:
        difference = num1 - num2
        print(f'{num1} - {num2} = {difference}')
    elif user_choice == MUL_CHOICE:
        product = num1 * num2
        print(f'{num1} * {num2} = {product}')
    elif user_choice == DIV_CHOICE:
        quotient = num1 / num2
        print(f'{num1} / {num2} = {quotient}')















    
    


if __name__ == '__main__':
    main()