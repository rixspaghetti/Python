import json

# reading json data from a file 
try:
    with open("/Users/rix/Documents/School/Python/ReadWriteFiles/text.txt", "r") as json_file:
        data = json.load(json_file)
        print(data)
except FileNotFoundError:
    print("File not found.")

# writing json data to a file 
sample_data = {"name": "Alice", "age": "25", "city": "Wonderland"}
with open("/Users/rix/Documents/School/Python/ReadWriteFiles/text.txt", "w") as json_file:
    json.dump(sample_data, json_file, indent=4)

