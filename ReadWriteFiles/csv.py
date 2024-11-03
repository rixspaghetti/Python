import csv

#reading from a CSV file
try: 
    with open("/Users/rix/Documents/School/Python/ReadWriteFiles/text.txt", "r") as csv_file:
        reader = csv.reader(csv_file)
        for row in reader:
            print(row) # each row is a list of values
except FileNotFoundError:
    print("File not found.")

# write to a csv file
data_to_write = [["Name", "Age", "City"], ["Alice", 25, "Wonderland"]]
with open("/path/to/output.csv", "w", newline='') as csv_file:
    writer = csv.writer(csv_file)
    writer.writerows(data_to_write)