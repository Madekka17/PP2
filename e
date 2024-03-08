def multiply(numbers):
    total = 1
    for x in numbers:
        total *= x
    return total


def string_test(s):
    d = {"UPPER_CASE": 0, "LOWER_CASE": 0}
    for c in s:
        if c.isupper():
            d["UPPER_CASE"] += 1
        elif c.islower():
            d["LOWER_CASE"] += 1
        else:
            pass

    print("Original String: ", s)
    print("No. of Upper case characters: ", d["UPPER_CASE"])
    print("No. of Lower case Characters: ", d["LOWER_CASE"])



def isPalindrome(string):
    right_pos = len(string) - 1
    while right_pos >= left_pos:
        if not string[left_pos] == string[right_pos]:
            return False
        left_pos += 1
        right_pos -= 1
    return True


from time import sleep
import math
def delay(fn, ms, *args):
    sleep(ms / 1000)
    return fn(*args)
print(delay(lambda x: math.sqrt(x), 100, 16))
print(delay(lambda x: math.sqrt(x), 1000, 100))
print(delay(lambda x: math.sqrt(x), 2000, 25100))



import os

def list_files_and_directories(path):
    print("Directories:")
    print(os.listdir(path))
    
    print("\nFiles:")
    files = [f for f in os.listdir(path) if os.path.isfile(os.path.join(path, f))]
    print(files)

    print("\nAll Directories and Files:")
    for root, dirs, files in os.walk(path):
        print(f"Directory: {root}")
        print(f"Files: {files}")import os

def check_path_access(path):
    exists = os.path.exists(path)
    readable = os.access(path, os.R_OK)
    writable = os.access(path, os.W_OK)
    executable = os.access(path, os.X_OK)

    print(f"Path exists: {exists}")
    print(f"Readable: {readable}")
    print(f"Writable: {writable}")
    print(f"Executable: {executable}")

import os

def check_path_existence_and_details(path):
    exists = os.path.exists(path)

    if exists:
        filename = os.path.basename(path)
        directory = os.path.dirname(path)

        print(f"Path exists: {exists}")
        print(f"Filename: {filename}")
        print(f"Directory: {directory}")
    else:
        print(f"Path does not exist: {exists}")


