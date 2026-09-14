# Get the student's information
last_name = input("Enter your last name: ")
midterm = float(input("Enter your midterm exam score (0-100): "))
final = float(input("Enter your final exam score (0-100): "))

# Calculate the total exam points
total = (midterm * 0.40) + (final * 0.60)

# Display the results
print("Student last name:", last_name)
print("Total exam points: {:.2f}".format(total))