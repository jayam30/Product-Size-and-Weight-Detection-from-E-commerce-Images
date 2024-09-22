import pandas as pd
import os

# Load the main file (file1)
main_file = pd.read_csv('cfa_1.csv')

# Directory where your 17 file2-like files are stored (replace 'path_to_files' with actual path)
file2_directory = 'files'

# Get a list of all file2-like files in the directory
file2_files = [f for f in os.listdir(file2_directory) if f.endswith('.csv')]

# Loop through each file2 file and merge the data with the main file
for file2_name in file2_files:
    file2_path = os.path.join(file2_directory, file2_name)
    
    # Load each file2 file
    file2 = pd.read_csv(file2_path)
    
    # Merge main_file with current file2 on the 'index' column
    main_file = main_file.merge(file2, on='index', how='left', suffixes=('', '_file2'))

    # Fill missing values in the 'prediction' column using values from the current file2
    main_file['prediction'].fillna(main_file['prediction_file2'], inplace=True)

    # Drop the extra column from file2 after filling
    main_file = main_file.drop(columns=['prediction_file2'])

# Save the updated main file
main_file.to_csv('main_file_filled.csv', index=False)

print("Missing data from all files filled and saved to 'main_file_filled.csv'")
