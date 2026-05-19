import json

# 1️⃣ SAVE (Dict → JSON file)
data = {"name": "Alpha Coder", "age": 17, "skills": ["Python", "OOP"]}

with open("my_data.json", "w") as file:
    json.dump(data, file)  # Save karo
print("✅ Saved!")

# 2️⃣ LOAD (JSON file → Dict)
with open("my_data.json", "r") as file:
    loaded_data = json.load(file)  # Load karo
print(loaded_data["name"])  # Alpha Coder

# 3️⃣ STRING to DICT (Internet se data aata hai)
json_string = '{"city": "Karachi", "temp": 30}'
parsed = json.loads(json_string)  # String → Dict
print(parsed["city"])  # Karachi

# 4️⃣ DICT to STRING (Bhejne ke liye)
new_string = json.dumps({"msg": "Hello"})
print(new_string)  # '{"msg": "Hello"}'