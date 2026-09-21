# Get the business costs and prices from the user
fixed_costs = float(input("Enter fixed costs: $"))
price_per_unit = float(input("Enter price per unit: $"))
cost_per_unit = float(input("Enter cost per unit: $"))

# Calculate the break-even point
break_even = fixed_costs / (price_per_unit - cost_per_unit)

# Display the break-even point
print("Break-even point:", format(break_even, ".2f"), "units")