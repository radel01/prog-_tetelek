from Szek import Szek


def peldanyositas():
    peldany1 = Szek("kék", 3)
    peldany2 = Szek("piros", 4)
    peldany3 = Szek("zöld", 5)

    szekek = [peldany1, peldany2, peldany3]
    return szekek


def listakiiras(lista):
    for index in range(0, len(lista), 1):
        print(lista[index])


listakiiras(peldanyositas())


def beolvasas():
    lista = []
    beFajl = open("szekAdatok.txt", "r", encoding="utf-8")
    beFajl.readline()
    sorok = beFajl.readlines()
    for index in range(0, len(sorok), 1):
        daraboltSor = sorok[index].strip().split("@")
        peldany = Szek(daraboltSor[0], daraboltSor[1])
        lista.append(peldany)
        print(lista[index])
    return lista


beolvasas()