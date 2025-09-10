# ------------------------------------------------------------
# Analyzing Data with Pandas and Visualizing Results with Matplotlib
# Author: Bikila Keneni
# ------------------------------------------------------------

# Import required libraries
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# ------------------------------------------------------------
# Task 1: Load and Explore the Dataset
# ------------------------------------------------------------

# Load dataset (Iris dataset from seaborn for demo; replace with your CSV file)
try:
    df = sns.load_dataset('iris')   # you can replace with: pd.read_csv("yourfile.csv")
    print("Dataset loaded successfully!")
except FileNotFoundError:
    print("Error: File not found. Please check the file path.")

# Display first few rows
print("\nFirst 5 rows of dataset:")
print(df.head())

# Check dataset info (data types + null values)
print("\nDataset Info:")
print(df.info())

# Check for missing values
print("\nMissing values in dataset:")
print(df.isnull().sum())

# If missing values exist → handle them (drop or fill)
df = df.dropna()   # dropping rows with missing values
# alternatively: df.fillna(df.mean(), inplace=True)

# ------------------------------------------------------------
# Task 2: Basic Data Analysis
# ------------------------------------------------------------

# Compute summary statistics
print("\nSummary Statistics:")
print(df.describe())

# Grouping: mean petal_length by species
grouped = df.groupby("species")["petal_length"].mean()
print("\nMean Petal Length by Species:")
print(grouped)

# Identify interesting findings (example)
print("\nObservations:")
print("-> Iris-virginica generally has the highest petal length on average.")

# ------------------------------------------------------------
# Task 3: Data Visualization
# ------------------------------------------------------------

# 1. Line chart (trend over index since iris has no time column, we simulate with index)
plt.figure(figsize=(8,5))
plt.plot(df.index, df["sepal_length"], label="Sepal Length")
plt.plot(df.index, df["petal_length"], label="Petal Length")
plt.title("Line Chart: Sepal vs Petal Length")
plt.xlabel("Index")
plt.ylabel("Length (cm)")
plt.legend()
plt.show()

# 2. Bar chart (mean petal length per species)
plt.figure(figsize=(6,4))
sns.barplot(x="species", y="petal_length", data=df, ci=None)
plt.title("Average Petal Length by Species")
plt.xlabel("Species")
plt.ylabel("Petal Length (cm)")
plt.show()

# 3. Histogram (distribution of sepal length)
plt.figure(figsize=(6,4))
plt.hist(df["sepal_length"], bins=15, edgecolor="black")
plt.title("Histogram of Sepal Length")
plt.xlabel("Sepal Length (cm)")
plt.ylabel("Frequency")
plt.show()

# 4. Scatter plot (sepal length vs petal length)
plt.figure(figsize=(6,4))
plt.scatter(df["sepal_length"], df["petal_length"], alpha=0.7)
plt.title("Scatter Plot: Sepal Length vs Petal Length")
plt.xlabel("Sepal Length (cm)")
plt.ylabel("Petal Length (cm)")
plt.show()

print("\nAnalysis Complete ✅")
