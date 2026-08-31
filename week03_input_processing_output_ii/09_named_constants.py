# ------------------------------------------------------------------------------
# Named Constants are names that represent special values in your program. These
# values should generally not change. They can be actual mathematical constants
# like PI, or Euler's number e and so on. 
#
# Most programming languages will enforce that a constant's value cannot change.
# Python does not do this but all programmers conventionally agree when something
# is a constant, they will not change the value.
#
# Constants should be named using ALL CAPS with words separated by underscores.
# ------------------------------------------------------------------------------

def main():

    # Without using constants, code is harder to read.
    price = 50
    tax = price * 0.06 #<-- What is 0.06?
    total = price + tax
    print(total)

    # Constants make the code more readible
    TAX_RATE = 0.06  # 6% sales tax

    price = 50
    tax = price * TAX_RATE
    total = price + tax
    print(total)

    # Example: Unit conversion
    FEET_TO_METERS = 0.3048

    feet = float(input("Enter length in feet: "))
    meters = feet * FEET_TO_METERS
    print("Meters:", meters)

    # Fixed prices and discounts
    BASE_PRICE = 19.99
    DISCOUNT_RATE = 0.15  # 15%

    quantity = int(input("How many items? "))
    subtotal = BASE_PRICE * quantity
    discount = subtotal * DISCOUNT_RATE
    total = subtotal - discount
    print("Total after discount:", total)

    # Time and Date parts
    MINUTES_PER_HOUR = 60
    HOURS_PER_DAY = 24

    hours = int(input("Hours: "))
    minutes = hours * MINUTES_PER_HOUR
    print("Minutes:", minutes)

    days = int(input("Days: "))
    hours_total = days * HOURS_PER_DAY
    print("Hours in those days:", hours_total)

    # Ticket prices and service fees
    TICKET_PRICE = 12.00
    SERVICE_FEE = 2.50

    count = int(input("Number of tickets: "))
    subtotal = count * TICKET_PRICE
    total = subtotal + SERVICE_FEE
    print("Total cost:", total)

    # Limiting Attempts
    MAX_ATTEMPTS = 3

    print("You have", MAX_ATTEMPTS, "attempts.")
    # (Later, when loops are introduced, you can use this to control retry logic.)

    # Calorie Counter
    CAL_PIZZA_SLICE = 285
    CAL_APPLE = 95
    CAL_MILK = 150

    slices = int(input("Pizza slices: "))
    apples = int(input("Apples: "))
    milks = int(input("Milk cartons: "))

    total_cal = slices * CAL_PIZZA_SLICE + apples * CAL_APPLE + milks * CAL_MILK
    print("Total calories:", total_cal)

if __name__ == '__main__':
    main()