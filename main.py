import csv
here = None
doing = None
f = open("data.csv", 'r+')
read = [i[1] for i in csv.reader(f)]

def ask(*options: tuple, question="What do you do?", other="") -> str:
    print("\t\b", question, '\n\t')
    for i in options:
        print(f"\t{i[0]}: {i[1]}")
    if (x := input('\tة<( ')) in options: return x
    else: return other
class Action:
    def __init__(self, nickname: str, str: str, opt: tuple, print: bool) -> None:
        self.nickname = nickname
        self.str = str
        self.opt = opt
        self.print = print
        self.question = "What do you want to do now?"
    def next(self):
        if self.print:
            print(self.str)
        going(ask(*self.opt, self.question)) if not self.question == None else going(ask(*self.opt))
class Scene(Action):
    def __init__(self, nickname, desc, next):
        super().__init__(nickname, desc, next, True)
        self.question = f"Where do you want to go from {self.nickname}?"
    def forth(self, to):
        self.next.append(to)
    def link(self, to):
        self.forth(to)
        to.forth(self)

def do(where):
    here = where

        