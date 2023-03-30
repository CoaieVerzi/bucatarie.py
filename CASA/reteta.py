# from CASA.bucatarie import scoatem
# from CASA.bucatarie import adaugam


continut = {
    "faina": 500,
    "zahar": 500,
    "sare": 500,
    "lapte": 500,
    "oua": 500,
    "unt": 500
}



class Reteta():
    def __init__(self, nume, ingrediente):
        self.nume = nume
        self.ingrediente = ingrediente

reteta_tiramisu = Reteta("Tiramisu", {
    "faina": 50,
    "zahar": 50,
    "sare": 5,
    "lapte": 600,
    "oua": 3,
    "unt": 100
})



def tiramisu(reteta, continut):
    for ingredient, quantity in reteta.ingrediente.items():
        if ingredient in continut:
            continut[ingredient] -= quantity
            if continut[ingredient] < 0:
                raise ValueError(f"Nu exista suficient {ingredient} in continut pentru reteta {reteta.nume}.")
        else:
            raise ValueError(f"{ingredient} nu exista in continut.")



tiramisu(reteta_tiramisu, continut)


print(continut)