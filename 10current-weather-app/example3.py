"""
This program is an example of json.loads().
It converts a JSON string into a Python dictionary.
"""

import json

# JSON string
json_string = '{"name": "Alice", "age": 25, "city": "Tokyo"}'

# Convert JSON string to Python dictionary
data = json.loads(json_string)

# Access values
print("Name:", data["name"])
print("Age:", data["age"])
print("City:", data["city"])