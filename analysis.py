# Author: Elaine Cazetta
# Description: This program is part of the Iris Dataset Analysis Project.
# It loads the Iris dataset, saves it as a CSV file, and generates a summary 
# of each variable, saving the results to a text file.
# Module: Programming and Scripting
# Lecturer: Andrew Beatty
# Institution: Atlantic Technological University
# Year: 2025

# Adding the Iris Dataset to my repository:
from sklearn.datasets import load_iris
import pandas as pd

# Load the Iris dataset
iris = load_iris()

# Create a DataFrame
df = pd.DataFrame(data=iris.data, columns=iris.feature_names)
df['species'] = iris.target

# Save to CSV
df.to_csv('iris.csv', index=False)

# Create a summary using the describe() function
summary = df.describe()

# Save the summary to a text file
with open('summary.txt', 'w') as f:
    f.write("Summary of Each Variable in the Iris Dataset\n")
    f.write(summary.to_string())  # Converts the summary dataframe into a string

