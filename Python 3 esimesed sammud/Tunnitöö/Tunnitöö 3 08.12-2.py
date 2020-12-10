#Mark Metshein IT20
#08.12
#Sissetulekud
# fail = open("konto.txt","r")
# loeb = fail.readlines()
# for n in range(len(loeb)):
#     if float(loeb[n]) > 0:
#         print(loeb[n],end="")

#3.4 Jukebox
# kysimus = input("Sisestage faili nimi: ") 
# fail2 = open(kysimus+".txt","r")
# read = fail2.readlines()
# for n in range(len(read)):
#     print(str(n+1)+". "+read[n],end="")
# kysimus2 = int(input("\n\nMillist laulu soovite? "))
# print(read[kysimus2-1])

#Random Name Generator
# fail3 = open("nimekiri.txt","r")
# rida = fail3.readlines()
# from datetime import *
# print(rida[datetime.now().day-1])

#4.1 Bänner
# def banner(a):
#     r = a.upper()
#     return r
# nr = int(input("Mitu korda soovite reklaamlauset kuvada?: "))
# tekst = input("Sisestage reklaamlause: ")
# for i in range(nr):
#     print(banner(tekst))

#4.2 õunamahla tegemine
# ounad = int(input("Mitu õuna? :"))
# def mahlapakid(b):
#     mp=round(ounad*0.4/3,0)
#     mp=int(mp)
#     return mp
# print(mahlapakid(ounad))

#Peo eelarve
# def eelarve(k):
#     summa = k*10+55
#     return summa
# arv = int(input("Mitu inimest on kutsutud: "))
# arv2 = int(input("Mitu inimest tuleb: "))
# 
# print("Maksimaalne eelarve: ", eelarve(arv), "eurot")
# print("Minimaalne eelarve: ", eelarve(arv2), "eurot")

#Tervitused mõtisklustega
# def tervitus(n):
#     print(f"Võõrustaja: \"Tere!\" \n Täna {n}. kord tervitada, mõtiskleb võõrustaja. \n Külaline: \n""Tere, suur tänu kutse eest!\"")
# kylalised = int(input("Mitu külalist tuleb?: "))
# for i in range(kylalised):
#     tervitus(i+1)

#Mündid
# fail = open("myndid.txt")
# rida = fail.readlines()
# def pronksikarva_summa(m):
#     kassa = 0
#     for i in range(len(m)):
#         if int(m[i]) < 10:
#             kassa+=int(m[i])
#     print("Hoiupõrsasse läheb",kassa,"senti.")
# pronksikarva_summa(rida)

#Kuupäev
kuupaev = input("Sisestage kuupäev (DD.MM.YYYY): ")
def kuu_nimi(i):
    p,k,a = i.split(".")
    kuud = ('jaanuar', 'veebruar', 'märts', 'aprill', 'mai', 'juuni', 'juuli', 'august', 'september', 'oktoober', 'november', 'detsember')
    k = int(k)
    return kuud[k-1]
def kuupaev_s6nena(i):
    p,k,a = i.split(".")
    return p+". "+kuu_nimi(i)+" "+a+". a"


print(kuupaev_s6nena(kuupaev))





