import random

house1 = ["Lea", "Agus"]
house2 = ["Mama", 'Vitu', 'Juampi']
house3 = ["Marijo", "JB"]
house4 = ["Fran"]
houses = [house1] + [house2] + [house3] + [house4]


def delete_name_from_house(name):
    for h in houses:
        if name in h:
            h.remove(name)


def houses_do_not_have_person():
    for h in houses:
        if len(h) != 0:
            return False
    return True

paire = []
# random_house_1 = random.choice(houses)
# print(random_house_1)
while not houses_do_not_have_person():
    random_house_1 = random.choice(houses)
    random_house_2 = random.choice(houses)
    # print(random_house_2)
    # print(random_house_1)
    if random_house_1 is random_house_2:
        print("continue")
        continue
    else:
        name1 = random.choice(random_house_1)
        name2 = random.choice(random_house_2)
        paire.append((name1, name2))
        delete_name_from_house(name1)
        delete_name_from_house(name2)
        if len(random_house_1) == 0:
            houses.remove(random_house_1)
        if len(random_house_2) == 0:
            houses.remove(random_house_2)
print(paire)


# paire = [('Fran', 'Juampi'), ('Mama', 'JB'), ('Agus', 'Marijo'), ('Lea', 'Vitu')]
moment =[ 'Aperitivo','Entrada','Plato principal','Postre']

quien_hace_que = []
for m in moment:
    p = random.choice(paire)
    quien_hace_que.append((m, p))
    paire.remove(p)

for qhq in quien_hace_que:
    print(qhq)