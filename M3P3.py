# Get the amount received for the job
amount = float(input("Enter the amount received for the job: $"))

# Split the amount evenly between three people
share = amount / 3

# Display the amount each person will receive
print("Each person will receive: ${:.2f}".format(share))