
def main():
    # The else clause can be attached to any loop (for or while).
    # The else clause will only execute when the loop it is attached to terminates
    # normally.
    n = 1
    while n < 5:
        print(n)
        n += 1
    else:
        print(f'Now n is {n}.')

    # Here the 2 triggers the if statement to execute which exectues a break.
    # Because we broke out of the loop prematurely, the else clause DOES NOT
    # execute.
    for num in [7, 3, 7, 3, 9]: 
        if num % 2 == 0: 
            print("even number") 
            break
    else:
        print("list does not contain an even number")

    # This example shows using an else with a loop while performing login
    # authentication.
    
    MAX_TRIES = 3
    PASSWORD = '12345'

    for attempt in range(1, MAX_TRIES + 1):
        if (user_password := input('Enter your password: ') == PASSWORD):
            print("Login successful")
            break
    else:
        print("All attempts failed; lock account or alert")

if __name__ == '__main__':
    main()
