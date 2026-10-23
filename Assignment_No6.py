import re

def check_allowed_chars_regex(text):
    pattern = r'^[a-zA-Z0-9]+$'
    if re.match(pattern, text):
        return True
    return False

if check_allowed_chars_regex(user_input):
    print(f"'{user_input}' contains ONLY allowed characters (a-z, A-Z, 0-9).")
else:
    print(f"'{user_input}' contains invalid or special characters.")

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("sample_data_assignment_07.csv")
print("Dataset:")
print(df)

plt.figure(figsize=(7, 4.5))
plt.plot(df["Student"], df["Python"], marker="o")
plt.title("Python Marks of Students")
plt.xlabel("Student")
plt.ylabel("Python Marks")
plt.grid(True)
plt.show()

plt.figure(figsize=(7, 4.5))
plt.bar(df["Student"], df["Maths"], color='skyblue')
plt.title("Maths Marks of Students")
plt.xlabel("Student")
plt.ylabel("Maths Marks")
plt.show()

plt.figure(figsize=(7, 4.5))
plt.scatter(df["Maths"], df["Python"], s=70, color='purple')
plt.title("Maths vs Python Marks")
plt.xlabel("Maths Marks")
plt.ylabel("Python Marks")
plt.grid(True)
plt.show()

correlation = df[["Maths", "Python", "Attendance"]].corr()
print("\nCorrelation Matrix:")
print(correlation)

plt.figure(figsize=(6.5, 5))
sns.heatmap(correlation, annot=True, cmap="Blues", vmin=-1, vmax=1)
plt.title("Correlation Heatmap")
plt.show()
