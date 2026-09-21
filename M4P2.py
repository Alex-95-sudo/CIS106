# Get the stock information from the user
purchase_price = float(input("Enter the purchase price per share: $"))
current_price = float(input("Enter the current stock price: $"))
quantity = int(input("Enter the quantity of stock: "))

# Calculate the increase or decrease in value
change = (current_price - purchase_price) * quantity

# Display the result
print("Increase or decrease in stock value: $", format(change, ".2f"))