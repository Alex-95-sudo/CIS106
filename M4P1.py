# Get the two exam scores from the user
exam1 = float(input("Enter the first exam score: "))
exam2 = float(input("Enter the second exam score: "))

# Calculate the weighted scores
weighted_exam1 = exam1 * 0.60
weighted_exam2 = exam2 * 0.40

# Calculate the total score
total_score = weighted_exam1 + weighted_exam2

# Display the total score
print("Total score:", format(total_score, ".2f"))