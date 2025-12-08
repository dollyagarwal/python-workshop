
import json
from collections import Counter
from typing import List, Dict

# String normalization
sentence = ' hello,   world from   python  '
normalized = ' '.join(sentence.split()).strip()
print(normalized)

# Deduplicate & count
emails = ['a@example.com','b@example.com','a@example.com','c@example.com']
unique = list(set(emails))
counts = Counter(emails)
print(unique, counts)

# JSON parsing & filtering
users = [{"id":1,"name":"Ann","active":True},{"id":2,"name":"Bob","active":False}]
active_users = [u for u in users if u.get('active')]
print(active_users)

# Write filtered output
with open('active_users.json', 'w') as f:
    json.dump(active_users, f, indent=2)

# Mock API
def fetch_posts():
    return [
        {"id": 1, "title": "Intro to Python", "tags": ["python","training"]},
        {"id": 2, "title": "Using Requests", "tags": ["http","python"]}
    ]

posts = fetch_posts()
print(posts)

# Optional pandas usage
try:
    import pandas as pd
    df = pd.DataFrame(posts)
    print(df.describe(include='all'))
except Exception as e:
    print('Pandas not installed or error:', e)
