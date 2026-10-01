import tkinter as tk
from tkinter import messagebox
from student import Student 
from storage import save_student, load_data

def save_data():
    # Retrieve the text typed into the input fields
    name = entry_name.get()
    roll = entry_roll.get()
    std = entry_std.get()
    
    # Basic validation to ensure fields aren't empty
    if name and roll and std:
        s = Student(name, roll, std)
        save_student(s)
        
        # Show a success popup to the user
        messagebox.showinfo("Success", f"Student {name} saved successfully!")
        
        # Clear the input fields for the next entry
        entry_name.delete(0, tk.END)
        entry_roll.delete(0, tk.END)
        entry_std.delete(0, tk.END)
    else:
        messagebox.showwarning("Error", "Please fill in all fields.")

def fetch_data():
    # Calls your existing load function
    load_data()
    messagebox.showinfo("Loaded", "Data loaded successfully! (Check your console for output)")

# 1. Create the main application window
root = tk.Tk()
root.title("Student Management System")
root.geometry("300x300") # Width x Height

# 2. Create and place Labels and Entry (input) fields
tk.Label(root, text="Student Name:").pack(pady=(10, 0))
entry_name = tk.Entry(root)
entry_name.pack(pady=5)

tk.Label(root, text="Roll Number:").pack()
entry_roll = tk.Entry(root)
entry_roll.pack(pady=5)

tk.Label(root, text="Standard (Std):").pack()
entry_std = tk.Entry(root)
entry_std.pack(pady=5)

# 3. Create and place Buttons, linking them to the functions above
btn_save = tk.Button(root, text="Save Student", command=save_data, bg="lightblue")
btn_save.pack(pady=10)

btn_load = tk.Button(root, text="Load Data", command=fetch_data)
btn_load.pack(pady=5)

# 4. Start the GUI event loop
root.mainloop()