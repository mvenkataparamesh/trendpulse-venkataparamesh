import pandas as pd

# load json (change date if needed)
df = pd.read_json("data/trends_20260408.json")

print("Initial rows:", len(df))

# removing duplicates
df = df.drop_duplicates(subset="post_id")
print("After duplicates:", len(df))

# removing missing values
df = df.dropna(subset=["post_id", "title", "score"])
print("After removing nulls:", len(df))

# fixing types
df["score"] = df["score"].astype(int)
df["num_comments"] = df["num_comments"].astype(int)

# removing low score stories
df = df[df["score"] >= 5]
print("After low score filter:", len(df))

# cleaning titles (sometimes extra spaces exist)
df["title"] = df["title"].str.strip()

# saving cleaned data
df.to_csv("data/trends_clean.csv", index=False)

print("\nSaved cleaned csv file")

# showing category count
print("\nStories per category:")
print(df["category"].value_counts())