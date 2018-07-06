teljesLista = []
with open ("tavok.txt", "r") as bemenet:
    for sor in bemenet:
        adat = sor.strip().split(" ")
        teljesLista.append(adat)
        #0 - nap
        #1 - fuvar
        #2 - táv
print("2.feladat")
flag = True
for lista in teljesLista:
    if flag:
        elsonap = lista[0]
        elsofuvar = lista[1]
        elsotav = lista[2]
        flag = False
    else:
        if elsonap > lista[0]:
            elsonap = lista[0]
            elsofuvar = lista[1]
            elsotav = lista[2]
            
        elif elsofuvar > lista[1]:
            elsofuvar = lista[1]
            elsotav = lista[2]
print("A hét legelső útja", elsotav, "km volt.")

print("\n3.feladat")
flag = True
for lista in teljesLista:
    if flag:
        lastnap = lista[0]
        lastfuvar = lista[1]
        lasttav = lista[2]
        flag = False
    else:
        if lastnap < lista[0]:
            lastnap = lista[0]
            lastfuvar = lista[1]
            lasttav = lista[2]
            
        elif lastfuvar < lista[1]:
            lastfuvar = lista[1]
            lasttav = lista[2]
print("A hét legutolsó útja", lasttav, "km volt.")

print("\n4.feladat")
napok = {1:False, 2:False, 3:False, 4:False, 5:False, 6:False, 7:False}
for lista in teljesLista:
    if int(lista[0]) in napok:
        napok[int(lista[0])] = True
print("A következő számú napokon nem dolgozott a futár a héten:")
for key, value in napok.items():
    if value == False:
        print(key)

print("\n5.feladat")
maxfuvar = 0
maxnap = 0
for nap in range(1,8):
    fuvarok = 0
    adottnap = nap
    for lista in teljesLista:
        if nap == int(lista[0]):
            fuvarok += 1
                   
    if maxfuvar < fuvarok:
        maxfuvar = fuvarok
        maxnap = adottnap
print("A legtöbb fuvar a(z)", maxnap, ". napon volt")

print("\n6.feladat")
for nap in range (1,8):
    napitav = 0
    for lista in teljesLista:
        if nap == int(lista[0]):
            napitav += int(lista[2])
    print(str(nap)+". nap:", napitav, "km")

print("\n7.feladat")
tav = input("Adjon meg egy tetszőleges távot km-ben, hogy kiszámoljam az érte járó díjazást!")
tav =int(tav)
if tav <=2:
    print("500 Ft")
elif tav <=5:
    print("700 Ft")
elif tav <= 10:
    print("900 Ft")
elif tav <=20:
    print("1400 Ft")
elif tav <=30:
    print("2000 Ft")

def dijak(tav):
    tav =int(tav)
    if tav <=2:
        return("500 Ft")
    elif tav <=5:
        return("700 Ft")
    elif tav <= 10:
        return("900 Ft")
    elif tav <=20:
        return("1400 Ft")
    elif tav <=30:
        return("2000 Ft")
    
with open ("dijazas.txt", "w") as kimenet:
    for nap in range(1,8):
        for ut in range(1, 41):
            for lista in teljesLista:
                if nap == int(lista[0]) and ut == int(lista[1]):
                    dij = dijak(lista[2])
                    sor = (str(nap)+". nap "+ str(ut)+".út: "+str(dij))
                    kimenet.write(sor)
                    kimenet.write("\n")
                    
print("\n9.feladat")
def intdijak(tav):
    tav =int(tav)
    if tav <=2:
        return(500)
    elif tav <=5:
        return(700)
    elif tav <= 10:
        return(900)
    elif tav <=20:
        return(1400)
    elif tav <=30:
        return(2000)
    
teljesosszeg = 0
for lista in teljesLista:
    teljesosszeg += (intdijak(lista[2]))
print("A heti bér: ", teljesosszeg)

    
    
            
    
        
                      
                      
        

            


        
