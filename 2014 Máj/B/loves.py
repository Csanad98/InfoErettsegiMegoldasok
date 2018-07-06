teljes = []
letszam = 0
with open ("verseny.txt", "r") as bemenet:
    flag = True
    for sor in bemenet:
        if flag:
            letszam = int(sor)
            flag = False
        else:
            adat = list(sor)
            teljes.append(adat[:-1])
print("\n2.feladat")
count =0
rajt = ''
for adat in teljes:
    count +=1
    lovc = 0
    for lov in adat:
        if lov == "+":
           lovc +=1
        elif lov == "-":
            lovc = 0
        if lovc == 2:
            rajt += str(count)
            rajt += " "
print("Az egymás után többször célbataláló versenyzők rajtszáma:", rajt)

print("\n3.feladat")
maxc = 0
rajt = 0
maxrajt = 0
for adat in teljes:
    rajt +=1
    count = 0
    for lov in adat:
        if lov == "+":
            count +=1
    if maxc < count :
        maxc = count
        maxrajt = rajt
print("A legtöbb lövést leadó rajtszáma:", maxrajt)

def loertek (sor):
    ertek = 0
    aktpont = 20
    for num in range(len(sor)):
        if aktpont > 0 and sor[num] == "-":
            aktpont -=1
        else:
            ertek +=aktpont

    return ertek
        
print("\n5.feladat")
sorszam = int(input ("Adja meg egy versenyző sorszámát!"))-1
adat = teljes[sorszam]
count = 0
hanyadik = ""
for num in adat:
    count +=1
    if num == "+":
        hanyadik +=str(count)
        hanyadik +=" "
print("\n5a. feladat: célt érő lövések", hanyadik[:-1])
count = 0
for num in adat:
    if num == "+":
        count +=1
print("\n5b. feladat: Az eltalalt korongok szama:", count)        
count = 0
maxc = 0
for num in adat:
    if num == "+":
        count +=1
    else:
        count = 0
    if count > maxc:
        maxc = count
print("\n5c. feladat: A leghosszabb hibátlan sorozat hossza:", maxc)
print("A versenyző pontszáma:", loertek(adat))
    
with open("sorrend.txt", "w") as kimenet:
    kiosztott = 0
    hely = 0
    legjobb =[]
    for num in range(len(teljes)):
        hely +=1
        rajt = 0
        maxc = 0
        maxrajt = []
        for adat in teljes:
            rajt +=1
            if loertek(adat) > maxc and (str(rajt) not in legjobb):
                maxc = loertek(adat)
                maxrajt = []
                maxrajt.append(str(rajt))
                kiosztott +=1
            elif loertek(adat) == maxc and (str(rajt) not in legjobb):
                kiosztott +=1
                maxrajt.append(str(rajt))
        for top in maxrajt:
            legjobb.append(top)
        for n in maxrajt:
            kimenet.write(str(hely))
            kimenet.write("\t")
            kimenet.write(n)
            kimenet.write("\t")
            kimenet.write(str(maxc))
            kimenet.write("\n")
        for rajt in maxrajt:
            hely+=1
        hely -=1    
            






















            
            
  
