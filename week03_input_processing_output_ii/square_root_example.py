# This program demonstrates two ways to compute the square root in Python.
# OPTION 1: Importing the math module and use the math.sqrt() function
# OPTION 2: Use the ** operator to raise the value to the power of 1/2

import math # to use the math.sqrt() function, you need to import the 
            # math module

def main():
    # OPTION 1: math.sqrt()
    x = 16
    sqrt_x = math.sqrt(x)
    print(f'The square root of {x} is {sqrt_x}')

    # OPTION 2: ** (1/2)
    y = 64
    sqrt_y = y ** (1/2)
    print(f'The square root of {y} is {sqrt_y}')

if __name__ == '__main__':
    main()