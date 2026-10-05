def main():
    

    # This part does not use the walrus operator
    score = int(input('Enter your score: '))
    while score < 0:
        print('The score cannot be negative.')
        score = int(input('Enter your score:'))
    print(score)

    # With the walrus operator, you can make the code more concise
    while ( score := int(input('Enter your score: ')) ) < 0:
        print('The score cannot be negative.')

    # Using the walrus operator in this way also makes the score variable
    # accessible outside of the while loop structure without having to 
    # define the variable above the loop as in the first part of this example.
    print(score)


if __name__ == '__main__':
    main()

