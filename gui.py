import customtkinter as ctk
import subprocess
import os

# Set theme
ctk.set_appearance_mode("light")
ctk.set_default_color_theme("blue")

# Create main window
root = ctk.CTk()
root.geometry("400x300")
root.title("Range Fairness Query")

# Function to run C++ program and then the Python script
def run_cpp_and_python():
    min_age = min_age_entry.get()
    max_age = max_age_entry.get()
    epsilon = "0"

    if not all([min_age, max_age]):
        result_label.configure(text="Error: Please enter all values", text_color="red")
        return

    try:
        # Run C++ executable with user input values
        cpp_command = ["./2d_unweighted_pip_final", min_age, min_age, max_age, max_age, epsilon]
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
frame = ctk.CTkFrame(root, fg_color="#F0F0F0", corner_radius=10)
frame.pack(pady=20, padx=20, fill="both", expand=True)

# Title label aligned to the left
title_label = ctk.CTkLabel(frame, text="SELECT Name\nFROM compass", font=("Arial", 18, "bold"), anchor="w", justify="left")
title_label.pack(pady=5, padx=10, anchor="w")

# WHERE statement with inputs in one line
where_frame = ctk.CTkFrame(frame, fg_color="#F0F0F0")
where_frame.pack(pady=5, padx=10, fill="x")

where_text = ctk.CTkLabel(where_frame, text="WHERE", font=("Arial", 18, "bold"))
where_text.pack(side="left", padx=5)

min_age_entry = ctk.CTkEntry(where_frame, placeholder_text="18.0", font=("Arial", 18), width=60, corner_radius=10)
min_age_entry.pack(side="left", padx=5)

where_text_2 = ctk.CTkLabel(where_frame, text="≤ Age", font=("Arial", 18))
where_text_2.pack(side="left")

# Second line for AND condition
and_frame = ctk.CTkFrame(frame, fg_color="#F0F0F0")
and_frame.pack(pady=5, padx=10, fill="x")

and_text = ctk.CTkLabel(and_frame, text="AND Age ≤", font=("Arial", 18))
and_text.pack(side="left")

max_age_entry = ctk.CTkEntry(and_frame, placeholder_text="23.0", font=("Arial", 18), width=60, corner_radius=10)
max_age_entry.pack(side="left", padx=5)

# Calculate Button
calculate_button = ctk.CTkButton(
    frame, text="Run Query", font=("Arial", 16, "bold"),
    corner_radius=10, height=40, fg_color="#337AB7", text_color="white",
    hover_color="#285F8F", command=run_cpp_and_python
)
calculate_button.pack(pady=15)

# Output Label
result_label = ctk.CTkLabel(frame, text="", font=("Arial", 14), wraplength=300)
result_label.pack(pady=10)

# Back Button
back_button = ctk.CTkButton(
    frame, text="Back", font=("Arial", 14),
    corner_radius=10, height=35, fg_color="#337AB7", text_color="white",
    hover_color="#285F8F"
)
back_button.pack(pady=10)

# Run the GUI
root.mainloop()

