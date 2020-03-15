#!/usr/bin/env python3
import sys

##### HOMEWORK  
#  reorganize your code. 
#  apply literate programming (comments)
#  test out completion algorithm in >>> (IDE)
#  take 1 ACTION and make it a method of Wizard (such as 'study')


def main():
    set_readline() 
    wiz_help()
    wiz = Wizard()

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
    elif task in ["location", "where"]:
        if wiz.location is None:
            print('''You are nowhere. Where would you like to go?''')
        else:
            print(f"You are at the {wiz.location}.")
    elif task in ["skill level", "skill", "skills"]:
        print(f'''You are skill level {wiz.skill}.''' )
    elif task == "study":
        print(1)
        wiz.study()
    elif task == "relax":
        if wiz.location == "forest":
            wiz.stress -= 1
        else:
            print(f'''You can't relax in {wiz.location}. ''')
    elif task == "forage":
        if wiz.location == "forest":
            wiz.mushrooms += 1
            print(f'''You now have {wiz.mushrooms} mushrooms. ''')
        else:
            print(f'''There are no mushrooms in the {wiz.location}. ''')
    elif task == "work":
        if wiz.location == "village":
            if wiz.skill > 0:
                wiz.gold += wiz.skill
                wiz.stress += wiz.stress
                print(f'''All in a day's work. You now have {wiz.gold} gold.''')
            else:
                print(f'''You can't work without any skills.''')
        else:
            print(f'''There is no work in the {wiz.location}.''')
    elif task == "shop":
        if wiz.location == "village":
            if wiz.gold == 0:
                print(f'''You have {wiz.gold} gold. You must work to earn gold.''')
            else:
                wiz.gold -= 1
                wiz.books += 1
                wiz.stress += 1
                print(f'''You now have {wiz.books} books and {wiz.gold} gold.''')
        else:
            print(f'''You can't shop in the {wiz.location}.''')
    elif task == "gold":
        print(f'''You have {wiz.gold} gold.''')
    elif task == "purse":
        print(f'''You have {wiz.books} books, {wiz.gold} gold, {wiz.mushrooms} mushrooms & {wiz.potions} potions. ''')
    elif task == "items":
        print(f'''             
            wiz.books: {wiz.books}
            wiz.gold: {wiz.gold} 
            wiz.mushrooms: {wiz.mushrooms} 
            wiz.potions: {wiz.potions}
            wiz.skill: {wiz.skill}
            wiz.stress: {wiz.stress} ''')
    elif task == "brew":
        if wiz.location == "tower":
            if wiz.mushrooms == 0:
                print(f'''You can't brew potions without mushrooms. ''')
            else:
                wiz.mushrooms -= 1
                wiz.potions += 1
                wiz.stress += 1
                print(f'''You have now have {wiz.potions} potions.''')
        else:
            print(f'''You cannot brew potions in the {wiz.location}. ''')
    elif task == "sell":
        if wiz.location == "village":
            if wiz.potions > 0:
                wiz.gold += wiz.gold
                print(f'''You now have {wiz.gold} gold.''')
            else:
                print(f'''You have no brewed potions to sell.''')
        else:
                print(f'''You can't sell goods in the {wiz.location}.''')
    elif task in ["help", "h", "?"]:
        wiz_help()
    else:
        print(f'''I dunno "{task}".''')

class Wizard:
    def __init__(self, location="forest", skill=0, gold=0, books=1, stress=0,
            ego=0, potions=0, mushrooms=0):
        self.location = location
        self.skill = skill
        self.gold = gold
        self.books = books
        self.stress = stress
        self.ego = ego
        self.potions = potions
        self.mushrooms = mushrooms

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
                self.skill = self.skill + 1
                self.stress += self.stress
                self.books -= self.books
                print(f'''Your skill level is now {self.skill}.''')
            else:
                print('''You have no more new books to read. ''')
        else:
            print(f'''You cannot study in the {self.location}.''')

    def brew(self):
        pass
    
    def forage(self):
        pass

    def gift(self):
        pass

    def where(self):
        pass

    def purse(self):
        pass

    def sell (self):
        pass

    def shop (self):
        pass

    def work(self):
        pass

def save(wiz):
    data = {
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

def set_readline():
    import readline

    readline.set_auto_history(True)
    readline.set_completer(completion)

    if 'libedit' in readline.__doc__:
        readline.parse_and_bind("bind ^I rl_complete")
    else:
        readline.parse_and_bind("tab: complete")


if __name__ == "__main__":
    main()