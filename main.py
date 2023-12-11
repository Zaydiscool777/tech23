import csv
here = None
def ask(*options, question="What do you do?"):
    print("\t\b", question, '\n\t')
    for i in options:
        print(f"\t{i[0]}: {i[1]}")
    return input('\t:o~~>')
class Scene:
    def __init__(self, location, nickname, next):
        self.location = location
        self.next = next
        self.nickname = nickname
    def move(self):
        ask(*[i[0], i[1] for i in self.next], question=f"Where do you want to go from {self.nickname}?")
        