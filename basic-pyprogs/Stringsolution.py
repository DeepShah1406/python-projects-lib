def convert_to_uppercase(string):
    return string.upper()

def find_substring(first_string, second_string):
    return second_string in first_string

def reverse_string(string):
    return string[::-1]

def main():
    while True:
        print("\nMenu:")
        print("1. Convert string to uppercase")
        print("2. Check if second string exists in first string")
        print("3. Reverse the string")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            input_string = input("Enter a string: ")
            result = convert_to_uppercase(input_string)
            print("Result:", result)
        elif choice == '2':
            first_string = input("Enter the first string: ")
            second_string = input("Enter the second string: ")
            result = find_substring(first_string, second_string)
            if result:
                print("Second string exists in the first string.")
            else:
                print("Second string does not exist in the first string.")
        elif choice == '3':
            input_string = input("Enter a string: ")
            result = reverse_string(input_string)
            print("Reversed string:", result)
        elif choice == '4':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please enter a valid option.")

if __name__ == "__main__":
    main()
