# File Integrity Checker

A simple Python script that tells you if your files have been changed, deleted or added. It saves a SHA-256 hash (a fingerprint) of every file, and later compares the saved hashes with the current ones.

## How It Works

A hash is a fixed-length fingerprint made from a file's content. The same content always gives the same hash, and changing even one letter gives a completely different hash.

1. **Create baseline:** the script makes a hash of every file in the folder and saves the filenames and hashes in `baseline.txt`.
2. **Check files:** the script makes the hashes again and compares them with the saved ones, then labels every file.

Files are read in chunks of 4096 bytes, so large files do not use much memory.

## Features

- SHA-256 hashing with the `hashlib` module
- Simple menu: create a baseline or check files
- Four labels: `OK`, `MODIFIED`, `MISSING`, `NEW`
- Results shown in alphabetical order with a summary
- Creating a baseline again replaces the old one

## Requirements

- Python 3
- No extra installation needed. `hashlib` and `os` come built into Python.

## Usage

1. Put `integrity.py` in the folder with the files you want to monitor.
2. Run the script:

```bash
python integrity.py
```

3. Choose an option from the menu:

```
FILE INTEGRITY CHECKER
1. Create baseline
2. Check files
Enter choice:
```

Run option 1 first to save the baseline. Run option 2 any time after that to check the files.

## Example Output

**Option 1: Create baseline**

```
Saved: a.txt
Saved: b.txt

Baseline created for 2 files.
```

**`baseline.txt` after that**

```
a.txt                : <64-character hash>
b.txt                : <64-character hash>
```

**Option 2: Check files (nothing changed)**

```
INTEGRITY CHECK
===============
a.txt                OK
b.txt                OK

Summary
-------
OK       : 2
MODIFIED : 0
MISSING  : 0
NEW      : 0
```

**Option 2: Check files (`a.txt` edited, `b.txt` deleted, `c.txt` added)**

```
INTEGRITY CHECK
===============
a.txt                MODIFIED
b.txt                MISSING
c.txt                NEW

Summary
-------
OK       : 0
MODIFIED : 1
MISSING  : 1
NEW      : 1
```

If you choose option 2 before creating a baseline, the script prints:

```
No baseline found. Run option 1 first.
```

## Result Labels

| Label | Meaning |
|---|---|
| `OK` | The file is in the baseline and its hash is the same |
| `MODIFIED` | The file is in the baseline but its hash is different |
| `MISSING` | The file is in the baseline but no longer in the folder |
| `NEW` | The file is in the folder but not in the baseline |

## Project Structure

| File | Purpose |
|---|---|
| `integrity.py` | The main script |
| `baseline.txt` | Saved hashes, created by option 1 |
| `README.md` | Project description |

## Notes

- The script checks every file in the folder it runs in, including `integrity.py` and `baseline.txt`.
- `baseline.txt` is rewritten while the baseline is being created, so it will usually show as `MODIFIED` in a check.