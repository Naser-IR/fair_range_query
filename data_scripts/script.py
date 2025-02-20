import csv

input_file = 'compas-scores.csv'              # Your input CSV file
output_file = 'compas_preprocessedandsorted.csv'  # Desired output file

rows = []

with open(input_file, mode='r', newline='', encoding='utf-8') as infile:
    reader = csv.DictReader(infile)
    for row in reader:
        # Normalize and convert the sex field
        sex_value = row['sex'].strip().lower()
        if sex_value == 'male':
            new_sex = '1'
        elif sex_value == 'female':
            new_sex = '0'
        else:
            new_sex = row['sex']  # fallback if unexpected value
        
        # Build a new dictionary containing only the desired fields.
        # We convert the age field to a number for sorting.
        try:
            age_value = float(row['age'])
        except ValueError:
            # In case age is missing or non-numeric, skip the row.
            continue
        
        new_row = {
            'sex': new_sex,
            'age': age_value
        }
        rows.append(new_row)

# Sort rows by age (ascending order)
rows.sort(key=lambda x: x['age'])

# Write the sorted rows to the output file.
with open(output_file, mode='w', newline='', encoding='utf-8') as outfile:
    fieldnames = ['sex', 'age']
    writer = csv.DictWriter(outfile, fieldnames=fieldnames)
    writer.writeheader()
    for row in rows:
        # If you want to write age as an integer when possible, you can convert it here.
        writer.writerow({
            'sex': row['sex'],
            'age': row['age']
        })

print(f"Preprocessing complete. New file saved as {output_file}.")
