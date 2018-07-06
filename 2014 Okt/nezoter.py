with open ("foglaltsag.txt", "r") as bemenet:
    nezoter = []
    sorszam = 0
    for sor in bemenet:
        sorszam += 1
        szeksor = sor.strip()
        szekek = [sorszam]
        for letter in szeksor:
            szekek.append(letter)
        nezoter.append(szekek)


with open("kategoria.txt", "r") as kat:
    arak = []
    sorszam = 0
    for sor in kat:
        sorszam += 1
        sorar = sor.strip()
        szekarak = [sorszam]
        for number in sorar:
            szekarak.append(int(number))
        arak.append(szekarak)


print("\n2.feladat")
print("Megnézem, hogy egy adott hely szabad-e.")
sor = int(input("Adja meg egy sornak a számát!(1-15)"))
szek = int(input("Adja meg a szék számát az adott sorban(1-20)!"))

for sorszam in range(1, 16):
    if sorszam == sor:
        adottsor = nezoter[sorszam-1]
        for szekszam in range(1, 21):
            if szekszam == szek:
                if adottsor[szek] == "x":
                    print("foglalt")
                elif adottsor[szek] == "o":
                    print("szabad")

            
print("\n3.feladat")
count = 0
for sor in range(15):
    adottsor = nezoter[sor]
    for letter in adottsor:
        if letter == "x":
            count +=1
szazalek = (count/(15*20))*100
szazalek = round(szazalek)
print("Az előadásra eddig", count, "jegyet adtak el, ez a nézőtér", str(szazalek)+"%-a.")

print("\n4.feladat")
kat1 =0
kat2 =0
kat3 =0
kat4 =0
kat5 =0
for sor in range(15):
    adottsor = nezoter[sor]
    adottarak = arak[sor]
    for letternum in range(len(adottsor)):
        if adottsor[letternum] == "x":
            num = adottarak[letternum]
            if num == 1:
                kat1 +=1
            elif num == 2:
                kat2 +=1
            elif num == 3:
                kat3 +=1
            elif num == 4:
                kat4 +=1
            elif num == 5:
                kat5 +=1
            
                
maxkat = 0
kat = 0
if maxkat < kat1:
    maxkat = kat1
    kat = "1."

if maxkat < kat2:
    maxkat = kat2
    kat = "2."
    
if maxkat < kat3:
    maxkat = kat3
    kat ="3."

if maxkat < kat4:
    maxkat = kat4
    kat ="4."
if maxkat < kat5:
    maxkat = kat5
    kat ="5."

print("A legtöbb jegyet a(z)", kat, "árkategóriában értékesítették.")

print("\n5.feladat")
osszbev = 0
bev1 = 5000*kat1
bev2 = 4000*kat2
bev3 = 3000*kat3
bev4 = 2000*kat4
bev5 = 1500*kat5
osszbev = bev1 + bev2 + bev3 + bev4 + bev5
print("A színház bevétele a jelenleg eladott jegyek alapján:", osszbev, " Ft lenne.")

""" ez nem jo, osszbevteles
"""

print("\n6. feladat")
ossz = 0
for sor in range(15):
    adottsor = nezoter[sor]
    count = 0
    if adottsor[20] == "o" and adottsor[19] == "x":
        ossz +=1
    for szek in adottsor:
        if szek == "o":
            count +=1
        elif szek == "x":
            if count == 1:
                ossz +=1
            count = 0
print("Összesen", ossz, "egyedülálló üres hely van.")
def katkeres (sor, szek):
    for sorok in range(15):
        if sorok == sor:
            keressor = arak[sor]
            return keressor[szek]

    
with open ("szabad.txt", "w") as kimenet:
    for sor in range(15):
        adottsor = nezoter[sor]
        for szek in range(1, 21):
            if adottsor[szek] == "x":
                kimenet.write("x")
            elif adottsor[szek] == "o":
                kimenet.write(str(katkeres(sor, szek)))
        kimenet.write("\n")
        

        
            
        





















        
