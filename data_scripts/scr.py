import csv

input_file = 'compas-scores.csv'           # Replace with your input filename
output_file = 'compas_preprocessed.csv'  # Output filename

with open(input_file, mode='r', newline='', encoding='utf-8') as infile, \
     open(output_file, mode='w', newline='', encoding='utf-8') as outfile:
    
    reader = csv.DictReader(infile)
    fieldnames = ['sex', 'age']  # Only keep these columns
    writer = csv.DictWriter(outfile, fieldnames=fieldnames)
    
    writer.writeheader()  # Write header inside the 'with' block
    
    for row in reader:
        # Create a new row containing only the 'sex' and 'age' fields.
        new_row = { key: row[key] for key in fieldnames }
        writer.writerow(new_row)

print(f"Preprocessing complete. New file saved as {output_file}.")