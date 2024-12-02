class largest_value:
  
 
    def __init__(self, v1, v2, v3):
        self.v1 = v1
        self.v2 = v2
        self.v3 = v3

    def find_largest(self):       
        largest = max(self.v1, self.v2, self.v3)
        return largest


v1 = float(input("Enter the first value: "))
v2 = float(input("Enter the second value: "))
v3 = float(input("Enter the third value: "))

finder = largest_value(v1, v2, v3)
largest_value = finder.find_largest()

print(f"The largest value is: {largest_value}")

