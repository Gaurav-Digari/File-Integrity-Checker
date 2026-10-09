import hashlib , os
file=[]
directory="."
count=0
files=os.listdir(directory)

for items in files:
    if os.path.isfile(items):
        file.append(items)
        file=sorted(file)

def create_hash(f):
    h = hashlib.sha256()
    with open(f,"rb") as fi:
        while True:
            chunk = fi.read(4096)
            if chunk == b"":
                break
            h.update(chunk)
    return h.hexdigest()

def write_file():
    global count
    open("baseline.txt", "w").close()
    for f in file:
        hash=create_hash(f)
        print(f"{'saved:':<10} {f}")
        with open ("baseline.txt","a") as w:
            w.write(f"{f:<20} : {hash}\n")
            count+=1
    print(f"\nBaseline created for {count} files")


def compare(filename):
    with open("baseline.txt", "r") as base:
        for line in base:
            saved_file, saved_hash = line.split(":", 1)

            if saved_file.strip() == filename:
                return saved_hash.strip()

    return None

def checkfiles():
    try:
        f=open("baseline.txt","r")
        f.close()
    except FileNotFoundError:
        print("No baseline found. Run option 1 first.")
        return

    results = {}

    for f in file:
        current_hash = create_hash(f)
        saved_hash = compare(f)

        if saved_hash is None:
            results[f] = "NEW"
        elif current_hash == saved_hash:
            results[f] = "OK"
        else:
            results[f] = "MODIFIED"

    with open("baseline.txt", "r") as base:
        for line in base:
            saved_file, saved_hash = line.split(":", 1)
            if saved_file.strip() not in file:
                results[saved_file.strip()] = "MISSING"

    print("\nINTEGRITY CHECK")
    print("===============")

    ok = 0
    modified = 0
    missing = 0
    new = 0

    for name in sorted(results):
        label = results[name]
        print(f"{name:<20} {label}")

        if label == "OK":
            ok += 1
        elif label == "MODIFIED":
            modified += 1
        elif label == "MISSING":
            missing += 1
        elif label == "NEW":
            new += 1

    print("\nSummary")
    print("-------")
    print(f"{'OK':<9}: {ok}")
    print(f"{'MODIFIED':<9}: {modified}")
    print(f"{'MISSING':<9}: {missing}")
    print(f"{'NEW':<9}: {new}")

print("FILE INTEGRITY CHECKER")
print("1. Create baseline")
print("2. Check files")
choice=int(input("Enter choice:"))

if choice==1:
    write_file()
elif choice==2:
    checkfiles()
