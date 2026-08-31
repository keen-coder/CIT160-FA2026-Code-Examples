# ------------------------------------------------------------------------------
# Python has 7 math operators
# +     Addition
# -     Subtraction
# /     Division
# //    Integer Division (The result will be a whole number)
# %     Remainder (Modulus, divides two number and returns the remainder)
# **    Exponent
# ------------------------------------------------------------------------------

def main():
    value1 = 11
    value2 = 2

    add = value1 + value2
    print('value1 + value2 = \t', add)

    subtract = value1 - value2
    print('value1 - value2 = \t', subtract)

    multiply = value1 * value2
    print('value1 * value2 = \t', multiply)

    float_division = value1 / value2
    print('value1 / value2 = \t', float_division)

    # Integer division will truncate the result. Truncate means cut off the decimal
    # places but do not round.
    int_division = value1 // value2
    print('value1 // value2 = \t', int_division)

    exponent = value1 ** value2
    print('value1 ** value2 = \t', exponent)

if __name__ == '__main__':
    main()