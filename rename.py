import os

for filename in os.listdir('.'):
    if "_code" in filename:
        continue

    if filename.endswith(".py"):
        newname = filename.replace(".py", ".txt")
        print("Renaming {} to {}".format(filename, newname))
        os.rename(filename, newname)
