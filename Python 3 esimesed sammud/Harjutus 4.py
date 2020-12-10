#MM IT20
#25.11.2020
# #Ülesanne 4
#####IF#####
#Ruut
#sisend
kulg1 = (input("Sisestage esimene külg: "))
kulg2 = (input("Sisestage teine külg: "))
#if else
if kulg1 == kulg2:
    print("Tegemist on ruuduga!")
else:
    print("Tegemist ei ole ruuduga!")

#Matemaatika
arv1 = int(input("Sisestage esimene arv: "))
arv2 = int(input("Sisestage teine arv: "))
tehe = input("Kas soovite teha (+-/*) tehet?: ")
if tehe == "+":
    print(f"{arv1}+{arv2}={arv1+arv2}")
elif tehe=="-":
    print(f"{arv1}-{arv2}={arv1-arv2}")
elif tehe=="/":
    print(f"{arv1}/{arv2}={arv1/arv2}")
elif tehe=="*":
    print(f"{arv1}*{arv2}={arv1*arv2}")

# #Juubel
aasta = int(input("Sisestage sünniaasta: "))
vanus = 2020-aasta
if vanus%5==0:
     print("Juubel!")
else:
     print("Ei ole juubel!")
     
#Müük
hind = int(input("Sisestage toote hind: "))
if hind <= 10:
     ale = 0.1
     print ("Saate 10% allahindlust")
else:
     ale = 0.2
     print ("Saate 20% allahindlust")
summa = hind-hind*ale
print (summa)
 
#Jalgpalli meeskond
vanus = int(input("Sisestage enda vanus: "))
sugu = input("Kas olete mees või naine?(M/N): ")
if 16 <= vanus < 18 and sugu=="M":
     print("Sobite meeskonda!")
else:
     print("Ei sobi meeskonda!")
 
#####While, For#####
#Tärnid
for i in range(1,6):           #read
    for j in range(1,6):       #veerud
        print('* ', end='')
    print()                     #lihtsalt print() lisab ainult reavahetuse
 
# #Loto
import random
print(random.randint(10000,99999))
 
#Paaris ja paaritu
import random
num = random.randint(1,100)
if (num % 2) == 0:  
   print("{0} on paarisarv".format(num))  
else:  
   print("{0} on paaritu arv".format(num))  
#Pisike korrutustabel
n = 5
 
#loopib 10 korda
for i in range(1,11):
   print(n,'x',i,'=',n*i)
 
#Viisikud
lower = 0
upper = 100
for i in range(lower, upper+1):
   if((i%5==0)):
      print(i)

#Arvamismäng - arva ära number 1-50
import random
n = random.randint(1, 10)
guess_count = 0
guess_limit = 2      #tegelik kordade arv on 3
while guess_count <= guess_limit :
    guess = int(input("Arvake ära number 1-10: "))
    guess_count += 1    
    if guess == n:
        print("Õige! See arv oli", n, ", Tubli!")
        break
else:

    print ("Vabandust, korrektne arv oli", n,"." "Kas soovite uuesti proovida?")

#Pank
konto = 10000
aeg = 5
intress = 0.05
alg = konto
print("Aasta \t Algsumma \t Intress \t Aasta lõpus")
for i in range(aeg):
    algsumma = konto
    konto = konto+konto*intress
    print(f"{i+1} \t {algsumma:.2f} \t {algsumma*intress:.2f} \t {konto:.2f}")
kasum = konto-alg
 
print(f"Summa kokku: {kasum:.2f}€")
print(f"Kasum: {alg}€")
 
#Ruutude ja kuupide tabel
def square(i):
    return(i*i)
def cube(i):
    return (i*i*i)

print ("mingi tekst")

start1 = 1
start2 = 11
print("Number Ruudus Kuubis")

for i in range(start1,start2):
    print(i,"\t", square(i),"\t",cube(i))

