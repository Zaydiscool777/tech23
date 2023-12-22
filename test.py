import main

# understanding line 56

class Thing():
	def __init__(self, hello, str):
		self.hello = hello
		self.str = str

poo = {
	'hello': Thing(314, 'hi'),
	'lala': Thing(89, 'la'),
	'notmuch': Thing(404, 'no')
}

def bla(x):
	return [[poo[i].str, poo[i].hello] for i in x]

this = bla(['hello', 'lala'])
for i in this:
	print(i[1])

def ask(options: list, question="What do you do?", other=""):
	print("\t\b", question, '\n\t')
	for i in options:
		print(f"\t{i[0]}: {i[1]}")
	if (x := input('\tة<( ')) in options: return x
	elif x == 'quit':
		save()
		exit(0)
	else: return other

print(ask(bla(['hello', 'lala'])))