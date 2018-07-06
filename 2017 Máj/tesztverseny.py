print("1.feladat")
print("Az adatok beolvasása")

with open ("valaszok.txt", "r") as bemenet:
    flag = True
    eredmenyek = {}
    for sor in bemenet:
        if flag == True:
            helyesvalasz = sor.strip()
            flag = False
        else:
            adat = sor.strip().split()
            versenyzo = adat[0]
            megoldas = adat[1]
            eredmenyek[versenyzo] = megoldas

print("\n2. feladat")
count = 0
for tag in eredmenyek:
    count+=1
print("A vetélkedőn", count, "versenyző indult.")

print("\n3. feladat")
azon = input("A versenyző azonosítója = ")
valasz = eredmenyek[azon]
print(valasz, "(A versenyző válasza)")
valasz = list(valasz)

print("\n4. feladat")
print(helyesvalasz, "(a helyes megoldás)")
jovalasz = list(helyesvalasz)
valaszcheck = ""
for betu in range(len(jovalasz)):
    if jovalasz[betu] == valasz[betu]:
        valaszcheck += "+"
    else:
        valaszcheck += " "
print(valaszcheck, "(a versenyző helyes válaszai)")

print("\n5. feladat")
feladat = int(input("A feladat sorszáma = "))
helyesbetu = jovalasz[feladat-1]
jocount = 0
for betuk in eredmenyek:
    adottvalasz = list(eredmenyek[betuk])
    if adottvalasz[feladat-1] == helyesbetu:
        jocount +=1
szazalek = round((jocount/count)*100, 2)        
print("A feladatra", jocount, "fő, a versenyzők", str(szazalek)+"%-a adott helyes választ")


print("\n6.feladat")
print("A versenyzők pontszámának meghatározása")

def pontszam(kodnev):
    pontok = 0
    adottvalasz = list(eredmenyek[kodnev])
    for num in range(5):
        if jovalasz[num] == adottvalasz[num]:
            pontok +=3
    for num in range(5, 10):
        if jovalasz[num] == adottvalasz[num]:
            pontok +=4
    for num in range(10, 13):
        if jovalasz[num] == adottvalasz[num]:
            pontok +=5
    if jovalasz[13] == adottvalasz[13]:
            pontok +=6
    return pontok

with open("pontok.txt", "w") as kimenet:
    for kodnev in eredmenyek:
        kimenet.write(kodnev)
        kimenet.write(" ")
        kimenet.write(str(pontszam(kodnev)))
        kimenet.write("\n")
        

print("\n7. feladat: A verseny legjobbjai:")
legjobb1 = [0, 0]
legjobb2 = [0, 0]
legjobb3 = [0, 0]
pontszamok = {}
for kodnev in eredmenyek:
    kod = [kodnev]
    adottpont = pontszam(kodnev)
    if adottpont in pontszamok:
        pontszamok[adottpont].append(kodnev)
    else:
        pontszamok[adottpont] = kod
       
for adottpont in pontszamok:
    if adottpont > legjobb1[0]:
        legjobb1 = [0,0]
        legjobb1[0] = adottpont
        legjobb1[1] = pontszamok[adottpont]
        
del pontszamok[legjobb1[0]]

for adottpont in pontszamok:
    if adottpont > legjobb2[0]:
        legjobb2 =[0,0]
        legjobb2[0] = adottpont
        legjobb2[1] = pontszamok[adottpont]
        
del pontszamok[legjobb2[0]]

for adottpont in pontszamok:
    if adottpont > legjobb3[0]:
        legjobb3 = [0,0]
        legjobb3[0] = adottpont
        legjobb3[1] = pontszamok[adottpont]

pont1 = legjobb1[0]
pont2 = legjobb2[0]
pont3 = legjobb3[0]
jatekosok1 = legjobb1[1]
jatekosok2 = legjobb2[1]
jatekosok3 = legjobb3[1]

for top1 in jatekosok1:
    print("1. díj ("+str(pont1)+" pont):", top1)

for top2 in jatekosok2:
    print("2. díj ("+str(pont2)+" pont):", top2)

for top3 in jatekosok3:
    print("3. díj ("+str(pont3)+" pont):", top3)













    
