# ------------------------------------------------------------------------------
# Integers can also be formatted with f-strings. You have to use the character 
# 'd' (Decimal integer) as the type specifier. You would think it should be 'i'
# but sadly no.
#
# Since integers do not have a floating-point part, you cannot use a precision
# designator with integers.
#
# Typically integers are formatted with comma grouping, leading zeros, and 
# width specifiers (see future examples)
# ------------------------------------------------------------------------------

def main():
    magic_number = 123456789


    # Technically the :d here is not required since no other formatting is applied.
    print(f'magic_number = {magic_number:d}')

    # Comma grouping
    print(f'magic_number = {magic_number:,d}')

if __name__ == '__main__':
    main()