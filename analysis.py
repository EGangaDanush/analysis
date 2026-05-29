import pandas as pd

df = pd.read_csv("students.csv")

df["Average"] = (
    df["Math"] +
    df["Science"] +
    df["English"]
) / 3

print("\nStudent Averages")
print(df[["Name", "Average"]])

top_student = df.loc[df["Average"].idxmax()]

print("\nTop Student")
print(top_student["Name"])
print("Average:", round(top_student["Average"], 2))

print("\nStatistics")
print(df.describe())
