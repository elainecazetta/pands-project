# Author: Elaine R. Cazetta
# Description: This script is part of the Iris Dataset Analysis 
# Project for the Programming and Scripting module. It performs 
# basic data analysis using the Iris dataset, including:
# - Exporting the dataset to CSV format
# - Generating summary statistics
# - Creating histograms for each feature
# - Visualising relationships between features using scatter plots
# - Exploring differences between species with box plots
# - Displaying feature correlations using a heatmap
# - Visualising relationships between features using a pairplot
# Lecturer: Andrew Beatty
# Institution: Atlantic Technological University
# Year: 2025

#-----------------------------------------------------------------#

# Importing the libraries:
# For data manipulation and analysis
import pandas as pd 
# For numerical operations and working with arrays
import numpy as np 
# For creating data visualizations
import matplotlib.pyplot as plt 
# For creating enhanced and statistical visualizations
import seaborn as sns
# To load the Iris dataset
from sklearn.datasets import load_iris 

#-----------------------------------------------------------------#

# Load the Iris dataset from sklearn
iris = load_iris()

#-----------------------------------------------------------------#

# Create a pandas dataframe with the feature data
df = pd.DataFrame(data=iris.data, columns=iris.feature_names)

# Add a 'species' column to identify each row
df['species'] = iris.target

# Map the numeric species labels (0, 1, 2) to their corresponding 
# species names
species_map = {0: 'setosa', 1: 'versicolor', 2: 'virginica'}
df['species'] = df['species'].replace(species_map)

#-----------------------------------------------------------------#

# Save the full dataset to a CSV file for external use or review
df.to_csv('iris.csv', index=False)

#-----------------------------------------------------------------#

# Generate summary statistics for each numeric feature
# Includes: count, mean, std deviation, min, 25%, 50%, 75%, and 
# max values
summary = df.describe()

# Save the summary to a text file
with open('summary.txt', 'w') as f:
    f.write("Summary of Each Variable in the Iris Dataset\n")
    f.write(summary.to_string()) # Converts summary dataframe into a string

#-----------------------------------------------------------------#

# Plot and save histograms to show distribution of each numeric feature:

# Histogram: Sepal Length
plt.figure()
plt.hist(df['sepal length (cm)'], bins=15, color='dodgerblue', edgecolor='black')
plt.title('Histogram of Sepal Length')
plt.xlabel('Sepal Length (cm)')
plt.ylabel('Frequency')
plt.grid()
plt.savefig('fig01_hist_sepal_length.png')
plt.close()

# Histogram: Sepal Width
plt.figure()
plt.hist(df['sepal width (cm)'], bins=15, color='dodgerblue', edgecolor='black')
plt.title('Histogram of Sepal Width')
plt.xlabel('Sepal Width (cm)')
plt.ylabel('Frequency')
plt.grid()
plt.savefig('fig02_hist_sepal_width.png')
plt.close()

# Histogram: Petal Length
plt.figure()
plt.hist(df['petal length (cm)'], bins=15, color='dodgerblue', edgecolor='black')
plt.title('Histogram of Petal Length')
plt.xlabel('Petal Length (cm)')
plt.ylabel('Frequency')
plt.grid()
plt.savefig('fig03_hist_petal_length.png')
plt.close()

# Histogram: Petal Width
plt.figure()
plt.hist(df['petal width (cm)'], bins=15, color='dodgerblue', edgecolor='black')
plt.title('Histogram of Petal Width')
plt.xlabel('Petal Width (cm)')
plt.ylabel('Frequency')
plt.grid()
plt.savefig('fig04_hist_petal_width.png')
plt.close()

#-----------------------------------------------------------------#

# Create scatter plots for feature pairs, colored by species
# These plots help visualize how species differ based on two features:

# Define colours for each species using a dictionary
colors = {'setosa': 'dodgerblue', 'versicolor': 'darkorange', 
          'virginica': 'mediumvioletred'}

# Scatter Plot: Sepal Length vs Sepal Width
plt.figure(figsize=(8, 6)) # Set the figure size

