'''
Take in the following three values from the user:
    - investment amount
    - interest rate in percentage
    - number of years to invest

Print the future values to the console.

'''
# simple formula found on google
# A = P(1 + rt)

print("This application calculates future investment value based on initial principal, interest rate, and time.")
initial_principal = float(input("Enter initial principal amount: "))
interest_rate = float(input("Enter interest rate in percentage: ")) / 100
time_in_years = float(input("Enter number of years to invest: "))

final_amount = initial_principal * (1 + interest_rate * time_in_years)
print(f"Your future investment will be $ {final_amount}")