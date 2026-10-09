import hashlib , os
file=[]
directory="."
h = hashlib.sha256()
count=0

def baseline():
    open("baseline.txt", "w").close()
    global file ,directory,h,count
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
                count+=1
                print(f"{f:<20} : {h.hexdigest()}")
        with open ("baseline.txt","a") as w:
            w.write(f"{f:<20} : {h.hexdigest()}\n")
            
    with open ("baseline.txt","a") as w :
        w.write(f"\nBaseline created for {count} files")
    print(f"\nBaseline created for {count} files")

baseline()