
num_str=int(input("enter a number of string you want to add in list:"))
str_list=[]
for i in range(num_str):
    string=input("Enter  a  string:")
    str_list.append(string)
print(f"original string is :{str_list}")
len_str=[len(item) for item in str_list]
print(f"length of string is :{len_str}")




'''def calculate_string_lengths(string_list):
    length_list = [len(item) for item in string_list]
    return length_list

# Dynamically create a string list
string_list = []
num_strings = int(input("Enter the number of strings you want to add to the list: "))

for i in range(num_strings):
    string = input(f"Enter string {i+1}: ")
    string_list.append(string)

# Call the function to calculate the length of each string and create a new list
length_list = calculate_string_lengths(string_list)

# Display the original string list and the corresponding lengths
print(f"\nOriginal String List: {string_list}")
print(f"Lengths of Strings: {length_list}")'''

