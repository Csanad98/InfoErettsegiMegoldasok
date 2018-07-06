teljesLista = []

with open ("veetel.txt", "r") as bemenet:
   for sor in bemenet:
       if len(sor) > 6:
           uzenet = sor.strip()
           vetel.append(uzenet)
           teljesLista.append(vetel)
           
       else:
           vetel = []
           szam = sor.strip().split(" ")
           nap = szam[0]
           vevo = szam[1]
           vetel.append(nap)
           vetel.append(vevo)

       
print("2.feladat")
elso = 0
utolso = 0


elsolista = teljesLista[0]
elso = elsolista[1]

utolsolista = teljesLista[-1]
utolso = utolsolista[1]
print("Az első üzenet rögzítője: ", elso)
print("Az utolsó üzenet rögzítője: ", utolso, "\n")

print("3.feladat")

for listaelem in teljesLista:
    if "farkas" in listaelem[2]:
        print(str(listaelem[0])+". nap", str(listaelem[1])+". rádióamatőr")


print("\n")
print("4.feladat")


napok = {1:0, 2:0, 3:0, 4:0, 5:0, 6:0, 7:0, 8:0, 9:0, 10:0, 11:0}



for listaelem in teljesLista:
    if int(listaelem[0]) in napok.keys():
        napok[int(listaelem[0])] +=1

for nap, szam in napok.items():
    print(str(nap)+". nap: ", str(szam)+" rádióamatőr")



with open("adaas.txt", "w") as kimenet:
    uzenetlista ={1:'', 2:'', 3:'', 4:'', 5:'', 6:'', 7:'', 8:'', 9:'', 10:'', 11:''}

    for number in range (1,12):
        for listaelem in teljesLista:
            if number == int(listaelem[0]):
                if uzenetlista[number] == '':
                    szoveg = list(listaelem[2])
                    uzenetlista[number] = szoveg

                elif uzenetlista[number] != '':
                    regiszoveg = uzenetlista[number]
                    ujszoveg = list(listaelem[2])
                    for ithchar in range (len(szoveg)):
                        if ujszoveg[ithchar] !="#" and regiszoveg[ithchar] == "#":
                            regiszoveg[ithchar] = ujszoveg[ithchar]
                    uzenetlista[number] = regiszoveg
        nyomtatas = uzenetlista[number]
        nyomtatas = "".join(nyomtatas)
        kimenet.write(nyomtatas)
        kimenet.write("\n")

def szame (szo):
    valasz = True
    for i in range(len(szo)):
        if szo[i] < '0' or szo[i]>'9':
            valasz = False

    return valasz


print("7.feladat")
egyedek = "Nincs ilyen feljegyzés"
nap = input("Adja meg a nap sorszámát! ")
radioam = input("Adja meg a rádióamatőr sorszámát! ")
szamok = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
for listaelem in teljesLista:
    if listaelem[0] == nap and listaelem[1] == radioam:
        egyedek = "Nincs információ"
        szoveg = listaelem[2]
        print(szoveg)
        szam = 0
        for karakter in szoveg:
            if karakter in szamok:
                szam+= int(karakter)
            egyedek = szam          
print("A megfigyelt egyedek száma: ", egyedek)



                        
