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
def ask(options: list, question="What do you do?", other=""):
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
	def __init__(self, id: str, nickname: str, str: str, opt: list, print: bool, dict=actions) -> None:
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
			#save(ask(*self.opt, self.question)) if not self.question == None else save(ask(*self.opt))
			# until save fixed
			return ask(self.opt, self.question) if self.question is not None else ask(self.opt)
	def __repr__(self):
		return f"{self.id}\n{self.nickname}\nclass: {self.__class__.__name__}\n{self.str}\n{self.question}({self.print})\n{[i.id for i in self.opt]}"

scenes = {}
class Scene(Action):
	def __init__(self, id: str, nickname: str, desc: str, *nextl):
		super().__init__(id, nickname, desc, [[scenes[i].id, scenes[i].str] for i in nextl], True, scenes)
		self.question = f"Where do you want to go from {self.nickname}?"
		for i in [self.dict[i] for i in nextl]:
			self.opt.append(i)
			i.opt.append(self)
	def forth(self, to):
		self.opt.append(to)
	def link(self, to):
		self.forth(to)
		to.forth(self)
	
#--- adding to the dicts  --#

# switch to json? i mean... vvv
#:village -> :village:goat -> :village:goat;milk -> :village:goat;slaughter!

Scene(':village', 'the village', "A village.")
Scene(':village:shop', 'the shop', "A shop with three merchants.", ':village')
Scene(':village:shop:1', 'the first merchant', "A merchant that can sell various items")
Scene(':village:shop:2', 'the second merchant',
	"A merchant that can sell various items",
	':village:shop:1')
Scene(':village:shop:3', 'the third merchant', 
	"A merchant that can sell various items",
	':village:shop:1', ':village:shop:2')

print(scenes[':village'].__repr__())
x = scenes[':village']
#while True:
#	print( (x := scenes[x.next()]) )

#--- thank you for coming --#

def step():
	pass