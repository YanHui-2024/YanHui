import gc
import torch
print(len(gc.get_objects))  # Works
a = gc.get_objects()  # works
print(gc.get_objects())  # Fails
for obj in gc.get_objects():
    print(obj)  # Works until encountering torch
                    # Though it works on some files
print(sum(map(sys.getsizeof, gc.get_objects())))  # Works
print(collections.Counter(map(type, gc.get_objects())))  # Works