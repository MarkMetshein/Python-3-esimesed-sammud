#Mark Metshein
#20.11.2020
#Harjutus 2
##########aste on **#########
#####// võtab jäägi ära####
#1 Arvutame kolmnurga ümbermõõdu
import math
a,b,c=2,3,4
P=a+b+c
print("Kolmnurga ümbermõõt on "+str(P),"cm")
#2 Toote hind
a, b, c =36.75, 0.4, 3
d=(a-a*b)*3
print(c,"toote summa on "+str(d),"€")
#Pitsa
pitsa=12.9
inimesed=3
tip=12.9 * 0.1
kokku=pitsa+tip
maksmine=kokku/inimesed
print (inimesed,"inimest peavad maksma näo pealt "+str(maksmine),"€")
#Rulluisutajad
kiirus=29.9
aeg=24/60
dist=kiirus*aeg
print ("24 minutiga liigub ta " +str(dist),"km")
#Leia kolmnurga hüpotenuus
a, b=16,9
tehe=(a ** 2 + b ** 2)
arv = "Kolmnurga hüpotenuus on " +str(round(math.sqrt(tehe),2))+" 6cm"
print (arv)
#Ajateisendus
sisestus = int(input("Sisestage minutid: "))

tunnid = sisestus // 60
minutid = sisestus % 60

vastus = "{}:{}".format(tunnid, minutid)
print(vastus)
#Arvusüsteemid
sisestus = int(input("Sisestage täisarv kümnendsüsteemis: "))
print("Sisestatud täisarv", sisestus, "on:")
print(bin(sisestus), "kahendsüsteemis.")
print(hex(sisestus), "kuueteistkümnendsüsteemis.")
#Kütusekulu arvutamine
distants = float( int(input ("Sisestage läbitud kilomeetrid: ")))
kutus = float( int(input ("Sisestage tangitud kütus liitrites: ")))
kulu = distants / kutus
print ("100km sõitmiseks kulub " + str(kulu) + " liitrit bensiini")