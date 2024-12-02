'''m1={1,2,3,4}
m2={3,4,5,6}
m1.union(m2)
m1.update(m2)
print(m1)
def  remove_list(list_item):
    return list_item.pop(-1)
k=["mayank","mzx","yellow"]
remove_list(k)
print(remove_list(k))
DaysA = set(["Mon","Tue","Wed"])
DaysB = set(["Wed","Thu","Fri","Sat","Sun"])
AllDays = DaysA - DaysB 
#AllDays = DaysA & DaysB
un=DaysA.intersection(DaysB)
print(AllDays)
DaysA = set(["Mon","Tue","Wed"])
DaysB = set(["Mon","Tue","Wed","Thu","Fri","Sat","Sun"])
SubsetRes = DaysA <= DaysB
SupersetRes = DaysB >= DaysA
print(SubsetRes)    
print(SupersetRes)
def greet(name, greeting):
    message = f"{greeting}, {name}!"
    return message

greeting_message = greet(name="Alice", greeting="Hello")
print(greeting_message)  # Output: Hello, Alice!'''
import time

def greet():
    print("Hello! I am Jarvis. How can I assist you today?")

def execute_command(command):
    if "time" in command:
        current_time = time.strftime("%H:%M:%S")
        print(f"The current time is {current_time}")
    elif "date" in command:
        current_date = time.strftime("%Y-%m-%d")
        print(f"Today's date is {current_date}")
    elif "greet" in command:
        print("Hello! How can I help you?")
    elif "exit" in command or "quit" in command:
        print("Goodbye!")
        exit()
    else:
        print("I'm sorry, I don't understand that command.")

if __name__ == "__main__":
    greet()

    while True:
        user_input = input("Your command: ").lower()
        execute_command(user_input)



