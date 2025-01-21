def calculate_interest():
    print("Choose the type of interest calculation:")
    print("1. Simple Interest")
    print("2. Compound Interest")
    
    choice = int(input("Enter your choice (1 or 2): "))
    
    if choice not in [1, 2]:
        print("Invalid choice. Please select 1 or 2.")
        return
    
    # Input values
    principal = float(input("Enter the principal amount (e.g., 1000): "))
    rate = float(input("Enter the annual interest rate (in %): "))
    time = float(input("Enter the time period (in years): "))
    
    if choice == 1:
        # Simple Interest Calculation
        simple_interest = (principal * rate * time) / 100
        total_amount = principal + simple_interest
        print(f"\nSimple Interest: {simple_interest:.2f}")
        print(f"Total Amount after {time} years: {total_amount:.2f}")
    else:
        # Compound Interest Calculation
        n = int(input("Enter the number of times interest is compounded per year: "))
        total_amount = principal * (1 + rate / (100 * n))**(n * time)
        compound_interest = total_amount - principal
        print(f"\nCompound Interest: {compound_interest:.2f}")
        print(f"Total Amount after {time} years: {total_amount:.2f}")

# Run the function
calculate_interest()
