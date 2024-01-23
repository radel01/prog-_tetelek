from Szek import Szek

peldany1 = Szek("kék", 3)
peldany2 = Szek("piros", 4)
peldany3 = Szek("zöld", 5)

# print(peldany1.__str__())
# print(peldany2.__str__())
# print(peldany3.__str__())

szekek = [peldany1, peldany2, peldany3]


def labakSzama():
    print("I.")
    ossz = 0
    for index in range(0, len(szekek), 1):
        ossz += szekek[index].labszam
    print(f"\tÖsszesen ennyi székláb van a teremben: {ossz} db")


labakSzama()


def maxLabSzine():
    print("II.")
    maxLabIndex = 0
    for index in range(1, len(szekek), 1):
        if szekek[maxLabIndex].labszam > szekek[index].labszam:
            maxLabIndex = index
    return szekek[maxLabIndex].szin


print(f"\tA legtöbb lábú szék színe: {maxLabSzine()}")


def negyneltobb():
    print("III.")
    db = 0
    for index in range(0, len(szekek), 1):
        if szekek[index].labszam > 4:
            db += 1
    return db


print(f"\tNégynél több lábú székek száma: {negyneltobb()} db")


def vanepirosnegylabu():
    print("IV.")
    van_e = False
    index = 0
    while index < len(szekek) and van_e == False:
        if (szekek[index].labszam == 4) and (szekek[index].szin == "piros"):
            van_e = True
        index += 1
    return van_e


print(f"\tVan-e négylábú piros szék? {vanepirosnegylabu()}")
