teljesLista = []
with open ("ip.txt", "r") as bemenet:
    for sor in bemenet:
        egysor = sor.strip().split(':')
        elso = egysor[0]
        masodik = egysor[1]
        harmadik = egysor[2]
        negyedik = egysor[3]
        otodik = egysor[4]
        hatodik = egysor[5]
        hetedik = egysor[6]
        nyolcadik = egysor[7]
        kod = [elso, masodik, harmadik, negyedik, otodik, hatodik, hetedik, nyolcadik]
        teljesLista.append(kod)

print ("2.feladat\n")
count = 0
for ipcim in teljesLista:
    count +=1

print("Az állományban ", count, " darab adatsor van.\n")
        
print("3. feladat\n")
legkisebbip = 0
for kod in teljesLista:
    egyesitett = ''
    for kodreszlet in range (8):
        egyesitett += kod[kodreszlet]
    if legkisebbip == 0:
        legkisebbip = int(egyesitett, 16)
    else:
        if legkisebbip > int(egyesitett, 16):
            legkisebbip = int(egyesitett, 16)

legkisebbipcim = hex(legkisebbip)
legkisebbipcim = legkisebbipcim[2:]
legkisebbipcim = legkisebbipcim[:4]+ ":" + legkisebbipcim[4:8]+":"+legkisebbipcim[8:12]+":"+legkisebbipcim[12:16]+":"+legkisebbipcim[16:20]+":"+legkisebbipcim[20:24]+":"+legkisebbipcim[24:28]+":"+legkisebbipcim[28:32]

print("A legalacsonyabb tárolt IP-cím: ")
print(legkisebbipcim, "\n")

print("4. feladat")
dok = 0
glob = 0
hely = 0

for ipcim in teljesLista:
    if ipcim[0] == "2001" and ipcim[1] == "0db8":
        dok +=1
    elif ipcim[0] == "2001":
        maradek = ipcim[1]
        if maradek[:2] == "0e":
            glob +=1
    else:
        elso = ipcim[0]
        if elso[:2] == "fc" or elso[:2] == "fd":
            hely +=1
        


print("Dokumentációs cím: ", dok, " darab")
print("Globális egyedi cím: ", glob, " darab")
print("Helyi egyedi cím: ", hely, " darab", "\n")


with open ("sok.txt", "w") as kimenet:
    for kod in teljesLista:
        egyesitett = ''
        for kodreszlet in range (8):
            egyesitett += kod[kodreszlet]
        egyesitett = list(egyesitett)
        nullakszama = 0
        for karakter in egyesitett:
            if karakter == '0':
                nullakszama +=1
        if nullakszama >= 18:
            irnivalokod = ''
            for kodreszlet in range (8):
                irnivalokod += (kod[kodreszlet] + ":")
            irnivalokod = irnivalokod[:-1]
            kimenet.write(irnivalokod)
            kimenet.write("\n")

print("6.feladat")
sorszam = input("Kérek egy sorszámot: ")
sorszam = (int(sorszam) -1)

munkadarab = teljesLista[sorszam]
for kodresz in range (8):
    if kodresz == 7:
        print(munkadarab[kodresz])
    else:
        print(munkadarab[kodresz] +":", end ="")
        
roviditett = ''
for kodresz in munkadarab:
    if kodresz == "0000":
        roviditett += "0"
        roviditett += ":"
    elif kodresz[:1] == "0":
        roviditett += kodresz[1:]
        roviditett += ":"
    else:
        roviditett += kodresz
        roviditett += ":"
roviditett = roviditett[:-1]
        

print (roviditett, "\n")

print("7.feladat")
eredeti = roviditett
roviditett = roviditett.split(":")
count = 0
maxcount = 0
for kodreszlet in roviditett:
    
    if kodreszlet == '0':
        
        count +=1
        maxcount += count
        

    else:
        count = 0
maxcount = 3
ujrovid = roviditett[:]
for kodreszletszam in range (len(roviditett)):
    if roviditett[kodreszletszam] == '0':
        count +=1
        if maxcount == count:
            ujrovid.insert(kodreszletszam+1, "")
            for number in range(maxcount):
                szam = kodreszletszam - number
                ujrovid.remove(ujrovid[szam])
           
                
    else:
        count = 0


roviditett = ujrovid
roviditett = ":".join(roviditett)


if eredeti == roviditett:
    print("Nem rövidíthető tovább.")
else:
    print(roviditett)
    






        
