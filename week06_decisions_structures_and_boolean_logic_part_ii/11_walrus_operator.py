
def main():
    # print('hello world', end=' ')
    print(pw:='hello world')



    CORRECT = "opensesame"

    # Capture once, reuse multiple times
    pw = = input("Enter password: ")

    if not (pw):
        print("Password cannot be empty.")
    elif len(pw) < 6:
        print("Password too short.")
    elif pw == CORRECT:
        print("Access granted.")
    else:
        print("Access denied.")

    print(pw)

if __name__ == '__main__':
    main()