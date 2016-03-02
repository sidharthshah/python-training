import os
import sys
from os.path import join, getsize

if __name__ == "__main__":
    if len(sys.argv) <= 1:
        print "Please specify input directory"
        sys.exit(0)
    dir_to_traverse = sys.argv[1]

    for root, dirs, files in os.walk(dir_to_traverse):
        print sum([getsize(join(root, name)) for name in files]),
        print "bytes in", len(files), "non-directory files"
