#!/usr/bin/env python3
import sys
import readline

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

##### HOMEWORK  
#  reorganize your code. 
#  apply literate programming (comments)
#  test out completion algorithm in >>> (IDE)
#  take 1 ACTION and make it a method of Wizard (such as 'study')

class Wizard:
    def __init__(self, location="forest"):
        self.location = location

        self.locations = {
            "forest" : "You travel to the forest where " \
                "you can forage for mushrooms and relax.",
            "tower"  : "You travel to your tower where there is peace and quiet.",
            "village" : "You travel to your village where " \
                "you can work, sell goods and shop.",
            "black rock city" : "You travel to the playa )'(.",
            }

    def travel(self, location):
        if location not in self.locations: 
            print(f'''{location} is not a place in this land.''')
        elif location == self.location:
            print(f'''You are already in {location}.''')
        else:
            self.location = location
            print(f"{self.locations[location]}")

def main():
    readline.set_auto_history(True)
    readline.set_completer(completion)
    wiz_help()
    wiz = Wizard()

    try:
        while True:
            task = input("> ")
            task = task.strip().lower()
            request(wiz, task)
    except (KeyboardInterrupt, EOFError):
        bye()

def completion(text, state):
    options = [
        "forest",
        "village", 
        "tower",
        "black rock city",
        "brew",
        "forage",
        "gift",
        "gold",
        "location",
        "purse",
        "sell",
        "skill level",
        "shop",
        "study",
        "work",
    ]
    matches = []
    
    for option in options:
        if option.startswith(text):
            matches.append(option)
    if state >= len(matches):
        return None
    return matches[state]

def request(wiz, task):
    global EGO
    global GOLD
    global BOOKS
    global MUSHROOMS
    global POTIONS
    global SKILL
    global STRESS

    if task in ["quit", "q", "Q"]:
        bye()
    elif task in wiz.locations:
        wiz.travel(task)       
    elif task in ["location", "where"]:
        if wiz.location is None:
            print('''You are nowhere. Where would you like to go?''')
        else:
            print(f"You are at the {wiz.location}.")
    elif task in ["skill level", "skill", "skills"]:
        print(f'''You are skill level {SKILL}.''' )
    elif task == "study":
        if wiz.location == "tower":
            if SKILL < BOOKS:
                SKILL = SKILL + 1
                STRESS += STRESS
                BOOKS -= BOOKS
                print(f'''Your skill level is now {SKILL}.''')
            else:
                print('''You have no more new books to read. ''')
        else:
            print(f'''You cannot study in the {wiz.location}.''')
    elif task == "relax":
        if wiz.location == "forest":
            STRESS -= 1
        else:
            print(f'''You can't relax in {wiz.location}. ''')
    elif task == "forage":
        if wiz.location == "forest":
            MUSHROOMS += 1
            print(f'''You now have {MUSHROOMS} mushrooms. ''')
        else:
            print(f'''There are no mushrooms in the {wiz.location}. ''')
    elif task == "work":
        if wiz.location == "village":
            if SKILL > 0:
                GOLD += SKILL
                STRESS += STRESS
                print(f'''All in a day's work. You now have {GOLD} gold.''')
            else:
                print(f'''You can't work without any skills.''')
        else:
            print(f'''There is no work in the {wiz.location}.''')
    elif task == "shop":
        if wiz.location == "village":
            if GOLD == 0:
                print(f'''You have {GOLD} gold. You must work to earn gold.''')
            else:
                GOLD -= 1
                BOOKS += 1
                STRESS += 1
                print(f'''You now have {BOOKS} books and {GOLD} gold.''')
        else:
            print(f'''You can't shop in the {wiz.location}.''')
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
        if wiz.location == "tower":
            if MUSHROOMS == 0:
                print(f'''You can't brew potions without mushrooms. ''')
            else:
                MUSHROOMS -= 1
                POTIONS += 1
                STRESS += 1
                print(f'''You have now have {POTIONS} potions.''')
        else:
            print(f'''You cannot brew potions in the {wiz.location}. ''')
    elif task == "sell":
        if wiz.location == "village":
            if POTIONS > 0:
                GOLD += GOLD
                print(f'''You now have {GOLD} gold.''')
            else:
                print(f'''You have no brewed potions to sell.''')
        else:
                print(f'''You can't sell goods in the {wiz.location}.''')
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
        '''\n gift'''
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