import csv
import cpe_utils
import json

invObjs = []

with open('MAKEathon/Inventar_makeathon.csv', newline='') as f:
    objs = list(csv.reader(f, delimiter=';'))
print(objs)

for el in objs:
    invObjs.append(InvObj(el[0], el[1]))

for x in invObjs:
    print(x.part)


class InvObj:
    def __init__(self, cpe, ip):
        self.cpe = cpe
        self.ip = ip
        self.cpeJson = json.loads(cpe_utils.CPE(cpe).to_json())

        if (self.cpeJson["part"] == "a"):
            self.part = "Application"
        elif (self.cpeJson["part"] == "o"):
            self.part = "Operating System"
        else:
            self.part = "Hardware"

    def get_cpe(self):
        return self.cpe
