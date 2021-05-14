import os

with open('filenames.txt') as x:
    for line in x:
        line = line.strip()
        os.mkdir(line)