#############MM IT20################
#############02.12.2020#############
#############Harjutus 7#############

#funktsiooni loomine
# def tervitus(keel="de"):
#     "Tervituse funktsioon"
#     keel = input("Sprache wählen? (en, et, ge): ")
#     if keel == "et":
#         nimi = input("Mis on teie nimi?: ")
#         return("Tere, " + nimi)
#     if keel == "en":
#         nimi = input("What's your name?: ")
#         return("Hi, " + nimi)    
#     else:
#         nimi = input("Wie ist Ihr Name?: ")
#         return("Hallo, " + nimi)
# 
# print(tervitus())
#######Leiame ruumala######
import math
def kuup():
    x = int(input("Sisestage üks külg: "))
    v = pow(x, 3)
    return v

def kera():
    x = int(input("Sisestage kera raadius: "))
    v = 4/3 * math.pi * pow(x, 3)
    return v

def koonus():
    return v

def silinder():
    return v


def app(loop):
    while loop == 1:
        print("Tee valik")
        print("1. Kuup")
        print("2. Kera")
        print("3. Koonus")
        print("4. Silinder")
        print()
        valik = int(input("Tehke valik 1-4: "))
        
        if valik == 1:
            print("Valisite kuubi!")
            print(f"Kuubi ruumala on {kuup()}")
        if valik == 2:
            print("Valisite kera!")
            print(kera())
        if valik == 3:
            print("Valisite koonuse!")
            print(koonus())
        if valik == 4:
            print("Valisite silindri!")
            print(silinder())

app(1)

    