# Filter the DataFrame by species [18]
for species, color in colors.items():
    subset = df[df['species'] == species]

# Plot Sepal Length vs Sepal Width for each species
    plt.scatter(subset['sepal length (cm)'], subset['sepal width (cm)'],
                label=species, color=color)
    
plt.xlabel("Sepal Length (cm)")
plt.ylabel("Sepal Width (cm)")
plt.title("Sepal Length vs Sepal Width")
plt.grid()
plt.legend()
plt.savefig("fig05_sepal_scatter_plot.png")
plt.close()

# Scatter Plot: Petal Length vs Petal Width
plt.figure(figsize=(8, 6)) # Set the figure size

# Filter the DataFrame by species [18]
for species, color in colors.items():
    subset = df[df['species'] == species]

# Plot Petal Length vs Petal Width for each species
    plt.scatter(subset['petal length (cm)'], subset['petal width (cm)'],
                label=species, color=color)
    
plt.xlabel("Petal Length (cm)")
plt.ylabel("Petal Width (cm)")
plt.title("Petal Length vs Petal Width")
plt.grid()
plt.legend()
plt.savefig("fig06_petal_scatter_plot.png")
plt.close()

#-----------------------------------------------------------------#

# Create box plots to show distribution of each feature grouped by species.
# Helps compare median, range, and outliers among species for each feature:

# Set style to white to remove gridlines
sns.set(style="whitegrid")

# Features to plot
features = ['sepal length (cm)', 'sepal width (cm)', 
            'petal length (cm)', 'petal width (cm)']

# Loop through each feature and save individual plots
for i, feature in enumerate(features, start=7):  # Start numbering at figure 7
    plt.figure(figsize=(8, 6))  # Create a new figure

    # Create boxplot for the current feature grouped by species
    sns.boxplot(x='species', y=feature, data=df,
                hue='species', legend=False,
                palette={'setosa': 'dodgerblue',
                         'versicolor': 'darkorange',
                         'virginica': 'mediumvioletred'})

    # Add title, axis labels and gridelines
    plt.title(f'Box Plot of {feature} by Species')
    plt.xlabel('')
    plt.ylabel(feature)
    plt.grid()

    # Save the plot as a PNG file
    filename = f'fig{i:02d}_boxplot_{feature.replace(" ", "_")}_by_species.png'
    plt.savefig(filename)
    plt.close()

#-----------------------------------------------------------------#

# Create heatmaps to show correlations between numeric features:

# Loop through each species and create individual heatmaps
species_list = df['species'].unique()

for i, species in enumerate(species_list, start=11): # Start figure at 11
    subset = df[df['species'] == species].drop('species', axis=1) # Drop species column
    corr = subset.corr()  # Calculate correlation matrix

    # Create a new figure
    plt.figure(figsize=(8, 5))

    # Plot the heatmap
    sns.heatmap(corr, annot=True, cmap='BuPu', fmt=".2f",
                square=True, cbar=True)

    # Set title and rotate x-axis labels
    plt.title(f'{species.capitalize()} - Feature Correlation', fontsize=12)
    plt.xticks(rotation=45)
    plt.tight_layout() # Adjust spacing between plots

    # Save the figure
    filename = f'fig{i}_heatmap_{species}_correlation.png'
    plt.savefig(filename)
    plt.close()

#-----------------------------------------------------------------#

# Create pairplots to show relationships between variables:

# Set style to white to remove gridlines
sns.set_style("white")

# Create a pairplot to show relationships between all numeric 
# variables, grouped by species
sns.pairplot(df, hue="species", palette={'setosa': 'dodgerblue',
                      'versicolor': 'darkorange',
                      'virginica': 'mediumvioletred'})

# Add a title slightly above the plot
plt.suptitle("Pairplot of Iris Dataset", y=1.02)

# Save the figure
plt.savefig("fig14_pairplot_iris_dataset.png")
plt.close()

#-----------------------------------------------------------------#