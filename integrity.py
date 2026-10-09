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
    if os.path.isfile("!baseline.txt"):
        print("No baseline found. Run option 1 first.")
        exit
    for f in file:
        current_hash = create_hash(f)
        saved_hash = compare(f)
        