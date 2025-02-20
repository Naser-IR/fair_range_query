import csv

input_file = 'compas-scores.csv'              # Your input CSV file
output_file = 'compas2_preprocessed.csv'  # Desired output file

with open(input_file, mode='r', newline='', encoding='utf-8') as infile, \
     open(output_file, mode='w', newline='', encoding='utf-8') as outfile:
    
    reader = csv.DictReader(infile)
    fieldnames = ['sex', 'age']
    writer = csv.DictWriter(outfile, fieldnames=fieldnames)
    writer.writeheader()  # Write header inside the 'with' block
    
    for row in reader:
        # Normalize the sex value to lowercase and remove surrounding whitespace
        sex_value = row['sex'].strip().lower()
        # Convert "male" to 1 and "female" to 0; if neither, keep the original value.
        if sex_value == 'male':
            new_sex = '1'
        elif sex_value == 'female':
            new_sex = '0'
        else:
            new_sex = row['sex']  # fallback if unexpected value
        
        new_row = {
            'sex': new_sex,
            'age': row['age']
        }
        writer.writerow(new_row)

print(f"Preprocessing complete. New file saved as {output_file}.")
