"""
class Student:
    def __init__(self, s_id, s_name, sub1, sub2):
        self.s_id = s_id
        self.s_name = s_name
        self.sub1 = sub1
        self.sub2 = sub2

    def calculate_per(self):
        total = self.sub1 + self.sub2
        max_marks = 200  # Assuming both sub1 and sub2 are out of 100
        per = (total / max_marks) * 100
        return total, per

name = input("ENTER NAME OF STUDENT: ")
id = input("ENTER ID OF STUDENT: ")
sub_1 = float(input("ENTER MARKS OF SUB1: "))
sub_2 = float(input("ENTER MARKS OF SUB2: "))

result = Student(id, name, sub_1, sub_2)
total_marks, percentage = result.calculate_per()

print(f"STUDENT NAME: {name}")
print(f"STUDENT ID: {id}")
print(f"SUB1 MARKS: {sub_1}")
print(f"SUB2 MARKS: {sub_2}")
print(f"TOTAL MARKS: {total_marks}")
print(f"PERCENTAGE IS: {percentage}")
"""
import tkinter as tk
from tkinter import messagebox

class Student:
    def __init__(self, s_id, s_name, sub1, sub2):
        self.s_id = s_id
        self.s_name = s_name
        self.sub1 = sub1
        self.sub2 = sub2

    def calculate_per(self):
        total = self.sub1 + self.sub2
        max_marks = 200  # Assuming both sub1 and sub2 are out of 100
        per = (total / max_marks) * 100
        return total, per

def calculate_result():
    name = name_entry.get()
    id = id_entry.get()
    sub_1 = float(sub1_entry.get())
    sub_2 = float(sub2_entry.get())

    result = Student(id, name, sub_1, sub_2)
    total_marks, percentage = result.calculate_per()

    messagebox.showinfo("Result", f"Student Name: {name}\nStudent ID: {id}\nSub1 Marks: {sub_1}\nSub2 Marks: {sub_2}\nTotal Marks: {total_marks}\nPercentage: {percentage}")

# Create the main window
root = tk.Tk()
root.title("Student Result Calculator")

# Create labels and entry fields
tk.Label(root, text="Name:").grid(row=0, column=0)
name_entry = tk.Entry(root)
name_entry.grid(row=0, column=1)

tk.Label(root, text="ID:").grid(row=1, column=0)
id_entry = tk.Entry(root)
id_entry.grid(row=1, column=1)

tk.Label(root, text="Sub1 Marks:").grid(row=2, column=0)
sub1_entry = tk.Entry(root)
sub1_entry.grid(row=2, column=1)

tk.Label(root, text="Sub2 Marks:").grid(row=3, column=0)
sub2_entry = tk.Entry(root)
sub2_entry.grid(row=3, column=1)

# Create a button to calculate result
calculate_button = tk.Button(root, text="Calculate", command=calculate_result)
calculate_button.grid(row=4, column=0, columnspan=2)

root.mainloop()
