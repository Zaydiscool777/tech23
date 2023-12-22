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

print(main.ask(bla(['hello', 'lala']), other='other'))

print(main.x.next())
