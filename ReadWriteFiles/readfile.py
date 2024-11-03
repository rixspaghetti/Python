try:
    with open ("/Users/rix/Documents/School/Python/ReadWriteFiles/text.txt") as file:
        content = file.read()
        print(content)
except FileNotFoundError:
    print("File not found.")