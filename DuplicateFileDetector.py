print()
print (title)
print()

import os
import hashlib
import csv
import datetime
from prettytable import PrettyTable


def calculate_hash(file_path, block_size = 65536):
    file_hash = hashlib.sha256()
    with open(file_path, 'rb') as f:
        for block in iter(lambda: f.read(block_size), b''):
            file_hash.update(block)
    return file_hash.hexdigest()


def find_duplicates(directory_path):
    hashes = {}
    for foldername, subfolders, filenames in os.walk(directory_path):
        for filename in filenames:
            file_path = os.path.join(foldername, filename)
            print(f"Scanning {file_path}")
            file_hash = calculate_hash(file_path)
            if file_hash not in hashes:
                hashes[file_hash] = [file_path]
            else:
                hashes[file_hash].append(file_path)
    return hashes


def log_and_print_duplicates(duplicates):
    table = PrettyTable(["Hash", "File Paths"])
    current_time = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    filename = f"duplicates_{current_time}.csv"
    with open(filename, 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(["Hash", "File Paths"])
        for key, values in duplicates.items():
            if len(values) > 1:
                for value in values:
                    writer.writerow([key, value])
                    table.add_row([key, value])
    print(table)


if __name__ == "__main__":
    directory_path = input("Enter directory path to search for duplicates: ")
    duplicates = find_duplicates(directory_path)
    log_and_print_duplicates(duplicates)
