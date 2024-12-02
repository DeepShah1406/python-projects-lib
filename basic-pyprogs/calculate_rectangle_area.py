def calculate_rectangle_area(length, breadth):
    return length * breadth

def calculate_square_area(length):
    return length * length

def calculate_circle_area(radius):
    return 3.14159 * radius * radius

def main():
    while True:
        print("\nMenu:")
        print("1. Calculate area of Rectangle")
        print("2. Calculate area of Square")
        print("3. Calculate area of Circle")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            length = float(input("Enter length of the rectangle: "))
            breadth = float(input("Enter breadth of the rectangle: "))
            area = calculate_rectangle_area(length, breadth)
            print("Area of Rectangle:", area)
        elif choice == '2':
            length = float(input("Enter length of the square: "))
            area = calculate_square_area(length)
            print("Area of Square:", area)
        elif choice == '3':
            radius = float(input("Enter radius of the circle: "))
            area = calculate_circle_area(radius)
            print("Area of Circle:", area)
        elif choice == '4':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please enter a valid option.")

if __name__ == "__main__":
    main()
