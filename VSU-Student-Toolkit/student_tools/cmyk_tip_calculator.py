TOOL_NAME = "Tip Calculator"

def run():
    print("Welcome to the Tip Calculator!")
    bill = float(input("Enter the total bill amount: $"))
    tip_percent = float(input("Enter tip percentage (e.g., 15, 18, 20): "))
    
    tip_amount = bill * (tip_percent / 100)
    total_bill = bill + tip_amount
    
    print(f"\nTip Amount: ${tip_amount:.2f}")
    print(f"Total Bill (including tip): ${total_bill:.2f}")

