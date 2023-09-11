# Duplicate File Detector

**Description:** This script, written in Python, is designed to detect and log duplicate files within a specified directory, including its subdirectories. The script identifies duplicates by calculating and comparing the SHA-256 hash of each file, a unique identifier produced from the file content.

**Author:** Altered Admin  
**Date:** July 20, 2022  
**Website:** [Altered Admin's Site](https://alteredadmin.github.io)  
**Twitter:** [@Alt3r3dAdm1n](https://twitter.com/Alt3r3dAdm1n)  

---

## Features

- Efficiently calculates SHA-256 hashes of files.
- Scans directories recursively for file duplicates.
- Saves duplicate details in a timestamped CSV file.
- Displays duplicates in a well-formatted table.

## Dependencies

Required modules:

- os
- hashlib
- csv
- datetime
- prettytable (Install via pip: `pip install prettytable`)

## Detailed Functions

- `calculate_hash(file_path, block_size = 65536)`: This function calculates the SHA-256 hash of a given file. It reads the file in blocks of size block_size to ensure it can handle large files without exhausting system memory.

- `find_duplicates(directory_path)`: This function takes in a directory path and traverses through every file within that directory and its subdirectories. For each file, it calculates the file's hash using the calculate_hash function, and keeps track of these hashes in a dictionary. If a file with the same hash is found, it is considered a duplicate.

- `log_and_print_duplicates(duplicates)`: This function logs the duplicate files to a CSV file and prints them in an ASCII table. The CSV file is named with the current date and time to ensure unique filenames for each run of the script. Each row in the CSV file represents a file path associated with a hash value.

## Usage

1. Clone the repository:

```bash
git clone https://github.com/alteredadmin/DuplicateFileDetector.git
cd DuplicateFileDetector
```

2. Run the script:

```bash
python DuplicateFileFinder.py
```

3. When prompted, enter the directory path where you wish to search for duplicates. During its execution, the script prints out the file paths of the files it is currently scanning, so users can observe its progress.

---

### Support the Developer

If you found this helpful, please consider:

- **Buymeacoffee:** [Link](http://buymeacoffee.com/alteredadmin)
- **BTC:** `bc1qhkw7kv9dtdk8xwvetreya2evjqtxn06cghyxt7`
- **LTC:** `ltc1q2mrh9s8sgmh8h5jtra3gqxuhvy04vuagpm3dk9`
- **ETH:** `0xef053b0d936746Df00C9CCe0454b7b8afb1497ac`

---

### License

n/a
