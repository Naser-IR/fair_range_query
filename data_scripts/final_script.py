#!/usr/bin/env python3
import csv

# Define the file names.
input_filename = 'ncompas_preprocessed_sorted.csv'
output_filename = 'sorted.csv'

# Open the input and output CSV files.
with open(input_filename, newline='') as infile, open(output_filename, 'w', newline='') as outfile:
    # Create a DictReader to parse the CSV input (using comma as the default delimiter).
    reader = csv.DictReader(infile)
    
    # Create a CSV writer for the output file.
    writer = csv.writer(outfile)
    
    # Optionally, write a header row to the output file.
    #writer.writerow(['age', 'age', 'sex'])
    
    # Process each row from the input file.
    for row in reader:
        age = row['age']
        sex = row['sex']
        # Write out the new row with age repeated twice followed by sex.
        writer.writerow([age, age, sex])

print(f"Processed '{input_filename}' and created '{output_filename}'.")
