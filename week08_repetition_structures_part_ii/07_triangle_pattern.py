# This program displays a triangle pattern.

def main():
    BASE_SIZE = 8

    for r in range(BASE_SIZE):
        for c in range(r + 1):
            print('*', end='')
        print()

    print()

    for r in range(BASE_SIZE):
        for c in range(BASE_SIZE - r):
            print('*', end='')
        print()





if __name__ == '__main__':
    main()
