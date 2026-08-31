# ------------------------------------------------------------------------------
# By default, if a value is smaller than the designated column width, it will
# be padded with spaces on the left (meaning the value is right-aligned).
#
# You can actually specify that a value should be right, left, or center-aligned
# using alignment specifiers.
# 
# < for left-align (this is the default for str)
# > for right-align (this is the default for int and float)
# ^ for center-align
# ------------------------------------------------------------------------------

def main():

    # Right-align all the output.

    name1 = 'Gordon'
    name2 = 'Smith'
    name3 = 'Washington'
    name4 = 'Alvarado'
    name5 = 'Livingston'
    name6 = 'Jones'

    print('RIGHT ALIGN--------------------------')
    print(f'|{name1:>20}|')
    print(f'|{name2:>20}|')
    print(f'|{name3:>20}|')
    print(f'|{name4:>20}|')
    print(f'|{name5:>20}|')
    print(f'|{name6:>20}|')

    print('\nLEFT ALIGN--------------------------')
    print(f'|{name1:<20}|')
    print(f'|{name2:<20}|')
    print(f'|{name3:<20}|')
    print(f'|{name4:<20}|')
    print(f'|{name5:<20}|')
    print(f'|{name6:<20}|')

    print('\nCENTER ALIGN--------------------------')
    print(f'|{name1:-^20}|')
    print(f'|{name2:-^20}|')
    print(f'|{name3:-^20}|')
    print(f'|{name4:-^20}|')
    print(f'|{name5:-^20}|')
    print(f'|{name6:-^20}|')

if __name__ == '__main__':
    main()