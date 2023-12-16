import csv
here = None
doing = None
f = open("data.csv", 'r+')
read = [i[1] for i in csv.reader(f)]
places = {}

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
    def __init__(self, nickname: str, desc: str, next=None):
        super().__init__(nickname, desc, next, True)
        self.question = f"Where do you want to go from {self.nickname}?"
    def forth(self, to):
        self.next.append(to)
    def link(self, to):
        self.forth(to)
        to.forth(self)

def do(where=read[0], doingp=read[1]):
    print("...") #oh no dont leave
    global here
    global doing
    global f
    read[0] = (here := where)
    read[1] = (doing := doingp)
    f.truncate(0)
    csv.writer(f).writerow("location", read[0])
    csv.writer(f).writerow("action", read[1])
    print('')#ok now

g = open('obj.py')    
exec(g.read())
g.close()
    
def step():
    pass

#do(1, 2)
#print(here)