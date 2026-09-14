# Get input from the user
ticker = input("Enter the stock ticker symbol: ")
shares = float(input("Enter the number of shares: "))
cost_per_share = float(input("Enter the cost per share: $"))

# Calculate the amount invested
amount_invested = shares * cost_per_share

# Display the results
print("\nStock:", ticker)
print("Number of shares:", shares)
print(f"Cost per share: ${cost_per_share:.2f}")
print(f"Amount invested: ${amount_invested:.2f}")
