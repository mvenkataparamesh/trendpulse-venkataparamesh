import pandas as pd
import matplotlib.pyplot as plt
import os

df = pd.read_csv("data/trends_analysed.csv")

# create folder if not exists
if not os.path.exists("outputs"):
    os.makedirs("outputs")

# -------- chart 1 --------
top10 = df.nlargest(10, "score")

plt.figure(figsize=(12, 8))
plt.barh(top10["title"].str[:50], top10["score"])
plt.xlabel("Score", fontsize=14)
plt.ylabel("Title", fontsize=14)
plt.title("Top 10 Stories", fontsize=16)
plt.xticks(fontsize=12)
plt.yticks(fontsize=10)
plt.tight_layout()
plt.savefig("outputs/chart1_top_stories.png", dpi=300)
plt.close()

# -------- chart 2 --------
counts = df["category"].value_counts()

plt.figure(figsize=(10, 6))
counts.plot(kind="bar")
plt.title("Stories per Category", fontsize=16)
plt.xlabel("Category", fontsize=14)
plt.ylabel("Count", fontsize=14)
plt.xticks(fontsize=12, rotation=45)
plt.yticks(fontsize=12)
plt.tight_layout()
plt.savefig("outputs/chart2_categories.png", dpi=300)
plt.close()

# -------- chart 3 --------
plt.figure(figsize=(10, 6))

pop = df[df["is_popular"] == True]
not_pop = df[df["is_popular"] == False]

plt.scatter(pop["score"], pop["num_comments"], label="Popular")
plt.scatter(not_pop["score"], not_pop["num_comments"], label="Not Popular")

plt.xlabel("Score", fontsize=14)
plt.ylabel("Comments", fontsize=14)
plt.title("Score vs Comments", fontsize=16)
plt.legend(fontsize=12)
plt.xticks(fontsize=12)
plt.yticks(fontsize=12)
plt.tight_layout()
plt.savefig("outputs/chart3_scatter.png", dpi=300)
plt.close()

# -------- dashboard --------
fig, axs = plt.subplots(1, 3, figsize=(18, 6))

axs[0].barh(top10["title"].str[:30], top10["score"])
axs[0].set_title("Top Stories", fontsize=14)
axs[0].tick_params(axis='both', which='major', labelsize=10)

counts.plot(kind="bar", ax=axs[1])
axs[1].set_title("Categories", fontsize=14)
axs[1].tick_params(axis='both', which='major', labelsize=10)
axs[1].tick_params(axis='x', rotation=45)

axs[2].scatter(df["score"], df["num_comments"])
axs[2].set_title("Scatter", fontsize=14)
axs[2].tick_params(axis='both', which='major', labelsize=10)

plt.suptitle("TrendPulse Dashboard", fontsize=16)
plt.tight_layout()
plt.savefig("outputs/dashboard.png", dpi=300)
plt.close()

print("All charts saved successfully")