#30.11
#Mark Metshein
#Kodutöö 1

#Tervitus
# print("Tere, maailm!")
# 
#Aasta liblikas - vale
# aasta = 2020
# liblikas = "teelehe mosaiikliblikas"
# lause_keskosa = ". aasta liblikas on "
# lause = str(aasta) + lause_keskosa + liblikas
# print(lause)


# #Pilved
# kusimus = float(input("Mis on pilvede aluse kõrgus? (kilomeetrites) "))
# if kusimus > 6:
#     print("Need on ülemised pilved!")
# else:
#     print("Need ei ole ülemised pilved!")

#Bussid
# inimesed = int(input("Kui mitu inimest? "))
# kohad = int(input("Mitu kohta on bussis? "))
# if kohad > inimesed:
#     print("Vaja on ühte bussi")
# else:
#     if inimesed%kohad == 0:
#         print("Vaja on" + " " + str((inimesed//kohad)) + " " +  "bussi")
#         print("Viimases bussis on " + str(kohad))
#     else:
#         print("Vaja on" + " " + str((inimesed//kohad+1)) + " " +  "bussi")
#         print("Viimases bussis on " + str(inimesed%kohad) + " " + "inimest")

#äratus
# äratus = int(input("Mitu äratust? "))
# for i in range(äratus):
#     print("Tõuse ja sära!")

#Murelikud lapsevanemad
porgand = 0
kusimus= abs(int(input("Sisestage ringide arv: ")))
i = 1
while i <= kusimus:
    if i % 2 == 0:
        porgand=porgand + i 
    i += 1
print(f"Jänku jooksis {i -1} ringi")
print(f"Porgandeid kokku {porgand} porgandit")
# print("Jänku jooksis" + " " + str(kusimus) + " " + "ringi")








