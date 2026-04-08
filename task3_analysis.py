import pandas as pd
import numpy as np

df = pd.read_csv("data/trends_clean.csv")

print("Data shape:", df.shape)
print("\nFirst few rows:")
print(df.head())

# basic averages
avg_score = df["score"].mean()
avg_comments = df["num_comments"].mean()

print("\nAverage score:", avg_score)
print("Average comments:", avg_comments)

# using numpy
scores = df["score"].values

print("\n--- Stats ---")
print("Mean:", np.mean(scores))
print("Median:", np.median(scores))
print("Std Dev:", np.std(scores))
print("Max:", np.max(scores))
print("Min:", np.min(scores))

# category with most stories
top_cat = df["category"].value_counts().idxmax()
print("\nMost stories in:", top_cat)

# most commented story
top_story = df.loc[df["num_comments"].idxmax()]
print("\nMost commented story:")
print(top_story["title"], "-", top_story["num_comments"])

# adding new columns
df["engagement"] = df["num_comments"] / (df["score"] + 1)
df["is_popular"] = df["score"] > avg_score

# saving file
df.to_csv("data/trends_analysed.csv", index=False)

print("\nSaved analysed file")