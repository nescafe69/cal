def calculate_simple_interest(principal, rate, time):
    """
    Calculates simple interest based on principal, rate per annum, and time in years.
    """
    interest = (principal * rate * time) / 100
    return interest

if __name__ == "__main__":
    print("--- Simple Interest Calculator ---")
    
    try:
        p = float(input("Enter Principal Amount: "))
        r = float(input("Enter Rate of Interest (%): "))
        t = float(input("Enter Time Period (years): "))

        si = calculate_simple_interest(p, r, t)
        total_amount = p + si

        print(f"\nSimple Interest: {si}")
        print(f"Total Amount: {total_amount}")
        
    except ValueError:
        print("Invalid input! Please enter numeric values.")
