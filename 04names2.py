import sys

name = sys.argv[1]
with open(name,'r') as f:
    for line in f:
        fname = line.split()
        print(fname[0])
        