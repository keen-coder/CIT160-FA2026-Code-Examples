# ------------------------------------------------------------------------------
# The order in which you list the designators is important!
#
# SYNTAX: f'{value:[[fill_char]alignment][[0]width][,][.precision][f or d or s or %]}'
# ------------------------------------------------------------------------------

def main():

    # Center-align a float, width of 20, round to two decimal places, group with commas

    number = 123456.7890
    print(f'|{number:-^20,.2f}|')

if __name__ == '__main__':
    main()