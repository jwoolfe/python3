#!/usr/bin/env python3


def main():
    while True:
        # store the numbers
        mon = input('Input hours Monday: ')
        tue = input('Input hours Tuesday: ')
        wed = input('Input hours Wednesday: ')
        thu = input('Input hours Thursday: ')
        fri = input('Input hours Friday: ')

	# add the hours for the week
        sum = float(mon) + float(tue) + float(wed) + float(thu) + float(fri)
        print('You worked {0} hours this week!'.format(sum))
        break

if __name__ == "__main__":
    main()
