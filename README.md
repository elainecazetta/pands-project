# Higher Diploma in Science in Computing (Data Analytics)
**Module:** Programming and Scripting
**Lecturer:** Andrew Beatty

---

# Project: Iris Dataset Analysis
**About the project:**

---

This project was developed as part of the *Programming and Scripting* module. It aims to analize the famous [Fisher's Iris Dataset](https://github.com/elainecazetta/pands-project/blob/main/iris.csv), apply basic data processing and visualization techniques, and present meaningful insights using Python.

---

**About the dataset:**

The [Iris dataset](https://doi.org/10.24432/C56C76) was created in 1936 by R. A. Fisher, and it is frequently used for testing out machine learning algorithms[2]. It contains 150 records of iris flowers, with the following features measured in centimeters:[1]

- *Sepal length*
- *Sepal width*
- *Petal length*
- *Petal width*

The flowers belong to three species:

- *Iris Setosa*  
- *Iris Versicolor*  
- *Iris Virginica*  

---

## Repository Contents  

- `iris.csv` – The dataset used in this analysis (downloaded from the [UCI ML Repository](https://archive.ics.uci.edu/ml/datasets/iris))  
- `analysis.py` – Python script that:
  - Outputs a summary of each variable to a text file
  - Creates histograms for each feature and saves them as PNGs
  - Generates scatter plots of each feature pair
- `iris_analysis.ipynb` – Jupyter notebook with notes and commentary
- `plots` – Files containing all output charts
- `summary.txt` – Summary statistics for each feature

---

## Requirements  

To run this project, you'll need **Python 3** and the following packages:

```bash
pip install numpy pandas matplotlib seaborn

---

## References  
[1] R. Fisher. Iris, UCI Machine Learning Repository, 1936. Available in: https://doi.org/10.24432/C56C76. [Accessed 05 May 2025]
[2] Kelleher, Curran. The Iris Dataset. Available in: https://gist.github.com/curran/a08a1080b88344b0c8a7. [Accessed 05 May 2025]

**End**
