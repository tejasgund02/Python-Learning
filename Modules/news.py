import requests

API_KEY = "1743025f4c1c44428619ea94349320bb"   # ← Replace with your key
BASE_URL = "https://newsapi.org/v2/top-headlines"

topics = {
    "technology": "technology",
    "business": "business",
    "sports": "sports",
    "science": "science",
    "entertainment": "entertainment",
    "health": "health"
}

def get_news(category):
    params = {
        "apiKey": API_KEY,
        "category": category,
        "country": "us"
    }
    response = requests.get(BASE_URL, params=params)
    data = response.json()

    if data.get("status") != "ok":
        print(f"Error fetching {category} news")
        return

    print(f"\n🔷 TOP {category.upper()} NEWS")
    print("-" * 50)

    for article in data["articles"][:5]:  # show top 5
        print("•", article["title"])
        if article["url"]:
            print("  Link:", article["url"])
        print()

# Fetch news for all topics
for topic, category in topics.items():
    get_news(category)
