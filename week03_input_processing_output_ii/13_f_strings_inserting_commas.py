# ------------------------------------------------------------------------------
# Large numbers can be formatted to display comma separators every 3 digits,
# just like we do in real life.
#
# You can put a comma in the format-specifier to display commas in the output.
#
# ------------------------------------------------------------------------------

def main():
    value = 1234567890.12345

    # Notice the use of the comma in the format specifier
    print(f'value is {value:,}')

    # You can even combine format specifiers to round and have commas.
    # NOTE: The comma must come BEFORE the precision designator
    print(f'value is {value:,.2f}')

    monthly_pay = 5000.0
    annual_pay = monthly_pay * 12
    print(f'Your annual pay is ${annual_pay:,.2f}')

if __name__ == '__main__':
    main()