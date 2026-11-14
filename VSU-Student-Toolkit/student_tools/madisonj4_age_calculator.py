TOOL_NAME = "Age in Days Calculator"

def run():
    print("Welcome to the Age in Days Calculator!")

    age = int(input("Enter your age in years: "))

    days = age * 365

    print("You are approximately", days, "days old!")
