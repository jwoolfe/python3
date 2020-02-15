#!/usr/bin/env python3
import sys
import readline

LOCATION = "forest"
SKILL = 0
GOLD = 0
LIBRARY = 1

def main():
    readline.set_auto_history(True)
    wiz_help()

    try:
        while True:
            task = input("> ")
            task = task.strip().lower()
            request(task)
    except (KeyboardInterrupt, EOFError):
        bye()

def request(task):
    global LOCATION
    global SKILL
    global GOLD
    global LIBRARY

    if task in ["quit", "q", "Q"]:
        bye()
    elif task == LOCATION:
        print(f"You are at the {LOCATION}.")
    elif task == "location":
        if LOCATION is None:
            print('''You are nowhere. Where would you like to go?''')
        else:
            print(f"You are at the {LOCATION}.")
    elif task == "skill level":
        print(f'''You are skill level {SKILL}.''' )
    elif task == "study":
        if LOCATION == "tower":
            if SKILL < LIBRARY:
                SKILL = SKILL + 1
                print(f'''Excellent Student. Your skill level is now {SKILL}''')
            else:
                print('''You have no more new books to read. ''')
        else:
            print(f'''You cannot study in the {LOCATION}.''')
    elif task == "tower":
        LOCATION = "tower"
        print('''You travel to your tower, away from the world.''')
    elif task == "village":
        LOCATION = "village"
        print ('''You travel to your village ''' 
         '''where there is much activity and joy.''')
    elif task == "forest":
        LOCATION = "forest"
        print('''You travel to the forest '''   
            '''where you can see all of the trees. ''')
    elif task == "work":
        if LOCATION == "village":
            if SKILL > 0:
                GOLD += SKILL
                print(f'''All in a day's work. You now have {GOLD} gold.''')
            else:
                print(f'''You can't work without any skills.''')
        else:
            print(f'''There is no work in the {LOCATION}.''')
    elif task == "shop":
        if LOCATION == "village":
            if GOLD == 0:
                print(f'''You have {GOLD} gold. You must work to earn gold.''')
            else:
                GOLD -= 1
                LIBRARY += 1
                print(f'''Nice shopping. You now have {LIBRARY} books and {GOLD} gold.''')
        else:
            print(f'''You can't shop in the {LOCATION}.''')
    elif task == "gold":
        print(f'''You have {GOLD} gold.''')
    elif task in ["help", "h", "?"]:
        wiz_help()
    else:
        print(f'''I dunno "{task}".''')

def wiz_help():
    print('''Where would you like to go? ''' 
        '''\n forest ''' 
        '''\n village ''' 
        '''\n tower '''
        '''\n'''
        '''\n location '''
        '''\n work'''
        '''\n study '''
        '''\n gold'''
        '''\n shop '''
        '''\n skill level '''
        '''\n'''
        '''\n help '''
        '''\n quit ''')

def bye():
    print("\nThank you for playing!")
    sys.exit()

if __name__ == "__main__":
    main()