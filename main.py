#!/bin/python3

# preparing
import csv
here = None
doing = None
f = open("data.csv", 'r+')
read = [i[1] for i in csv.reader(f)]

def save(where=read[0], doingp=read[1]):
    print("...") #oh no dont leave
    global here
    global doing
    global f
    read[0] = (here := where)
    read[1] = (doing := doingp)
    f.truncate(0)
    csv.writer(f).writerow("location", read[0])
    csv.writer(f).writerow("action", read[1])
    # TODO: fix this for battle
    print('')#ok now
# ask function
def ask(*options: tuple, question="What do you do?", other="") -> str:
    print("\t\b", question, '\n\t')
    for i in options:
        print(f"\t{i[0]}: {i[1]}")
    if (x := input('\tة<( ')) in options: return x
    elif x == 'quit':
        save()
        exit(0)
    else: return other

actions = {}
class Action:
    def __init__(self, id: str, nickname: str, str: str, opt: tuple, print: bool, dict=actions) -> None:
        self.id = id
        self.nickname = nickname
        self.str = str
        self.opt = opt
        self.print = print
        self.question = "What do you want to do now?"
        self.dict = dict
        self.dict[self.id] = self
    def next(self):
        if self.print:
            print(self.str)
            save(ask(*self.opt, self.question)) if not self.question == None else save(ask(*self.opt))
    def __str__(self):
        print(f"{self.id}\n{self.nickname}\nclass: {self.__class__.__name__}\n{self.str}\n{self.question} ({self.print})\n{[i.id for i in self.opt]}")

scenes = {}
class Scene(Action):
    def __init__(self, id: str, nickname: str, desc: str, next: tuple):
        super().__init__(id, nickname, desc, next, True, scenes)
        self.question = f"Where do you want to go from {self.nickname}?"
        for i in next:
            self.next.append(i)
            i.next.append(self)
    def forth(self, to):
        self.next.append(to)
    def link(self, to):
        self.forth(to)
        to.forth(self)
    
def step():
    pass