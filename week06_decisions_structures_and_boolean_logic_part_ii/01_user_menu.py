def main():
    # Store the Menu Options as Named Constants.
    # This is best practice.

    ADD_CHOICE = 1
    SUB_CHOICE = 2
    MUL_CHOICE = 3
    DIV_CHOICE = 4

    # Store the text of your menu in a string
    # NOTE: THe use of \ to break up the string over multiple lines this is only
    # for the python syntax, the '\n' character is what allows the string to be
    # printed over multiple lines in the console.

    MENU_TEXT = '\nWelcome to the Simple Calculator!\n' \
                f'{ADD_CHOICE}. Addition\n' \
                f'{SUB_CHOICE}. Subtraction\n' \
                f'{MUL_CHOICE}. Multiplication\n' \
                f'{DIV_CHOICE}. Division\n'

    # Print the menu
    print(MENU_TEXT)

    # get the user's choice
    user_choice = int(input('Enter your choice (1-4): '))

    print()

    # Create your if/elif/else structure for all the choices
    if user_choice == ADD_CHOICE:
        num1 = float(input('Enter number 1: '))
        num2 = float(input('Enter number 2: '))
        sum = num1 + num2
        print(f'{num1} + {num2} = {sum}')
    elif user_choice == SUB_CHOICE:
        num1 = float(input('Enter number 1: '))
        num2 = float(input('Enter number 2: '))
        difference = num1 - num2
        print(f'{num1} - {num2} = {difference}')
    elif user_choice == MUL_CHOICE:
        num1 = float(input('Enter number 1: '))
        num2 = float(input('Enter number 2: '))
        product = num1 * num2
        print(f'{num1} * {num2} = {product}')
    elif user_choice == DIV_CHOICE:
        num1 = float(input('Enter number 1: '))
        num2 = float(input('Enter number 2: '))
        quotient = num1 / num2
        print(f'{num1} / {num2} = {quotient}')
    else:
        print('MENU CHOICE ERROR!')
        print('Program will now exit!')














    
    


if __name__ == '__main__':
    main()