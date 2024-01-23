class Szek:

    def __init__(self, szin:str, labszam:int ):
        self.szin=szin
        self.labszam=int(labszam)

    def __str__(self):
        return (f"szín: {self.szin}, lábszám: {self.labszam}")