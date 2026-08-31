# ------------------------------------------------------------------------------
# Placeholders in an f-string can include a format specifier which will format
# the value being displayed. The value stored in the variable is unchanged,
# formatting is ONLY for display purposes.
#
# SYNTAX: {placeholder:format-specifier}
# ------------------------------------------------------------------------------

def main():

    # This program demonstrates how a floating-point
    # number is displayed with no formatting.
    amount_due = 5000.0
    monthly_payment = amount_due / 12.0
    print(f'The monthly payment is {monthly_payment}.')

    # This program demonstrates how a floating-point
    # number can be rounded.
    amount_due = 5000.0
    monthly_payment = amount_due / 12.0

    # .2 is the precision designator
    # f is the type designator (in this case f means float)
    print(f'The monthly payment is {monthly_payment:.2f}.')

    # Rounding PI to 3 decimal places
    pi = 3.1415926535
    print(f'{pi:.3f}')

    # Rounding to 1 decimal place
    a = 2 
    b = 3 
    print(f'{(a / b):.1f}')

if __name__ == '__main__':
    main()