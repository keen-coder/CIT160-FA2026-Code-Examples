def main():

    age = int(input('Enter your age: '))

    # A person qualifies if they are:
    #     under 13
    # OR
    #     65 or older

    if age < 13 or age >= 65:
        print('Discount applies')
    else:
        print('Regular price')

if __name__ == '__main__':
    main()