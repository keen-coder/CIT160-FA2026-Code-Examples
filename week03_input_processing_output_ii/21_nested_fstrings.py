price = 24.8487646

# We want to format the value to two decimal places
# And also format the width. This is a special case where
# we want the '$' to be next to the price. Since price
# is a number and $ is a character we need to concatenate
# the two together, but we need to format the number first
# BEFORE turning it into a string and concatenting.
print(f'Price:{'$'+f"{price:.2f}":>24}')

# Here, format the price first, store the result in a variable
# then plug the variable into the second f-string.
print_format = f"{price:.2f}"
print(f'Price:{'$'+print_format:>24}')