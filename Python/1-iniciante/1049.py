tipo1 = input()
tipo2 = input()
tipo3 = input()

if tipo1 == "vertebrado":
    if tipo2 == "ave":
        if tipo3 == "carnivoro":
            print("aguia")
        else:
            print("pomba")
    elif tipo2 == "mamifero":
        if tipo3 == "onivoro":
            print("homem")
        else:
            print("vaca")
            
if tipo1 == "invertebrado":
    if tipo2 == "inseto":
        if tipo3 == "hematofago":
            print("pulga")
        else:
            print("lagarta")
    elif tipo2 == "anelideo":
        if tipo3 == "hematofago":
            print("sanguessuga")
        else:
            print("minhoca")