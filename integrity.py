import hashlib , os
file=[]
directory="."
h = hashlib.sha256()

def baseline():
    global file ,directory,h
    files=os.listdir(directory)
    for items in files:
        if os.path.isfile(items):
            file.append(items)
    file=sorted(file)
    for f in file:
        with open(f,"rb") as fi:
            while True:
                chunk = fi.read(4096)
                if chunk == b"":
                    break
                h.update(chunk)
                print(h.hexdigest())
        with open ("baseline.txt","a") as w:
            w.write(f"{h.hexdigest()}\n")

baseline()