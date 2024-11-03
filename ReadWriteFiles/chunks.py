# reading large files in chunks 
chunk_size = 1024

try:
    with open("/Users/rix/Documents/School/Python/ReadWriteFiles/text.txt") as file:
        while chunk := file.read(chunk_size): # := operator is new in python 3.8
            # process each chunk
            print(chunk)
except FileNotFoundError:
    print("File not found")