teljes = []
kosar = []
with open("penztar.txt", "r") as bemenet:
    for sor in bemenet:
        adat = sor.strip()
        if adat != "F":
            kosar.append(adat)
        else:
            teljes.append(kosar)
            kosar = []
        
print("\n2.feladat")
count = 0
for f in teljes:
    count+=1
print("A fizetések száma:", count)

print("\n3.feladat")
egyes = len(teljes[0])
print("Az első vásárló", egyes, "darab árucikket vásárolt.")

print("\n4.feladat")
vasarlas = int(input("Adja meg egy vásárlás sorszámát! "))-1
aru = input("Adja meg egy árucikk nevét! ")
db = int(input("Adja meg a vásárolt darabszámot! "))
    
print("\n5.feladat")
count = 0
van = 0
flag = True
benne = 0
for kosar in teljes:
    count +=1
    if aru in kosar and flag:
        print("Az első vásárlás száma: ", count)
        flag = False
        benne +=1
    elif aru in kosar:
        van = count
        benne+=1
print("Az utolsó vásárlás száma: ", van)
print(benne, "vásárlás során vettek belőle.")

print("\n6.feladat")

def ertek(db):
    if db == 1:
        return 500
    elif db == 2:
        return 950
    elif db > 2:
        szam = db-2
        return 950 + szam*400
print(db, "db vételkor fizetendő:", ertek(db))    

print("\n7.feladat")
adott = teljes[vasarlas]
aruk = {}
for aru in adott:
    if aru not in aruk:
        aruk[aru] = 1
    elif aru in aruk:
        aruk[aru] +=1
for cikk in aruk.items():
    print(cikk[1], cikk[0])


with open ("osszeg.txt", "w") as kimenet:
    count = 0
    for kosar in teljes:
        count +=1
        valasz = ''
        valasz += str(count)
        valasz +=": "
        valasz += str(ertek(len(kosar)))
        kimenet.write(valasz)
        kimenet.write("\n")
    









