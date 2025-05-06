# Higher Diploma in Science in Computing (Data Analytics)

**Module:** Programming and Scripting  
**Lecturer:** Andrew Beatty  
**Author:** Elaine R. Cazetta

---

# Project: Iris Dataset Analysis

![Iris Flowers](https://github.com/elainecazetta/private_folder/blob/main/Iris_Flower.png)

---

## About the project:

This project was developed as part of the *Programming and Scripting* module. It aims to analize the famous [Fisher's Iris Dataset](https://archive.ics.uci.edu/dataset/53/iris)[1], apply basic data processing and visualization techniques, and present meaningful insights using Python.

---

## About the dataset:

The [Iris dataset](https://doi.org/10.24432/C56C76) was created in 1936 by the British statistician and biologist Ronald A. Fisher [3], and it is frequently used for testing classification algorithms and practicing basic data analysis because it’s simple, well-structured, and visually easy to understand [2]. It contains 150 records of iris flowers, with the following features measured in centimeters: [1]

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

- `iris.csv` – The dataset used in this analysis  
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
```

---

## Tools & Libraries  

- [`numpy`](https://numpy.org/) – For numerical operations and working with arrays  
- [`pandas`](https://pandas.pydata.org/) – For data manipulation and analysis  
- [`matplotlib`](https://matplotlib.org/) – For creating basic data visualizations like histograms and scatter plots  
- [`seaborn`](https://seaborn.pydata.org/) – Built on top of matplotlib, provides cleaner and more informative visualizations  
- [`scikit-learn`](https://scikit-learn.org/stable/) – Includes the Iris dataset

---

## References  
[1] R. Fisher. Iris, UCI Machine Learning Repository, 1936. Available in: https://doi.org/10.24432/C56C76. [Accessed 04 May 2025]  
[2] Kelleher, Curran. The Iris Dataset Explained. Available in: https://gist.github.com/curran/a08a1080b88344b0c8a7. [Accessed 05 May 2025]  
[3] Iris Flower data set - Wikipedia. Available in: https://en.wikipedia.org/wiki/Iris_flower_data_set. [Accessed 06 May 2025]  
[4] Image, credits: medium.com. Available in: https://3tw.medium.com/scikit-learn-the-iris-dataset-and-machine-learning-the-journey-to-a-new-skill-c8d2f537e087 [Accessed 06 May 2025]  

## End  