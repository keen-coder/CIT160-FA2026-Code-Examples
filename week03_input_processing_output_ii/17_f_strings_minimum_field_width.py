# ------------------------------------------------------------------------------
# Format specifiers can also take an integer value to designate a minimum field
# width. This is the minimum number of spaces to be used to display the value.
#
# If the value is larger than the width, the column will be expanded to exactly
# accomodate the value.
#  
# If the value is smaller than the width, extra space will be padded to the left 
# of the value.
#
# If you put a 0 in front of the width value, the extra spaces will be replaced
# with leading zeros.
# ------------------------------------------------------------------------------

def main():
    # Formatting the value with a field width of 10
    number = 99
    print(f'The number is {number:10d}')

    # Using leading zeros and field width
    number = 99
    print(f'The number is {number:010d}')

    # If the value is larger than the width, the column will expand to accomodate
    # exactly the right about of space with no extra padding
    number = 9999
    print(f'The number is {number:2d}')

    # Formatting a float to 2 decimal places, group using commas, with a field width
    # of 12

    number = 12345.6789

    # NOTE: The comma for grouping goes after the width and BEFORE the precision
    # designator.
    print(f'The number is {number:12,.2f}')

    # Same example as the previous, but without the commas grouping
    number = 12345.6789
    print(f'The number is {number:12.2f}')

    # Field widths are mainly used to display output in a tabular (table / 
    # column-like format)
    print('\n----------------------------')
    num1 = 127.899
    num2 = 3465.148
    num3 = 3.776
    num4 = 264.821
    num5 = 88.081
    num6 = 799.999

    print(f'{num1:10.2f}{num2:10.2f}')
    print(f'{num3:10.2f}{num4:10.2f}')
    print(f'{num5:10.2f}{num6:10.2f}')

if __name__ == '__main__':
    main()