# ------------------------------------------------------------------------------
# The behavior of the print() function can be changed using the 'end' and 'sep'
# arguments.
# ------------------------------------------------------------------------------

def main():
    # Changing the end of line character:
    # Normally when you print(), the print() function will automatically add the
    # new line character (\n) to the end of the line.
    print('old pond')
    print('frog leaps in')
    print("water's sound")

    print('-------------------------------------------------------------------------')

    # You can change the end character by using the end= argument.
    print('old pond', end=' ')
    print('frog leaps in', end=' ')
    print("water's sound")

    # Same example but with tabs
    print('old pond', end='\t')
    print('frog leaps in', end='\t')
    print("water's sound")

    print('-------------------------------------------------------------------------')

    # print() Also has the 'sep' argument which allows you to change the default
    # seperator when printing multiple things in the same print function.
    # The default separator is the 'space' character

    print('old pond','frog leaps in',"water's sound")
    print('old pond','frog leaps in',"water's sound", sep=',', end='??????')
    print('old pond','frog leaps in',"water's sound", sep='@')

if __name__ == '__main__':
    main()