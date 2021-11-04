"""A file line counter"""


with open("timestamps.txt", "r") as fh:
    count = 0

    for line in fh:
        print(line.strip())
        count = count + 1

print(count,  'Lines')