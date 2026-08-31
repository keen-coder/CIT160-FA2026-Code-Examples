# ------------------------------------------------------------------------------
# Placeholders expressions can be any value expression.
# ------------------------------------------------------------------------------

def main():

    print(f'The value is {42+7}.')

    value = 42

    # NOTE: In the following line of code, value is not change. It is still 42
    # after line 11. 7 is added to 42 and then displayed.
    print(f'The value + 7 is {value+7}.')
    print(f'Value is still {value}')

if __name__ == '__main__':
    main()