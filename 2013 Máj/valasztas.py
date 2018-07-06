jeloltLista = []
with open ('szavazatok.txt', 'r') as fajl:
    for sor in fajl:
        sor = sor.strip().split(' ')
        valasztoKerulet = sor[0]
        szavazatSzam = sor[1]
        jeloltVezetekneve = sor[2]
        jeloltKeresztneve = sor[3]
        partNeve = sor[4]
        jelolt = [valasztoKerulet, szavazatSzam, jeloltVezetekneve, jeloltKeresztneve, partNeve]
        jeloltLista.append(jelolt)

print("2. feladat\n")
indulokSzama = len(jeloltLista)
print('A helyhatósági választáson', indulokSzama, 'jelölt indult.\n' )

print("3. feladat\n")
print("Adja meg egy képviselő nevét, hogy megtudja hány szavazatot kapott:")
vezeteknev = input("Vezetéknév: ")
keresztnev = input("Keresztnév: ")

talalat = False
szavazatszam = 0
for jel in jeloltLista:
    if vezeteknev == jel[2] and keresztnev == jel[3]:
        talalat = True
        szavazatszam = int(jel[1])

if talalat:
    print("A keresett jelölt", szavazatszam, "szavazatot kapott.")

else:
    print("Ilyen nevű képviselőjelölt nem szerepel a nyilvántartásban!\n")
    
print("4. feladat\n")
osszesszavazat = 0
osszesallampolgar = 12345

for szav in jeloltLista:
    osszesszavazat += int(szav[1])

szazalek = round((osszesszavazat/osszesallampolgar)*100, 2)

print("A választáson", osszesszavazat,  "állampolgár, a jogosultak", szazalek, "%-a vett részt.")

print("5. feladat\n")
gyep = 0
hep = 0
zep = 0
fug = 0
tisz = 0
for i in jeloltLista:
    if i[4] == "GYEP":
        gyep += int(i[1])
    elif i[4] == "HEP":
        hep +=int(i[1])
    elif i[4] == "ZEP":
        zep +=int(i[1])
    elif i[4] == "-":
        fug +=int(i[1])
    elif i[4] == "TISZ":
        tisz +=int(i[1])

print("Zöldségevők Pártja= ", round((zep/osszesszavazat)*100, 2), "%")
print("Gyümölcsevők Pártja= ", round((gyep/osszesszavazat)*100, 2), "%")
print("Húsevők Pártja= ", round((hep/osszesszavazat)*100, 2), "%")
print("Tejivók Szövetsége= ", round((tisz/osszesszavazat)*100, 2), "%")
print("Független jelöltek= ", round((fug/osszesszavazat)*100, 2), "%")

print("6.feladat\n")

nyertesek = []
maxszavazat = 0

for i in jeloltLista:
    if int(i[1])> maxszavazat:
        maxszavazat = int(i[1])
        


for i in jeloltLista:
    nyertes = []
    if int(i[1]) == maxszavazat:
        nyertes.append(i[2])
        nyertes.append(i[3])
        if i[4] == "-":
            nyertes.append("független")
        else:
            nyertes.append(i[4])
        nyertesek.append(nyertes)
        
for i in nyertesek:
    print (i[0], i[1], i[2])


print("7.feldat\n")
maxszavazatszam = 0
with open ("kepviselok.txt", "w") as kimenet:

    for i in range (1, 9):
        for e in jeloltLista:
            if i == int(e[0]):
                if maxszavazatszam < int(e[1]):
                    maxszavazatszam = int(e[1])
        for f in jeloltLista:
            if i == int(f[0]) and maxszavazatszam == int(f[1]):
                if f[4] == "-":
                    q = "független"
                else:
                    q = f[4]
                kimenet.write(f[0]+" "+f[2]+" "+f[3]+" "+q+"\n")
        maxszavazatszam = 0


        
                    
            
    
      



