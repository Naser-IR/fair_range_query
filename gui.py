import customtkinter as ctk
import subprocess
import os

# Set theme
ctk.set_appearance_mode("light")  # Can be "dark"
ctk.set_default_color_theme("blue")  # Blue theme

# Create main window
root = ctk.CTk()
root.geometry("400x600")
root.title("Range Fairness")

# Function to run C++ program and then the Python script
def run_cpp_and_python():
    min_x = min_x_entry.get()
    min_y = min_x_entry.get()
    max_x = max_x_entry.get()
    max_y = max_x_entry.get()
    epsilon = "0"

    if not all([min_x, max_x]):
        result_label.configure(text="Error: Please enter all values", text_color="red")
        return

    try:
        # Run C++ executable with user input values
        cpp_command = ["./2d_unweighted_pip_final", min_x, min_y, max_x, max_y, epsilon]
        cpp_process = subprocess.run(cpp_command, capture_output=True, text=True)
        
        # Display C++ output
        result_label.configure(text=cpp_process.stdout, text_color="black")

        # Check if `output.txt` was created (C++ output file)
        if not os.path.exists("output.txt"):
            result_label.configure(text="❌ Error: output.txt was not generated!", text_color="red")
            return

        # Run the Python script after C++ program
        python_command = ["python3", "filter_names.py"]
        python_process = subprocess.run(python_command, capture_output=True, text=True)
        
        # Append Python output to the GUI result
        result_label.configure(text=f"{cpp_process.stdout}\n{python_process.stdout}", text_color="black")

    except Exception as e:
        result_label.configure(text=f"Execution Error: {str(e)}", text_color="red")

# Create main frame
frame = ctk.CTkFrame(root)
frame.pack(pady=20, padx=20, fill="both", expand=True)

# Title label
title_label = ctk.CTkLabel(frame, text="Range Fairness", font=("Arial", 24, "bold"))
title_label.pack(pady=10)

# Create input fields
input_fields = [
    ("Min Value 1", "18.0"), 
    ("Max Value 1", "23.0"), 
]

entries = []
for label_text, default in input_fields:
    label = ctk.CTkLabel(frame, text=label_text, font=("Arial", 16))
    label.pack(pady=5)
    entry = ctk.CTkEntry(frame, placeholder_text=default, font=("Arial", 14))
    entry.pack(pady=5)
    entries.append(entry)

# Assign entries to variables
min_x_entry, max_x_entry = entries

# Calculate Button
calculate_button = ctk.CTkButton(frame, text="Calculate Fair Range", font=("Arial", 16, "bold"),
                                 corner_radius=30, height=40, command=run_cpp_and_python)
calculate_button.pack(pady=15)

# Output Label
result_label = ctk.CTkLabel(frame, text="", font=("Arial", 14), wraplength=300)
result_label.pack(pady=10)

# Back Button
back_button = ctk.CTkButton(frame, text="Back", font=("Arial", 14), corner_radius=30, height=35)
back_button.pack(pady=10)

# Run the GUI
root.mainloop()


# import customtkinter as ctk
# import subprocess

# # Set theme
# ctk.set_appearance_mode("light")  # Can be "dark"
# ctk.set_default_color_theme("blue")  # Blue theme

# # Create main window
# root = ctk.CTk()
# root.geometry("400x600")
# root.title("Range Fairness")

# # Function to run C++ program
# def run_cpp_program():
#     min_x = min_x_entry.get()
#     min_y = min_x_entry.get()
#     max_x = max_x_entry.get()
#     max_y = max_x_entry.get()
#     # epsilon = epsilon_entry.get()
#     epsilon = "0"

#     if not all([min_x, max_x]):
#         result_label.configure(text="Error: Please enter all values", text_color="red")
#         return

#     try:
#         # Run C++ executable with user input values
#         command = ["./2d_unweighted_pip_final", min_x, min_y, max_x, max_y, epsilon]
#         process = subprocess.run(command, capture_output=True, text=True)
        
#         # Display output
#         result_label.configure(text=process.stdout, text_color="black")

