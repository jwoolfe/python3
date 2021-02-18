#!/usr/bin/env python3

from configparser import ConfigParser
import sys
import os.path

##### HOMEWORK  
#  reorganize your code. 
#  apply literate programming (comments)
#  test out completion algorithm in >>> (IDE)

def main():
    set_readline() 
    wiz_help()
    wiz = load()

    try:
        while True:
            task = input("> ")
            task = task.strip().lower()
            request(wiz, task)
            save(wiz)
    except (KeyboardInterrupt, EOFError):
        bye()

def request(wiz, task):

    if task in ["quit", "q", "Q"]:
        bye()
    elif task in wiz.locations:
        wiz.travel(task)
    elif task == "brew":
        wiz.brew()
    elif task == "forage":
        wiz.forage()
    elif task == "gift":
        wiz.gift()
    elif task == "gold":
        wiz.purse()
    elif task == "health":
        wiz.health()
    elif task in ["help", "h", "?"]:
        wiz_help()
    elif task in ["location", "where"]:
        wiz.where()
    elif task == "purse":
        wiz.purse()
    elif task == "relax":
        wiz.relax()
    elif task == "sell":
        wiz.sell()
    elif task in ["skill level", "skill", "skills"]:
        wiz.health
    elif task == "shop":
        wiz.shop()
    elif task == "study":
        wiz.study()
    elif task == "work":
        wiz.work()
    else:
        print(f'''I dunno "{task}".''')

class Wizard:
    def __init__(self, location="forest", skill=0, gold=0, books=1, stress=0,
            ego=0, potions=0, mushrooms=0, work=0):
        self.books = books
        self.ego = ego
        self.gold = gold
        self.location = location
        self.mushrooms = mushrooms
        self.skill = skill
        self.stress = stress
        self.potions = potions

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
    
    def study(self):
        if self.location == "tower":
            if self.skill < self.books:
                self.skill += 1
                self.stress += 1
                self.books -= 1
                print(f'''Your skill level is now {self.skill}.''')
            else:
                print('''You have no more new books to read. ''')
        else:
            print(f'''You cannot study in the {self.location}.''')

    def brew(self):
        if self.location == "tower":
            if self.mushrooms == 0:
                    print(f'''You can't brew potions without mushrooms. ''')
            else:
                self.mushrooms -= 1
                self.potions += 1
                self.stress -= 1
                print(f'''You have now have {self.potions} potions.''')
        else:
                print(f'''You cannot brew potions in the {self.location}. ''')
    
    def forage(self):
        if self.location == "forest":
            self.mushrooms += 1
            print(f'''You now have {self.mushrooms} mushrooms. ''')
        else:
            print(f'''There are no mushrooms in the {self.location}. ''')

    def gift(self):
        if self.location == "black rock city":
            if self.potions > 0:
                self.potions -= 1
                self.stress -= 1
                print(f'''You now have {self.potions} potions and you have lowered your stress level.''')
            else:
                print(f'''You have no potions to gift.''')
        else:
            print(f'''You cannot give gifts in the {self.location}.''')

    def where(self):
        if self.location is None:
            print('''You are nowhere. Where would you like to go?''')
        else:
            print(f"You are at the {self.location}.")

    def purse(self):
        print(f'''   You have {self.books} books''')
        print(f'''   You have {self.gold} gold''')
        print(f'''   You have {self.mushrooms} mushrooms''')
        print(f'''   You have {self.potions} potions''')

    def relax(self):
        if self.location == "forest":
            self.stress -= 1
        else:
            print(f'''You can't relax in {self.location}. ''')

    def sell(self):
        if self.location == "village":
            if self.potions > 0:
                self.gold += self.gold
                print(f'''You now have {self.gold} gold.''')
            else:
                print(f'''You have no brewed potions to sell.''')
        else:
                print(f'''You can't sell goods in the {self.location}.''')

    def shop(self):
        if self.location == "village":
            if self.gold == 0:
                print(f'''You have {self.gold} gold. You must work to earn gold.''')
            else:
                if self.stress >10:
                    print("You are too stressed out. Go do relaxing things.")
                else:
                    self.gold -= 1
                    self.books += 1
                    self.stress += 1
                    print(f'''You now have {self.books} books and {self.gold} gold.''')
        else:
            print(f'''You can't shop in the {self.location}.''')

    def health(self):
        print(f'''   You have a stress level of {self.stress}''')
        print(f'''   You are at skill level {self.skill}''' )

    def work(self):
        if self.location == "village":
            if self.skill > 0:
                self.gold += self.skill
                if self.stress >10:
                    print("You are too stressed out. Go do relaxing things.")
                else:
                    self.stress += 1
                    print(f'''All in a day's work. You now have {self.gold} gold.''')
            else:
                print(f'''You can't work without any skills.''')
        else:
            print(f'''There is no work in the {self.location}.''')

def completion(text, state):
    options = [
        "black rock city",
        "brew",
        "forage",
        "forest",
        "gift",
        "gold",
        "health",
        "location",
        "purse",
        "relax",
        "sell",
        "skill level",
        "shop",
        "study",
        "tower",
        "travel",
        "village", 
        "work",
    ]
    matches = []
    
    for option in options:
        if option.startswith(text):
            matches.append(option)
    if state >= len(matches):
        return None
    return matches[state]

def set_readline():
    import readline

    readline.set_auto_history(True)
    readline.set_completer(completion)

    if 'libedit' in readline.__doc__:
        readline.parse_and_bind("bind ^I rl_complete")
    else:
        readline.parse_and_bind("tab: complete")

def save(wiz):
    data = ConfigParser()
    data['wizard'] = {
        "location": wiz.location,
        "skill": wiz.skill,
        "gold": wiz.gold,
        "books": wiz.books,
        "stress": wiz.stress,
        "ego": wiz.ego,
        "potions": wiz.potions,
        "mushrooms": wiz.mushrooms,
    }
    savefile = open("wiz.save", "w")
    for key in data:
        savefile.write(f"{key}:{data[key]}\n")

def load():
    data = {}
    if os.path.isfile("wiz.save"):
        savefile = open("wiz.save", "r")
        for line in savefile:
            key, value = line.strip().split(":")
            if key != "location":
                value = int(value)
            data[key] = value
    wiz = Wizard(**data)
    return wiz

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