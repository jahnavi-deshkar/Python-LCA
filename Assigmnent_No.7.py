import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the CSV dataset
df = pd.read_csv("sample_data_assignment_07.csv")

# Display the dataset
print("Dataset:")
print(df)

# Line Plot
plt.figure(figsize=(7, 4.5))
plt.plot(df["Student"], df["Python"], marker="o")
plt.title("Python Marks of Students")
plt.xlabel("Student")
plt.ylabel("Python Marks")
plt.grid(True)
plt.show()

# Bar Plot
plt.figure(figsize=(7, 4.5))
plt.bar(df["Student"], df["Maths"])
plt.title("Maths Marks of Students")
plt.xlabel("Student")
plt.ylabel("Maths Marks")
plt.show()

# Scatter Plot
plt.figure(figsize=(7, 4.5))
plt.scatter(df["Maths"], df["Python"], s=70)
plt.title("Maths vs Python Marks")
plt.xlabel("Maths Marks")
plt.ylabel("Python Marks")
plt.grid(True)
plt.show()

# Correlation Matrix and Heatmap
correlation = df[["Maths", "Python", "Attendance"]].corr()
print("Correlation Matrix:")
print(correlation)

plt.figure(figsize=(6.5, 5))
sns.heatmap(correlation, annot=True, cmap="Blues", vmin=-1, vmax=1)
plt.title("Correlation Heatmap")
plt.show()