#     except Exception as e:
#         result_label.configure(text=f"Execution Error: {str(e)}", text_color="red")

# # Create main frame
# frame = ctk.CTkFrame(root)
# frame.pack(pady=20, padx=20, fill="both", expand=True)

# # Title label
# title_label = ctk.CTkLabel(frame, text="Range Fairness", font=("Arial", 24, "bold"))
# title_label.pack(pady=10)

# # Create input fields
# input_fields = [
#     ("Min Value 1", "18.0"), 
#     # ("Min Value 2", "18.0"), 
#     ("Max Value 1", "23.0"), 
#     # ("Max Value 2", "23.0"), 
#     # ("Epsilon Value", "0.1")
# ]

# entries = []
# for label_text, default in input_fields:
#     label = ctk.CTkLabel(frame, text=label_text, font=("Arial", 16))
#     label.pack(pady=5)
#     entry = ctk.CTkEntry(frame, placeholder_text=default, font=("Arial", 14))
#     entry.pack(pady=5)
#     entries.append(entry)

# # Assign entries to variables
# min_x_entry, max_x_entry = entries

# # Calculate Button
# calculate_button = ctk.CTkButton(frame, text="Calculate Fair Range", font=("Arial", 16, "bold"),
#                                  corner_radius=30, height=40, command=run_cpp_program)
# calculate_button.pack(pady=15)

# # Output Label
# result_label = ctk.CTkLabel(frame, text="", font=("Arial", 14), wraplength=300)
# result_label.pack(pady=10)

# # Back Button
# back_button = ctk.CTkButton(frame, text="Back", font=("Arial", 14), corner_radius=30, height=35)
# back_button.pack(pady=10)

# # Run the GUI
# root.mainloop()


# import tkinter as tk
# from tkinter import messagebox
# import subprocess

# def run_cpp_program():
#     """Runs the C++ fairness optimization program with user inputs."""
#     min_x = min_x_entry.get()
#     min_y = min_y_entry.get()
#     max_x = max_x_entry.get()
#     max_y = max_y_entry.get()

#     if not (min_x and min_y and max_x and max_y):
#         messagebox.showerror("Input Error", "Please enter all min/max values.")
#         return

#     try:
#         # Run the C++ executable with user input values
#         command = ["./2d_unweighted_pip_final", min_x, min_y, max_x, max_y]  # Change if needed
#         process = subprocess.run(command, capture_output=True, text=True)

#         # Display output in the text area
#         output_text.delete("1.0", tk.END)
#         output_text.insert(tk.END, process.stdout)

#         # Show errors (if any)
#         if process.stderr:
#             messagebox.showwarning("Warning", process.stderr)

#     except Exception as e:
#         messagebox.showerror("Execution Error", f"Failed to run C++ program: {str(e)}")

# # GUI Setup
# root = tk.Tk()
# root.title("Fairness Algorithm GUI")
# root.geometry("500x400")

# # Input Labels & Entry Fields
# tk.Label(root, text="Min X:").grid(row=0, column=0)
# tk.Label(root, text="Min Y:").grid(row=1, column=0)
# tk.Label(root, text="Max X:").grid(row=2, column=0)
# tk.Label(root, text="Max Y:").grid(row=3, column=0)

# min_x_entry = tk.Entry(root)
# min_y_entry = tk.Entry(root)
# max_x_entry = tk.Entry(root)
# max_y_entry = tk.Entry(root)

# min_x_entry.grid(row=0, column=1)
# min_y_entry.grid(row=1, column=1)
# max_x_entry.grid(row=2, column=1)
# max_y_entry.grid(row=3, column=1)

# # Run Button
# run_button = tk.Button(root, text="Run Fairness Algorithm", command=run_cpp_program)
# run_button.grid(row=4, column=0, columnspan=2, pady=10)

# # Output Box
# output_text = tk.Text(root, height=10, width=60)
# output_text.grid(row=5, column=0, columnspan=2)

# # Start GUI Loop
# root.mainloop()
