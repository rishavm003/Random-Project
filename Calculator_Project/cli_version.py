import sys

def add(x, y): return x + y
def subtract(x, y): return x - y
def multiply(x, y): return x * y
def divide(x, y):
    if y == 0:
        raise ZeroDivisionError("Cannot divide by zero!")
    return x / y

def display_menu():
    print("\n--- CLI CALCULATOR ---")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Exit")

def main():
    while True:
        display_menu()
        choice = input("\nEnter choice (1-5): ").strip()

        if choice == '5':
            print("Goodbye!")
            break

        if choice in ('1', '2', '3', '4'):
            try:
                num1 = float(input("Enter first number: "))
                num2 = float(input("Enter second number: "))
                
                if choice == '1': print(f"{num1} + {num2} = {add(num1, num2)}")
                elif choice == '2': print(f"{num1} - {num2} = {subtract(num1, num2)}")
                elif choice == '3': print(f"{num1} * {num2} = {multiply(num1, num2)}")
                elif choice == '4':
                    try:
                        print(f"{num1} / {num2} = {divide(num1, num2)}")
                    except ZeroDivisionError as e:
                        print(f"Error: {e}")
                
            except ValueError:
                print("Invalid input! Please enter numeric values.")
        else:
            print("Invalid Input! Please choose 1-5.")

if __name__ == "__main__":
    main()
