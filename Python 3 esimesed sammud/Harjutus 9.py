#IT20
#Mark Metshein
#Harjutus 9
#09.12.2020
#50003304723
ik = input("Sisestage oma isikukood: ")

if len(ik) == 11:
    p = ik[6:7]
    k = ik[4:5]
    a = ik[1:3]
    print(f"{p}.{k}.{a}")