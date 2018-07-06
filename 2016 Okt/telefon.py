def mpbe (ora, perc, masodperc):
    percek = perc
    percek += 60*ora
    mp = masodperc
    mp += 60*percek
    return mp

hivasok = []
with open("hivas.txt", "r") as bemenet:
    for sor in bemenet:
        ido = sor.strip().split(" ")
        hivasok.append(ido)
print("3. feladat")
stat = {}
for ido in hivasok:
    if ido[0] not in stat.keys():
        num = ido[0]
        stat[num] = 1
    else:
        num = ido[0]
        stat[num] +=1

for adat in stat:
    print(adat, "óra", stat[adat], "hívás")

print("\n4.feladat")
legh = 0
count =0
sorszam =0
for hivas in hivasok:
    count +=1
    kezdes = (mpbe(int(hivas[0]), int(hivas[1]), int(hivas[2])))
    vege = (mpbe(int(hivas[3]), int(hivas[4]), int(hivas[5])))
    idotartam = (vege - kezdes)
    
    if idotartam > legh:
        legh = idotartam
        sorszam = count

print("A leghosszabb ideig vonalban levo hivo a "+str(sorszam)+". sorban szerepel, a hivas hossza:", legh, "masodperc")

print("\n5. feladat")

bemenet = input("Adjon meg egy időpontot! (ora perc masodperc)")
bemenet = bemenet.strip().split()
count = 0
beszelo = 0
varakozok = 0
for ido in hivasok:
    count +=1
    if mpbe(int(bemenet[0]), int(bemenet[1]), int(bemenet[2])) > mpbe(int(ido[0]), int(ido[1]), int(ido[2])) and mpbe(int(bemenet[0]), int(bemenet[1]), int(bemenet[2])) < mpbe(int(ido[3]), int(ido[4]), int(ido[5])):
        if beszelo == 0:
            beszelo = count
        else:
            varakozok +=1
            
if beszelo == 0:
    print("Nem volt beszélő")
else:
    print("A várakozók száma:", varakozok, "A beszélő a:", str(beszelo) + ". hívó.")

print("\n6.feladat")
count = 0
utolsoido = 0
utolsohivo = 0
utelottiido = 0
utelottihivo = 0
utolsokezd = 0
for ido in hivasok:
    count +=1
    if mpbe(int(ido[3]), int(ido[4]), int(ido[5])) > mpbe(8,0,0) and mpbe(int(ido[0]), int(ido[1]), int(ido[2])) < mpbe(12,0,0):
        if mpbe(int(ido[3]), int(ido[4]), int(ido[5])) > utolsoido:
            utelottiido = utolsoido
            utelottihivo = utolsohivo
            utolsoido = mpbe(int(ido[3]), int(ido[4]), int(ido[5]))
            utolsohivo = count
            utolsokezd = mpbe(int(ido[0]), int(ido[1]), int(ido[2]))


varakozas = utelottiido - utolsokezd
if varakozas < 0:
    varakozas = 0

print("Az utolsó telefonáló adatai a(z)", utolsohivo, ". sorban vannak,", varakozas, "másodpercig várt.")


with open("sikeres.txt", "w") as kimenet:
    count = 0
    utido = 0
    flag = True
    
    
    for ido in hivasok:
        if mpbe(int(ido[3]), int(ido[4]), int(ido[5])) > mpbe(8,0,0):
            elozo = ido
            break
        
    for ido in hivasok:
        count +=1
        if mpbe(int(ido[3]), int(ido[4]), int(ido[5])) > mpbe(8,0,0) and mpbe(int(ido[0]), int(ido[1]), int(ido[2])) < mpbe(12,0,0):
            if mpbe(int(ido[3]), int(ido[4]), int(ido[5])) > utido:
                if flag:
                    uth = ["8","0","0","8","0","0"]
                else:
                    uth = elozo
                utido = mpbe(int(ido[3]), int(ido[4]), int(ido[5]))
                kimenet.write(str(count))
                kimenet.write(" ")
                kimenet.write(uth[3])
                kimenet.write(" ")
                kimenet.write(uth[4])
                kimenet.write(" ")
                kimenet.write(uth[5])
                kimenet.write(" ")
                kimenet.write(ido[3])
                kimenet.write(" ")
                kimenet.write(ido[4])
                kimenet.write(" ")
                kimenet.write(ido[5])
                kimenet.write("\n")
                elozo = ido
                flag = False
                
                

            
        
    
            
        
        


























