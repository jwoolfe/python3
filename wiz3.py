#!/usr/bin/env python3
import sys

def main():
    global LOCATION
    LOCATION = None
    wiz_help()

    try:
        while True:
            task = input("> ")
            request(task)
    except (KeyboardInterrupt, EOFError):
        bye()

def request(task):
    global LOCATION
    if task in ["quit", "q", "Q"]:
        bye()
    elif task == LOCATION:
        print(f"You are at the {LOCATION}. Did you forget? ")
    elif task == "location":
        if LOCATION is None:
            print('''You are nowhere. Where would you like to go?''')
        else:
            print(f"You are at the {LOCATION}.")
    elif task == "tower":
        LOCATION = "tower"
        print('''You travel to your modest, one-story tower.''')
    elif task == "village":
        LOCATION = "village"
        print ('''You travel to your village ''' 
         '''where the one-story tower cannot be seen. ''')
    elif task == "forest":
        LOCATION = "forest"
        print('''You travel to the forest '''   
            '''where you can not longer see the trees. ''')
    elif task in ["help", "h", "?"]:
        wiz_help()
    else:
        print(f'''I dunno "{task}".''')

def wiz_help():
    print('''Where would you like to go? ''' 
        '''\n forest ''' 
        '''\n village ''' 
        '''\n tower '''
        '''\n help '''
        '''\n location '''
        '''\n quit ''')

def bye():
    print("\nGoodbye")
    sys.exit()

if __name__ == "__main__":
    main()