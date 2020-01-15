#!/usr/bin/env python3

def main():
    while True:
        msg = input("What should I say? ")
        if msg == "quit":
            break
        print(msg)

if __name__ == "__main__":
    main()