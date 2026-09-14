# Get information about the auto
make = input("Enter the make of the auto: ")
model = input("Enter the model of the auto: ")
msrp = float(input("Enter the MSRP amount: $"))
discount_percent = float(input("Enter the discount percent as a decimal: "))

# Calculate the amount off the MSRP
amount_off = msrp * discount_percent

# Calculate the discounted price
discounted_price = msrp - amount_off

# Display the auto information and calculations
print("\nAuto Information")
print("Make:", make)
print("Model:", model)
print("MSRP: ${:.2f}".format(msrp))
print("Discount Percent: {:.2f}".format(discount_percent))
print("Amount Off: ${:.2f}".format(amount_off))
print("Discounted Price: ${:.2f}".format(discounted_price))