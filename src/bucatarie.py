import pickle


class Bucatarie:
    def __init__(self, nume):
        self.nume = nume
        self.inventar = {}

    def salvare_inventar(self):
        with open('my_object.pickle', 'wb') as f:
            pickle.dump(self.inventar, f)

    def initializare_inventar(self):
        with open('my_object.pickle', 'rb') as f:
            loaded_object = pickle.load(f)

        print(loaded_object)
    def adauga_inventar(self, nume, cantitate):
        if nume not in self.inventar.keys():
            self.inventar[nume] = cantitate
        else:
            self.inventar[nume] += cantitate
        self.salvare_inventar()



    def scada_inventar(self, nume, cantitate):
        if nume not in self.inventar.keys():
            raise ValueError(f"nu avem {nume}")

bucatarie_Hossein = Bucatarie("Bucatarie lui Hossein")
bucatarie_Hossein.adauga_inventar("piper", 50)
print(bucatarie_Hossein.inventar)

bucatarie_Hossein.scada_inventar("apa", 50)
print(bucatarie_Hossein.inventar)

