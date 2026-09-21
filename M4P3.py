# Get the meal total from the user
meal_total = float(input("Enter the total for the meal: "))

# Calculate the 15% tip
tip15 = meal_total * 0.15
total15 = meal_total + tip15

# Calculate the 18% tip
tip18 = meal_total * 0.18
total18 = meal_total + tip18

# Calculate the 20% tip
tip20 = meal_total * 0.20
total20 = meal_total + tip20

# Display the results
print("With 15% Tip:")
print("Total:", format(meal_total, ".2f"))
print("Tip:", format(tip15, ".2f"))
print("Total with Tip:", format(total15, ".2f"))
print()

print("With 18% Tip:")
print("Total:", format(meal_total, ".2f"))
print("Tip:", format(tip18, ".2f"))
print("Total with Tip:", format(total18, ".2f"))
print()

print("With 20% Tip:")
print("Total:", format(meal_total, ".2f"))
print("Tip:", format(tip20, ".2f"))
print("Total with Tip:", format(total20, ".2f"))