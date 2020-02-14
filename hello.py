#!/usr/bin/env python3

import sys
def main(name):
    print(f'''hello, {s()}!''')

def s():
    return "booyah!"


if __name__ == "__main__":
    main(sys.argv[1])