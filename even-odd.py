#!/usr/bin/env python3

def main():
    while True:
        msg = input("Even, odd or quit? ")
        if msg == "quit":
            break
        elif msg == "Even":
            for num in range(1,11):
                if num % 2 == 0:
                    print(num, end = " ")
            print()
        elif msg == "odd":
            print("1","3","5","7","9")
        else:
            print("Retry. ")


if __name__ == "__main__":
    main()