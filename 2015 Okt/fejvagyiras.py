print("1.feladat")
import random

erme = ["F", "I"]
print(random.choice(erme), "\n")

print("2.feladat")
tipp = input("Tippeljen! (F/I)= ")
dobas = random.choice(erme)
print("A tipp ", tipp, ", a dobás eredménye ", dobas, " volt.")
if tipp == dobas:
    print("Ön eltalálta.", "\n")
else:
    print("Ön nem találta el.", "\n")
    
print("3.feladat")
allcount = 0
with open("kiserlet.txt") as infile:
    for sor in infile:
        allcount+=1
print("A kísérlet ", allcount, " dobásból állt.", "\n")

print("4.feladat")
fejcount = 0
with open("kiserlet.txt") as infile:
    for sor in infile:
        if sor[0] == "F" :
            fejcount +=1
relat = (fejcount/allcount)*100
relat = round(relat, 2)
print("A kísérlet során a fej relatív gyakorisága ", relat, "% volt.", "\n")

print("5.feladat")
fejcount = 0
allfejcount = 0
flag = True
with open("kiserlet.txt") as infile:
    for sor in infile:
        if sor[0] == "F" :
            fejcount +=1
            if fejcount == 2:
                allfejcount +=1
            elif fejcount > 2 and flag == True:
                allfejcount -=1
                flag = False
        else:
            fejcount = 0
            flag = True

print("A kísérlet során ", allfejcount, " alkalommal dobtak pontosan két fejet egymás után.", "\n")

print("6.feladat")
fejcount = 0
maxfejcount = 0
with open("kiserlet.txt") as infile:
    for sor in infile:
        if sor[0] == "F" :
            fejcount +=1
            if maxfejcount < fejcount:
                maxfejcount = fejcount
        else:
            fejcount = 0
            
    tagszam = maxfejcount
    maxfejcount = 0
    fejcount = 0
    dobas = 0
    sorszam = 0
    
with open("kiserlet.txt") as infile:    
    for sor in infile:
        sorszam +=1
        if maxfejcount == tagszam:
            dobas = sorszam - tagszam
            break
        
        elif sor[0] == "F" :
            fejcount +=1
            if maxfejcount < fejcount:
                maxfejcount = fejcount
            
        else:
            fejcount = 0

        

   
print("A leghosszabb tisztafej sorozat ", tagszam, " tagból áll, kezdete a(z) ", dobas, ". dobás.")

erme = ["F", "I"]
sorozat = []
for dobassor in range(1000):
    dob = []
    for dobas in range(4):
        dob.append(random.choice(erme))
    sorozat.append(dob)

FFFF = 0
FFFI = 0
    
for dobassor in sorozat:
    if dobassor == ["F","F","F","F"]:
        FFFF +=1
    elif dobassor == ["F","F","F","I"]:
        FFFI +=1

with open ("dobasok.txt", "w") as kimenet:
    FF = ("FFFF: ", str(FFFF))
    FF = "".join(FF)
    kimenet.write(FF)

    FI = (", FFFI: ", str(FFFI))
    FI = "".join(FI) + ' ' + '\n'
    kimenet.write(FI)

    for dobassor in sorozat:
        out = "".join(dobassor)+ ' '
        kimenet.write(out)



    
