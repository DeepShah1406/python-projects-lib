class MathOperations:
    def addition(self, num1, num2):
        return num1 + num2

    def subtraction(self, num1, num2):
        return num1 - num2

    def multiplication(self, num1, num2):
        return num1 * num2

    def division(self, num1, num2):
        if num2 != 0:
            return num1 / num2
        else:
            return "Cannot divide by zero."

    def integer_division(self, num1, num2):
        if num2 != 0:
            return num1 // num2
        else:
            return "Cannot divide by zero."


def main():
    math_ops = MathOperations()

    while True:
        print("\nMenu:")
        print("1. Addition")
        print("2. Subtraction")
        print("3. Multiplication")
        print("4. Division")
        print("5. Integer Division")
        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
            result = math_ops.addition(num1, num2)
            print("Result:", result)
        elif choice == '2':
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
            result = math_ops.subtraction(num1, num2)
            print("Result:", result)
        elif choice == '3':
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
            result = math_ops.multiplication(num1, num2)
            print("Result:", result)
        elif choice == '4':
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
            result = math_ops.division(num1, num2)
            print("Result:", result)
        elif choice == '5':
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
            result = math_ops.integer_division(num1, num2)
            print("Result:", result)
        elif choice == '6':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please enter a valid option.")


if __name__ == "__main__":
    main()
