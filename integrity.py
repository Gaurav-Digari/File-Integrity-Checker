import hashlib , os
file=[]
directory="."

def baseline():
    global file ,directory
    files=os.listdir(directory)
    for items in files:
        if os.path.isfile(items):
            file.append(items)
    file=sorted(file)