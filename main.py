#!/bin/python3

# preparing
import csv
write = [None, None, [], []]
f = open("data.csv", 'r+')
read = [i[1] for i in csv.reader(f)]

def save(*save):
	print("...") #oh no dont leave
	global write
	for i in enumerate(save):
		write[i[0]] = i[1]; read[i[0]] = write[i[0]] # what happened to mr. walrus
	f.truncate(0)
	csv.writer(f).writerow(["location", read[0]])
	csv.writer(f).writerow(["action", read[1]])
	csv.writer(f).writerow(["battle", *read[2]])
	csv.writer(f).writerow(["inventory", *read[3]])
	# TODO: fix everything else for battle
	print('')#ok now
# ask function
def ask(options: list, question="What do you do?", other=""):
	print("\t\b", question, '\n\t')
	for i in options:
		print(f"\t{i[0]}: {i[1]}")
	if (x := input('\tة<( ')) in [i[0] for i in options]: return x
	elif x == 'quit': save(*write); exit(0) # 
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
			return self.dict[ask(self.opt, self.question) if self.question is not None else ask(self.opt)]
	def __repr__(self):
		return f"{self.id}\n{self.nickname}\nclass: {self.__class__.__name__}\n\
    	{self.str}\n{self.question}({self.print})\n{[self.id for i in self.opt]}"

scenes = {}
class Scene(Action):
	def __init__(self, id: str, nickname: str, desc: str, *nextl):
		super().__init__(id, nickname, desc, [[scenes[i].nick, scenes[i].str] for i in nextl], True, scenes)		
		self.question = f"Where do you want to go from {self.nickname}?"
		for i in [self.dict[i] for i in nextl]:
			# i finally fixed it!!!
			self.opt.append([i.nickname, i.str])
			i.opt.append([self.nickname, self.str])
	def forth(self, to):
		self.opt.append([to.nickname, to.str])
	def link(self, to):
		self.forth(to)
		to.forth(self)
idk = {}
class Attack(Action):
	def __init__(self, id: str, name: str, desc: str, does: list):
		super().__init__(id, name, desc, [], False, idk)
		self.init = False
	def __call__(self, is_op: bool):
		if not self.init:
			self.init = True
			return 0
		return [i[1] + does[i[0]] for i in enumerate(write[3])]
opps = {}
class Battle(Action):
	def __init__(self, id: str, name: str, desc="yea", *attacks):
		super().__init__(id, name, desc, attacks, False, opps)

#--- adding to the dicts  --#

# switch to json? i mean... vvv
#:village -> :village:goat -> :village:goat;milk -> :village:goat;slaughter!

def SET():
	Scene(':village', 'the village',
		"A village.")
	Scene(':village:shop', 'the shop', 
		"A shop with three merchants.", 
		':village')
	Scene(':village:shop:1', 'the first merchant', 
		"A merchant that can sell various items")
	Scene(':village:shop:2', 'the second merchant',
		"A merchant that can sell various items",
		':village:shop:1', ':village:shop')
	Scene(':village:shop:3', 'the third merchant', 
		"A merchant that can sell various items",
		':village:shop:1', ':village:shop:2', ':village:shop')


#--- thank you for coming --#
SET()
def step():
	if write[2] != []:
		pass
