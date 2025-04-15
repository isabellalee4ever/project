import os

directory = "People"
count = 0
for i in os.listdir(directory):
    with open(os.path.join(directory, i)) as f:
        print(f.read())
        count += 1
        print(count)
        
        