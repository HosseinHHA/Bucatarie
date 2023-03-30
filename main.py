from src.bucatarie import Bucatarie

inventar = {}
print(Bucatarie.adaugaIngredient(inventar))
print(inventar)


Bucatarie.scadeInventar('oua', 7, inventar)
print(inventar)