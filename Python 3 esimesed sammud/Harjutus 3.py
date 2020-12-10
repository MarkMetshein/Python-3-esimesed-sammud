#MM IT20
#24.11.2020
#Ülesanne 3
########Email################
email = input("Mis on Teie email?: ")
print("@" in email)
########Korralik nimi####################
#küsib nime
nimi = input("Mis on Teie nimi?: ")
#teeb nime korrektseks + väljund
nimi = (nimi.strip()).capitalize()
print("Tere, " , nimi , "!")
##########Vandumine###################
sona = input("Sisestage sõna: ").lower()
print(sona.replace('kurat', '*****'))
#########Tundide ajad##############
#input
start = input("Mis kell algasid tunnid?: ")
lopp = input("Mis kell lõppesid tunnid?: ")
#kestvus = lopp - start
tund, minut = start.split(':')
tund2, minut2 = lopp.split(':')
#aja teisaldamine minutiteks
aeg = int(tund)*60+int(minut)
aeg2 = int(tund2)*60+int(minut2)
aegade_vahe = aeg2 - aeg
#tagasi teisaldamine tundideks ja minutiteks
viimane = aegade_vahe / 60
print("Koolipäev kestis", viimane , "tundi!")
###########Palindroom#############
# funktsioon, mis kontrollib tagurpidi kirja vist
def isPalindrome(s):
    return s == s[::-1]
#küsimus
kusimus = input("Sisestage palindroom: ")
ans = isPalindrome(kusimus)
#if/else väide
if ans:
    print("Sisestatud tekst on palindroom!")
else:
    print("Sisestatud tekst pole palindroom!")
    