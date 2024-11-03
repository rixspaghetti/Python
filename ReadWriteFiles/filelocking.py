import fcntl

try: 
    with open("/path/to/shared_file.txt", "r+") as file:
        fcntl.flock(file, fcntl.LOCK_EX) # exclusive lock for writing
        content = file.read()
        file.write("Appending new data...\n")
        fcntl.flock(file, fcntl.LOCK_UN) # release lock
except FileNotFoundError:
    print("File not found.")