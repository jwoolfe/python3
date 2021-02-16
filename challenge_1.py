#!/usr/bin/env python3

def main():
    pairs = [
        (2331, 1332),
        (123456789, 987654321),
        (-12, -21),
        (-9834937, -7394389),
        ]

    for forward, backward in pairs:
        if reverse_int(forward) == backward:
            print(f"{forward} reversed is {backward}: CORRECT!")
        else:
            print(
                f"Whups, {forward} resulted in {reverse_int(forward)} "
                f"instead of {backward}. WRONG!"
                )


def reverse_int(num:int):
    """
    Accepts an integer, and returns the same integer with the numbers in reverse order.

    For example, reverse_int(2355) should return 5532.

    It may get tricky, though, because reverse_int(-17) should return -71, not 71-.
    """
    # check if num is negative
    if num < 0:
        neg = True
    else:
        neg = False

    # convert types in order to reverse
    num = abs(num)
    num_list = list(str(num))
    num_list.reverse()
    num_str = ''.join([str(elem) for elem in num_list])

    if neg == True:
        num_str = '-' + num_str
    
    num = int(num_str)
    return num


if __name__=='__main__':
    main()
