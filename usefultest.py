import json

with open("fake.json", "r") as data:
    obj = json.load(data)

print obj