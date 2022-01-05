class Employee:
    def __init__(self, first, last):
        self.nameFirst = first
        self.nameLast = last
        self.nickname = ""
        self.nameFull = self.nameFirst + ' ' + self.nameLast

Minion1 = Employee('Greg', 'Kapler')
Minion1.nickname = 'Kaplermeister'

print(Minion1.nameFirst + ' "' + Minion1.nickname + '" ' + Minion1.nameLast)