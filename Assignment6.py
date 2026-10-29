
import pandas as pd

# Create dataset using your given data
data = {
    "Name": ["ABC", "XYZ", "PQR", "STU"],
    "Marks": [85, None, 72, 90],
    "City": ["Pune", "Mumbai", "Nashik", "Jalgaon"],
    "Remarks": ["Good", "Average", "Excellent", "Average"]
}

df = pd.DataFrame(data)

# Display original dataset
print("Original Dataset:")
print(df)

# Display first five rows
print("\nFirst Five Rows:")
print(df.head())

# Display dataset information
print("\nDataset Information:")
df.info()

# Display statistical summary
print("\nStatistical Summary:")
print(df.describe())

# Check missing values
print("\nMissing Values:")
print(df.isnull().sum())

# Fill missing marks with mean
df["Marks"] = df["Marks"].fillna(df["Marks"].mean())

# Identify duplicate rows
print("\nDuplicate Records:")
print(df[df.duplicated()])

# Remove duplicate rows
df = df.drop_duplicates()

# Drop the irrelevant Remarks column
df = df.drop(columns=["Remarks"])

# Select required columns using loc[]
selected_data = df.loc[:, ["Name", "Marks", "City"]]

# Filter students scoring above 80
filtered_data = selected_data.loc[selected_data["Marks"] > 80]

# Display cleaned dataset
print("\nCleaned Dataset:")
print(selected_data)

# Display filtered records
print("\nStudents Scoring Above 80:")
print(filtered_data)

# Save cleaned dataset
selected_data.to_csv("cleaned_data.csv", index=False)

print("\nCleaned dataset saved successfully!")
