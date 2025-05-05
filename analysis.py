# Author: Elaine Cazetta

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
