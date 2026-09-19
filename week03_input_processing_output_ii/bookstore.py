# Suppose the cover price of a book is $24.95, but bookstores get a 40% discount. Shipping costs $3 for the first copy and 75 cents for each additional copy. What is the total cost for 60 copies?*

# Write a program that will allow someone to enter the quantity of books ordered and then print the total cost for that order. 
quantity = int(input('Enter the number of books: '))

price = 24.95 - (24.95 * 0.40)
total_shipping = 3.0 + ((quantity - 1) * 0.75)

total_cost = (price * quantity) + total_shipping
print(total_cost)
