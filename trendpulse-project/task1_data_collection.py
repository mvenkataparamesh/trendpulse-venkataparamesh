import requests
import time
import os
import json
from datetime import datetime

# basic urls for hackernews api
top_url = "https://hacker-news.firebaseio.com/v0/topstories.json"
item_url = "https://hacker-news.firebaseio.com/v0/item/{}.json"

headers = {"User-Agent": "TrendPulse/1.0"}

# categories with keywords (kept simple)
cats = {
    "technology": ["ai","software","tech","code","computer","data","cloud","api","gpu","llm"],
    "worldnews": ["war","government","country","president","election","climate","attack","global"],
    "sports": ["nfl","nba","fifa","sport","game","team","player","league","championship"],
    "science": ["research","study","space","physics","biology","discovery","nasa","genome"],
    "entertainment": ["movie","film","music","netflix","game","book","show","award","streaming"]
}

all_data = []   # final list
count = {c: 0 for c in cats}   # tracking count

print("Getting top stories...")

# fetching ids
try:
    r = requests.get(top_url, headers=headers)
    ids = r.json()
except:
    print("Problem fetching ids")
    ids = []

ids = ids[:500]   # only first 500

# looping through stories
for sid in ids:

    print("Checking story:", sid)

    try:
        res = requests.get(item_url.format(sid), headers=headers)
        story = res.json()
    except:
        print("Skipping this id")
        continue

    if story is None or "title" not in story:
        continue

    title = story["title"].lower()

    # checking each category manually
    for cat in cats:

        if count[cat] >= 5:
            continue

        words = cats[cat]

        found = False
        for w in words:
            if w in title:
                found = True
                break

        if found:
            row = {}

            row["post_id"] = story.get("id")
            row["title"] = story.get("title")
            row["category"] = cat
            row["score"] = story.get("score", 0)
            row["num_comments"] = story.get("descendants", 0)
            row["author"] = story.get("by")

            # saving time of collection
            row["collected_at"] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

            all_data.append(row)
            count[cat] += 1

            print("Added:", row["title"])
            break

    # check if all categories filled
    done = True
    for k in count:
        if count[k] < 25:
            done = False
            break

    if done:
        print("Enough data collected")
        break

# small delay (just to follow instructions)
for i in cats:
    time.sleep(2)

# creating folder if not exists
if not os.path.exists("data"):
    os.makedirs("data")

filename = "data/trends_" + datetime.now().strftime("%Y%m%d") + ".json"

with open(filename, "w") as f:
    json.dump(all_data, f, indent=4)

print("\nTotal collected:", len(all_data))
print("Saved file:", filename)