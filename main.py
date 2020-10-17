import csv


invObjs = []

with open('MAKEathon/Inventar_makeathon.csv', newline='') as f:
    objs = list(csv.reader(f, delimiter=';'))
print(objs)

for el in objs:
    invObjs.append(InvObj(el[0], el[1]))

for el in invObjs:
    print(el.cpe)


class InvObj:
    def __init__(self, cpe, ip):
        self.cpe = cpe
        self.ip = ip
