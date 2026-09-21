# Get the user's first name and number of steps
first_name = input("Enter your first name: ")
steps = int(input("Enter the number of steps walked: "))

# Calculate calories burned
calories_burned = steps * 0.25

# Display the first name and calories burned
print("First Name:", first_name)
print("Calories Burned:", format(calories_burned, ".2f"))