import pandas as pd
import os

def save_data(data, columns, name):
    file_path = './csv_files/data.csv'
    if os.path.exists(file_path) and os.path.getsize(file_path) > 0:
        # Read the CSV file into a DataFrame
        df = pd.read_csv(file_path)
        # Check if the DataFrame is empty
        if not df.empty:
            # Create a new DataFrame with the provided data and columns
            new_df = pd.DataFrame([data], columns=columns)
            # Append the new DataFrame to the existing one
            df = pd.concat([df, new_df], ignore_index=True)
    else:
        # Create a new DataFrame with the provided data and columns
        df = pd.DataFrame([data], columns=columns)

    # Save the DataFrame to the specified file
    df.to_csv(name, index=False)
