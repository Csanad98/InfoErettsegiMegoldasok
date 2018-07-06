teljes = []

with open ("jarmu.txt", "r") as bemenet:
    for sor in bemenet:
        adat = sor.strip().split()
        teljes.append(adat)
print("\n2.feladat")
kezdes = 24
vege = 0
for adat in teljes:
    if int(adat[0]) < kezdes:
        kezdes = int(adat[0])
    
for adat in teljes:
    if int(adat[0]) > vege:
        vege = int(adat[0])
vege +=1
munka = vege - kezdes
print("Legalább", munka, "órát dolgoztak")

print("\n3.feladat")

adat1 = teljes[0]
ora = int(adat1[0])
for adat in teljes:
    if int(adat[0]) == ora:
        print(ora, "óra:", adat[3])
        ora +=1
    
print("\n4.feladat")
B = 0
K = 0
M = 0
G = 0

for adat in teljes:
    betu = adat[3]
    betu = betu[:1]
    if betu == "B":
        B +=1
    elif betu =="K":
        K +=1
    elif betu == "M":
        M+=1
    else:
        G+=1

print("Buszok száma:", B,"\n", "Kamionok száma:", K,"\n", "Motorok száma:", M,"\n", "Személygépkocsik száma:", G)

def mpbe (ora, perc, mp):
    orak = int(ora)*60*60
    percek = (int(perc))*60
    mpek = int(mp)
    ido = orak + percek + mpek
    return ido

print ("\n5.feladat")
mentes = 0
elozo = teljes[0]
elozomp = mpbe(elozo[0], elozo[1], elozo[2])
for adat in teljes:
    if (mpbe(adat[0], adat[1], adat[2]) - elozomp) > mentes:
        mentes = mpbe(adat[0], adat[1], adat[2]) - elozomp
        kezdes = elozo
        elozo = adat
        elozomp = mpbe(elozo[0], elozo[1], elozo[2])
    else:
        elozomp = mpbe(adat[0], adat[1], adat[2])
        

print(str(kezdes[0])+":"+str(kezdes[1])+":"+str(kezdes[2]), "-", str(elozo[0])+":"+str(elozo[1])+":"+str(elozo[2]))    

print("\n6.feladat")
keres = input("Adja meg a keresett rendszámot, *-gal helyettesítve az ismeretlen karaktereket!")
keres = list(keres)
egyezok = []
flag = True
for adat in teljes:
    rendsz = list(adat[3])
    for n in range(len(keres)):
        if keres[n] != "*":
            if keres[n] != rendsz[n]:
                flag = False
    if flag == True:
        egyezok.append(rendsz)
    flag = True
print("\nAz illeszthető rendszámok:")    
    
for rendsz in egyezok:
    out = ''
    for char in rendsz:
        out +=char
    print("\n"+out)


"""7.feladat"""
with open("vizsgalt.txt", "w") as kimenet:
    elz = teljes[0]
    def rendsz (adat):
        rendsz = ''
        print(adat)
        for n in adat:
            rendsz +=n
            rendsz +=" "
        return(rendsz[:-1])
    kimenet.write(rendsz(elz))
    kimenet.write("\n")
    for adat in teljes:
        if (mpbe(adat[0], adat[1], adat[2])-mpbe(elz[0], elz[1], elz[2])) >= 300:
            kimenet.write(rendsz(adat))
            kimenet.write("\n")
            elz = adat
            
    
        
    
    
                


















    
