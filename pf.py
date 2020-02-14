#!/usr/bin/env python3

import sys
def main(filename):
    f = open(filename, "a")
    f.write("ROCKY HORROR\n")
    f = open(filename)
    print(f.read())



if __name__ == "__main__":
    main(sys.argv[1])