import pandas as pd
import os  # Import for file deletion

def read_age_ranges(filename="output.txt"):
    """Reads age ranges from output.txt"""
    with open(filename, "r") as file:
        lines = file.readlines()
    
    # Extract four numbers and convert them to float
    min_original, max_original, min_fair, max_fair = map(float, lines)
    return min_original, max_original, min_fair, max_fair

def filter_csv(input_csv="ncompas_preprocessed_sorted.csv", output_original="original.csv", output_fair="fair_range.csv", output_file="output.txt"):
    """Reads data.csv and filters names based on age range"""
    min_original, max_original, min_fair, max_fair = read_age_ranges(output_file)

    # Load CSV with comma delimiter
    df = pd.read_csv(input_csv, delimiter=",")

    # Normalize column names (strip spaces, lowercase)
    df.columns = df.columns.str.strip().str.lower()

    # Debug: Print found column names
    print("✅ Found columns in CSV:", df.columns.tolist())

    # Check for required columns
    if "name" not in df.columns or "age" not in df.columns:
        print("❌ Error: CSV file must contain 'name' and 'age' columns.")
        return

    # Convert "age" column to numeric (handle errors)
    df["age"] = pd.to_numeric(df["age"], errors='coerce')

    # Filter for original range (18 ≤ Age ≤ 23)
    df_original = df[(df["age"] >= min_original) & (df["age"] <= max_original)]
    df_original[["name", "age"]].to_csv(output_original, index=False, sep=",")

    # Filter for fair range (19 ≤ Age ≤ 22)
    df_fair = df[(df["age"] >= min_fair) & (df["age"] <= max_fair)]
    df_fair[["name", "age"]].to_csv(output_fair, index=False, sep=",")

    print(f"✅ Files created: {output_original}, {output_fair}")

    # 🚀 Delete output.txt after successful execution
    try:
        os.remove(output_file)
        print(f"🗑️ Deleted file: {output_file}")
    except Exception as e:
        print(f"⚠️ Error deleting {output_file}: {e}")

# Run the filtering function
filter_csv("ncompas_preprocessed_sorted.csv")



# import pandas as pd

# def read_age_ranges(filename="output.txt"):
#     """Reads age ranges from output.txt"""
#     with open(filename, "r") as file:
#         lines = file.readlines()
    
#     # Extract four numbers and convert them to float
#     min_original, max_original, min_fair, max_fair = map(float, lines)
#     return min_original, max_original, min_fair, max_fair

# def filter_csv(input_csv="ncompas_preprocessed_sorted.csv", output_original="original.csv", output_fair="fair_range.csv"):
#     """Reads data.csv and filters names based on age range"""
#     min_original, max_original, min_fair, max_fair = read_age_ranges()

#     # Load CSV with tab delimiter
#     df = pd.read_csv(input_csv, delimiter=",")

#     # Normalize column names (strip spaces, lowercase)
#     df.columns = df.columns.str.strip().str.lower()

#     # Debug: Print found column names
#     print("✅ Found columns in CSV:", df.columns.tolist())

#     # Check for required columns
#     if "name" not in df.columns or "age" not in df.columns:
#         print("❌ Error: CSV file must contain 'name' and 'age' columns.")
#         return

#     # Convert "age" column to numeric (handle errors)
#     df["age"] = pd.to_numeric(df["age"], errors='coerce')

#     # Filter for original range (18 ≤ Age ≤ 23)
#     df_original = df[(df["age"] >= min_original) & (df["age"] <= max_original)]
#     df_original[["name", "age"]].to_csv(output_original, index=False, sep=",")

#     # Filter for fair range (19 ≤ Age ≤ 22)
#     df_fair = df[(df["age"] >= min_fair) & (df["age"] <= max_fair)]
#     df_fair[["name", "age"]].to_csv(output_fair, index=False, sep=",")

#     print(f"✅ Files created: {output_original}, {output_fair}")

# # Run the filtering function
# filter_csv("ncompas_preprocessed_sorted.csv")








# import pandas as pd

# # Step 1: Read the output.txt file to get age ranges
# def read_age_ranges(filename="output.txt"):
#     with open(filename, "r") as file:
#         lines = file.readlines()

#     # Extracting the four numbers from the file
#     min_original, max_original, min_fair, max_fair = map(float, lines)
#     return min_original, max_original, min_fair, max_fair

# # Step 2: Filter names based on age range
# def filter_csv(input_csv="ncompas_preprocessed_sorted.csv", output_original="original.csv", output_fair="fair_range.csv"):
#     # Read age ranges from output.txt
#     min_original, max_original, min_fair, max_fair = read_age_ranges()

#     # Load the CSV file
#     df = pd.read_csv(input_csv, delimiter="\t")  # Assuming the file is tab-separated

#     # Ensure the CSV has the required columns
#     if "name" not in df.columns or "age" not in df.columns:
#         print("Error: CSV file must contain 'name' and 'age' columns.")
#         return

#     # Convert Age column to numeric (handling potential string values)
#     df["age"] = pd.to_numeric(df["age"], errors='coerce')

#     # Filter for original range (18 ≤ Age ≤ 23)
#     df_original = df[(df["age"] >= min_original) & (df["age"] <= max_original)]
#     df_original[["name", "age"]].to_csv(output_original, index=False)

#     # Filter for fair range (19 ≤ Age ≤ 22)
#     df_fair = df[(df["age"] >= min_fair) & (df["age"] <= max_fair)]
#     df_fair[["name", "age"]].to_csv(output_fair, index=False)

#     print(f"✅ Files created: {output_original}, {output_fair}")

# # Run the filtering function
# filter_csv("ncompas_preprocessed_sorted.csv")  # Change "data.csv" if your filename is different
