#!/usr/bin/env python3
import sys
import readline

LOCATION = "forest"
SKILL = 0
GOLD = 0
BOOKS = 1
STRESS = 0
EGO = 0
POTIONS = 0
MUSHROOMS = 0

##### TEST
MUSHROOMS = 10
SKILL = 6
GOLD = 10


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
    global EGO
    global GOLD
    global BOOKS
    global LOCATION
    global MUSHROOMS
    global POTIONS
    global SKILL
    global STRESS

    if task in ["quit", "q", "Q"]:
        bye()
    elif task == LOCATION:
        print(f"You are at the {LOCATION}.")
    elif task in ["location", "where"]:
        if LOCATION is None:
            print('''You are nowhere. Where would you like to go?''')
        else:
            print(f"You are at the {LOCATION}.")
    elif task in ["skill level", "skill", "skills"]:
        print(f'''You are skill level {SKILL}.''' )
    elif task == "study":
        if LOCATION == "tower":
            if SKILL < BOOKS:
                SKILL = SKILL + 1
                STRESS += STRESS
                BOOKS -= BOOKS
                print(f'''Your skill level is now {SKILL}.''')
            else:
                print('''You have no more new books to read. ''')
        else:
            print(f'''You cannot study in the {LOCATION}.''')
    elif task == "tower":
        LOCATION = "tower"
        print('''You travel to your tower where there is quiet.''')
    elif task == "village":
        LOCATION = "village"
        print ('''You travel to your village ''' 
         '''where you can work, sell goods and shop.''')
    elif task == "forest":
        LOCATION = "forest"
        print('''You travel to the forest '''   
            '''where you can forage for mushrooms and relax. ''')
    elif task == "relax":
        if LOCATION == "forest":
            STRESS -= 1
        else:
            print(f'''You can't relax in {LOCATION}. ''')
    elif task == "forage":
        if LOCATION == "forest":
            MUSHROOMS += 1
            print(f'''You now have {MUSHROOMS} mushrooms. ''')
        else:
            print(f'''There are no mushrooms in the {LOCATION}. ''')
    elif task == "work":
        if LOCATION == "village":
            if SKILL > 0:
                GOLD += SKILL
                STRESS += STRESS
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
                BOOKS += 1
                STRESS += 1
                print(f'''You now have {BOOKS} books and {GOLD} gold.''')
        else:
            print(f'''You can't shop in the {LOCATION}.''')
    elif task in ["black rock", "playa", "brc", "black rock city"]:
        LOCATION = "black rock city"
        print('''You travel to the playa )'(.  ''')
    elif task == "gold":
        print(f'''You have {GOLD} gold.''')
    elif task == "purse":
        print(f'''You have {BOOKS} books, {GOLD} gold, {MUSHROOMS} mushrooms & {POTIONS} potions. ''')
    elif task == "items":
        print(f'''             
            BOOKS: {BOOKS}
            GOLD: {GOLD} 
            MUSHROOMS: {MUSHROOMS} 
            POTIONS: {POTIONS}
            SKILL: {SKILL}
            STRESS: {STRESS} ''')
    elif task == "brew":
        if LOCATION == "tower":
            if MUSHROOMS == 0:
                print(f'''You can't brew potions without mushrooms. ''')
            else:
                MUSHROOMS -= 1
                POTIONS += 1
                STRESS += 1
                print(f'''You have now have {POTIONS} potions.''')
        else:
            print(f'''You cannot brew potions in the {LOCATION}. ''')
    elif task == "sell":
        if LOCATION == "village":
            if POTIONS > 0:
                GOLD += GOLD
                print(f'''You now have {GOLD} gold.''')
            else:
                print(f'''You have no brewed potions to sell.''')
        else:
                print(f'''You can't sell goods in the {LOCATION}.''')
    elif task in ["help", "h", "?"]:
        wiz_help()
    else:
        print(f'''I dunno "{task}".''')

def wiz_help():
    print(
        '''\n LOCATIONS: '''
        '''\n forest ''' 
        '''\n village ''' 
        '''\n tower '''
        '''\n black rock city '''
        '''\n'''
        '''\n ACTIONS: '''
        '''\n brew '''
        '''\n forage '''
        '''\n gold '''
        '''\n location '''
        '''\n purse '''
        '''\n sell '''
        '''\n skill level '''
        '''\n shop '''
        '''\n study '''
        '''\n work '''

        '''\n'''
        '''\n help '''
        '''\n quit '''
        '''\n \n Please choose an action or location. ''' )

def bye():
    print("\nThank you for playing!")
    sys.exit()

if __name__ == "__main__":
    main()