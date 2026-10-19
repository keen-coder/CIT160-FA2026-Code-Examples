# Definition of the main function.
def main():
    get_name()
    print(f'Hello {name}.')     # This causes an error!

# Definition of the get_name function.
def get_name():
    name = input('Enter your name: ')

if __name__ == '__main__':
    # Call the main function.
    main()
