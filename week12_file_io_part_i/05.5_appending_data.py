# This program shows how to append data to an existing file.

def main():
    # Open a file for writing in append mode.
    outfile = open('colors.txt', 'a')

    # Get three numbers from the user.
    color1 = input('Enter a color: ')
    color2 = input('Enter another color: ')
    color3 = input('Enter another color: ')

    # Write the numbers to the file.
    outfile.write('\n' + color1 + '\n')
    outfile.write(color2 + '\n')
    outfile.write(color3 + '\n')

    # Close the file.
    outfile.close()
    print('Data written to colors.txt')

# Call the main function.
if __name__ == '__main__':
    main()