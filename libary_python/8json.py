import json
from pathlib import Path

movies = [
    {"Name":"Nataraj", "Age": 36},
    {"Name": "karthick", "Age": 27}
]

data = json.dumps(movies)
#print(data)
Path("movies.json").write_text(data)

data = Path("movies.json").read_text()
movies = json.loads(data)
print(movies[1])