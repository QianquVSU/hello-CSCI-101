TOOL_NAME = "Even or Odd Checker"

def run():
    number = int(input("Enter a whole number: "))

    if number % 2 == 0:
        print(f"{number} is even.")
    else:
        print(f"{number} is odd.")

if __name__ == "__main__":
    run()