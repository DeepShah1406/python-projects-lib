import tkinter as tk

def calculate_net_salary():
    # Retrieve values from textboxes
    employee_type = employee_type_entry.get()
    basic_salary = float(basic_salary_entry.get())

    # Calculate net salary based on the employee's role
    hra = 0.10 * basic_salary
    da = 0.20 * basic_salary
    pf = 0.12 * basic_salary

    net_salary = basic_salary + hra + da - pf

    # Display the result in the label
    result_label.config(text=f"Net Salary for {employee_type}: {net_salary}")

# Create the main application window
app = tk.Tk()
app.title("Net Salary Calculator")

# Create and place widgets (textbox, button, label)
employee_type_label = tk.Label(app, text="Enter the type of employee:")
employee_type_label.pack()

employee_type_entry = tk.Entry(app)
employee_type_entry.pack()

basic_salary_label = tk.Label(app, text="Enter the basic salary:")
basic_salary_label.pack()

basic_salary_entry = tk.Entry(app)
basic_salary_entry.pack()

calculate_button = tk.Button(app, text="Calculate Net Salary", command=calculate_net_salary)
calculate_button.pack()

result_label = tk.Label(app, text="")
result_label.pack()

# Start the Tkinter event loop
app.mainloop()
