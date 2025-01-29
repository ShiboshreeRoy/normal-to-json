from datetime import datetime
from normal_to_json import NormalToJsonConverter

# Sample data
data = {
    "name": "John Doe",
    "age": 30,
    "is_student": False,
    "courses": ["Math", "Science"],
    "birthday": datetime(1993, 4, 15)
}

# Convert to JSON string
json_string = NormalToJsonConverter.convert(data, indent=4)
print(json_string)

# Save to JSON file
NormalToJsonConverter.convert_to_file(data, "output.json", indent=4)