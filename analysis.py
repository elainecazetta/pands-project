# Author: Elaine Cazetta
# Description: This program is part of the Iris Dataset Analysis Project.
# It loads the Iris dataset, saves it as a CSV file, generates a summary 
# of each variable saving the results to a text file,
# outputs histograms, scatterplots and performs other analysis. 
# Module: Programming and Scripting
# Lecturer: Andrew Beatty
# Institution: Atlantic Technological University
# Year: 2025

# Imports:
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import load_iris

# Load the Iris dataset
iris = load_iris()

# Create a DataFrame
df = pd.DataFrame(data=iris.data, columns=iris.feature_names)
df['species'] = iris.target

# Save the dataset to a CSV file
df.to_csv('iris.csv', index=False)

# Create a summary using the describe() function
# The summary has the following information: count, mean, standard
# deviation, min, 25%, 50% and 75% percentiles, and max.
summary = df.describe()

# Save the summary to a text file
with open('summary.txt', 'w') as f:
    f.write("Summary of Each Variable in the Iris Dataset\n")
    f.write(summary.to_string())  # Converts the summary dataframe into a string

# Creating and saving histograms of each variable to png files:
# Histogram: Sepal Length
plt.figure()
plt.hist(df['sepal length (cm)'], bins=15, edgecolor='black')
plt.title('Histogram of Sepal Length')
plt.xlabel('Sepal Length (cm)')
plt.ylabel('Frequency')
plt.grid()
plt.savefig('fig1_hist_sepal_length.png')
plt.close()

# Histogram: Sepal Width
plt.figure()
plt.hist(df['sepal width (cm)'], bins=15, edgecolor='black')
plt.title('Histogram of Sepal Width')
plt.xlabel('Sepal Width (cm)')
plt.ylabel('Frequency')
plt.grid()
plt.savefig('fig2_hist_sepal_width.png')
plt.close()

# Histogram: Petal Length
plt.figure()
plt.hist(df['petal length (cm)'], bins=15, edgecolor='black')
plt.title('Histogram of Petal Length')
plt.xlabel('Petal Length (cm)')
plt.ylabel('Frequency')
plt.grid()
plt.savefig('fig3_hist_petal_length.png')
plt.close()

# Histogram: Petal Width
plt.figure()
plt.hist(df['petal width (cm)'], bins=15, edgecolor='black')
plt.title('Histogram of Petal Width')
plt.xlabel('Petal Width (cm)')
plt.ylabel('Frequency')
plt.grid()
plt.savefig('fig4_hist_petal_width.png')
plt.close()

# Creating and saving scatter plots for each pair
# of variables grouped by species:
# Define colors and labels
colors = ["dodgerblue", "darkorange", "mediumvioletred"]
labels = iris.target_names

# Scatter plot: Sepal Length vs Sepal Width
plt.figure(figsize=(8, 6))
for i in range(3):
    subset = df[df['species'] == i]
    plt.scatter(subset["sepal length (cm)"], subset["sepal width (cm)"],
                color=colors[i], label=labels[i])
plt.xlabel("Sepal Length (cm)")
plt.ylabel("Sepal Width (cm)")
plt.title("Sepal Length vs Sepal Width")
plt.grid()
plt.legend()
plt.savefig("fig5_sepal_scatter_plot.png")
plt.close()

# Scatter plot: Petal Length vs Petal Width
plt.figure(figsize=(8, 6))
for i in range(3):
    subset = df[df['species'] == i]
    plt.scatter(subset["petal length (cm)"], subset["petal width (cm)"],
                color=colors[i], label=labels[i])
plt.xlabel("Petal Length (cm)")
plt.ylabel("Petal Width (cm)")
plt.title("Petal Length vs Petal Width")
plt.grid()
plt.legend()
plt.savefig("fig6_petal_scatter_plot.png")
plt.close()