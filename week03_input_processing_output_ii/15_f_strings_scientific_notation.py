# ------------------------------------------------------------------------------
# F-strings can be used to display a floating-point value using scientific
# notation
# ------------------------------------------------------------------------------

def main():
    # The first example simply displays the value using scientific notation
    number = 12345.6789
    print(f'{number:e}')

    # This example rounds to two decimal places AND uses scientific notation.
    # NOTE: The e needs to come AFTER the precision designator
    print(f'{number:.2e}')

if __name__ == '__main__':
    main()