# Import Module
import tkinter as tk
 
# create root window
root = tk.Tk()
 
# root window title and dimension
root.title("Welcome to First GUI Application")
# Set geometry (widthxheight)
root.geometry('350x200')

l1 = tk.Label(root, text="First Label")
l1.pack()

# Entry widget
entry = tk.Entry(root)
entry.pack()

# Button widget
button = tk.Button(root, text="Click Me!")
button2 = tk.Button(root, text="I am Feeling Lucky!")
button.pack()
button2.pack()

#Check Button Widget
checkbutton = tk.Checkbutton(root, text = "ckbtn1")
checkbutton2 = tk.Checkbutton(root, text = "ckbtn2")
checkbutton.pack(),checkbutton2.pack()

#Listbox Widget
listbox = tk.Listbox(root)
listbox.insert(1,"abc")
listbox.insert(2,"def")
listbox.pack()













# all widgets will be here
# Execute Tkinter
root.mainloop()
