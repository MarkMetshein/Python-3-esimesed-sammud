#############MM IT20#############
#############26.11.2020#############
#############Ülesanne 5#############
#Nimede lisamine loendisse - korras
nimi1 = input("Sisestage esimene nimi: ")
nimi2 = input("Sisestage teine nimi: ")
nimi3 = input("Sisestage kolmas nimi: ")
nimi4 = input("Sisestage neljas nimi: ")
nimi5 = input("Sisestage viies nimi: ")
x = nimi1, nimi2, nimi3, nimi4, nimi5
sorteeritud = sorted(x)
print(sorteeritud)
print("Viimati lisatud nimi: "+(nimi5))

# Õpilased
opilased = ["Juhan","Kati","Maarja","Mario","Mati"]
print(opilased)
valik = input("Millist nime soovite asendada?: ")
if valik in opilased:
    opilased.remove(valik)
    print('Nimekirjast eemaldatud:',valik)
else:
    print('Sellist nime pole!')
uus = input("Sisestage uus nimi: ")
uued = uus, opilased
print(uued)

#Duplikaadid
opilased = ["Juhan","Kati","Mario","Mario","Mati","Mati"]
#ei väljasta kordusi
opilased = list(dict.fromkeys(opilased))
print(opilased)

#Vanused
vanused = [33, 16,8,12,40]
suurim = max(vanused)
vaikseim = min(vanused)
print(vanused)
keskmine = sum(vanused) / len(vanused)
print("Kõige väikseim number nimekirjas on", min(vanused))
print("Kõige suurem number nimekirjas on", max(vanused))
x = sum(vanused)
print("Numbrite kogusumma on", (x))
print("Numbrite keskmine on", (keskmine))

#Tärnid
numbrid = [23,63,72,10,24,98]
print(23 * '*')
print(63 * '*')
print(72 * '*')
print(10 * '*')
print(24 * '*')
print(98 * '*')