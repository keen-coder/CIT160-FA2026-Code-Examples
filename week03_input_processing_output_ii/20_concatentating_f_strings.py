# ------------------------------------------------------------------------------
# Two or more f-strings can be concatenated together just like normal strings.
# The result will also be an f-string.
#
# NOTE: If you leave out the f in front of any string in the concatenation,
# these will be treated as normal strings.
# ------------------------------------------------------------------------------

def main():
      # Correctly concatenating with f-strings
      name = 'Charles Summerton'
      department = 'Sales'
      position = 'Manager'
      print(f'Employee Name: {name}, ' +
            f'Department: {department}, ' +
            f'Position: {position}')

      # Forgetting the f with some strings
      print(f'Employee Name: {name}, ' +
            'Department: {department}, ' +
            'Position: {position}')

      # Implicit concatenation also works
      print(f'Name: {name}, '
            f'Department: {department}, '
            f'Position: {position}')

if __name__ == '__main__':
    main()