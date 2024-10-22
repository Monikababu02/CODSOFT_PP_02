# calculator.py

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Error! Division by zero."
    else:
        return a / b

def main():
    print("Simple Calculator")
    while True:
        try:
            num1 = float(input("Enter the first number: "))
            num2 = float(input("Enter the second number: "))
            print("\nSelect operation:")
            print("1. Add")
            print("2. Subtract")
            print("3. Multiply")
            print("4. Divide")
            choice = input("Enter your choice (1/2/3/4): ")

            if choice == '1':
                print(f"The result is: {add(num1, num2)}")
            elif choice == '2':
                print(f"The result is: {subtract(num1, num2)}")
            elif choice == '3':
                print(f"The result is: {multiply(num1, num2)}")
            elif choice == '4':
                print(f"The result is: {divide(num1, num2)}")
            else:
                print("Invalid choice. Please select 1/2/3/4.")

            cont = input("\nDo you want to perform another calculation? (yes/no): ").lower()
            if cont != 'yes':
                print("Exiting the calculator.")
                break
        except ValueError:
            print("Invalid input! Please enter numbers only.")

if __name__ == "__main__":
    main()
