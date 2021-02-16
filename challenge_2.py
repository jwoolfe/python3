#!/usr/bin/env python3

def main():
    pairs = [
        (230301, 233100),
        (1203045600789, 1234567890000),
        ]

    for start, end in pairs:
        start = [int(i) for i in str(start)]
        end = [int(i) for i in str(end)]
        if shove_zeroes_right(start) == end:
            print(f"{start} sorted is {end}: CORRECT!")
        else:
            print(
                f"Whups, {start} resulted in {shove_zeroes_right(start)} "
                f"instead of {end}. WRONG!"
                )


def shove_zeroes_right(numbers):
    """
    Accepts a list of integers, and returns the list with any entries equal to zero moved to the
    right, but all other numbers in the same order.

    For example:

        [1, 0, 4, 4, 2, 0, 7, 0, 9]

    would return:

        [1, 4, 4, 2, 7, 9, 0, 0, 0]
    """

    pass  # TO BE IMPLEMENTED


if __name__=='__main__':
    main()
