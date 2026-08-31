# ------------------------------------------------------------------------------
# Two or more strings can be concatenated (combined) using the + operator. If
# you want to concatentate a string with a non-string, the non-string needs to
# be converted into a string using the str() conversion function
# ------------------------------------------------------------------------------

def main():
      first_name = 'John'
      last_name = 'Smith'

      full_name = first_name + ' ' + last_name
      print('Name:\t', full_name)

      radius = 5.4
      PI = 3.14159265
      area = PI * radius ** 2

      # Note in this line you need to convert area to a string.
      output = 'The area of the circle is: ' + str(area)
      print(output)

      # String literals adjacent to each other, separated by only tabs, spaces,
      # or newline characters will be implicitly (automatically) concatenated into a
      # single string.
      numbers = 'one' 'two' 'three'
      print(numbers)

      print('It is dangerous '
            'to go alone. '
            'Take this.')

if __name__ == '__main__':
    main()