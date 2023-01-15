import random


"""

def getOpt(textOpts="",inputOptText="",rangeList=[]):
    while True:
        try:
            print(textOpts)
            op=input(inputOptText)
            if op.isdigit() and int(op) in rangeList:#Comprova si es un digit i esta en la llista de permessos i sino printa un error i torna a preguntar
                return int(op)
            else:
                raise ValueError("El valor introduit no es correcte")
        except ValueError as e:
            print()
            print(e)
def new_nif(new="yes"):
    while True:
        try:
            letrasDni = ["T", "R", "W", "A", "G", "M", "Y", "F", "P", "D", "X", "B", "N",
                         "J", "Z", "S", "Q", "V", "H", "L", "L", "C", "K", "E"]
            dni=input("NIF of the new Customer:  ")
            if len(dni)<9 and not dni[-1].isalpha() and not dni[:8].isdigit(): # comprova que es adequat el format
                raise ValueError ("El NIF no te un format adequat (8 números i una lletra)")
            if letrasDni[int(dni[:8]) % 23] == dni[8]: # comprova que la lletra es correcte
                raise ValueError("El NIF no te la lletra correcta")
            else:
                return dni.upper()
        except ValueError as e:
                print(e)
def nif_ale():
    cad = ""
    for i in range(1, 9):
        cad = cad + str(random.randint(0, 9))
    letrasDni = ["T", "R", "W", "A", "G", "M", "Y", "F", "P", "D", "X", "B", "N",
                 "J", "Z", "S", "Q", "V", "H", "L", "L", "C", "K", "E"]
    nif=cad + letrasDni[int(cad) % 23]
    return nif
def addPlayerH(player):
    nombre=""
    while not nombre.isalpha():
        nombre = input("Enter your name: ")
    print("Name: ",nombre)
    nif = new_nif()
    print("DNI: ", nif)
    print("Select Profile For The New Boot:\n")
    menurie="1) Cautious»\n2) Moderated\n3) Bold"
    opcrie=getOpt(menurie,"Option: ",[1, 2, 3])
    if opcrie==1:
        rie=50
        print("Profile: Cautious")
    if opcrie == 2:
        rie = 40
        print("Profile: Moderated")
    if opcrie == 3:
        rie = 30
        print("Profile: Bold")
    op=input("Is ok ? Y/n:n")
    if op=="Y":
        player[nif] = {"name": nombre, "human": True, "bank": False, "initialCard": "", "type": rie, "bet": 0,
                       "points": 0, "cards": [], "roundPoints": 0}
        return player
    if op=="n":
        return

def addPlayerB(player):
    nombre = ""
    while not nombre.isalpha():
        nombre = input("Enter your name: ")
    print("Name: ", nombre)
    nif = nif_ale()
    print("DNI: ", nif)
    print("Select Profile For The New Boot:\n")
    menurie = "1) Cautious»\n2) Moderated\n3) Bold"
    opcrie = getOpt(menurie, "Option: ", [1, 2, 3])
    if opcrie == 1:
        rie = 50
        print("Profile: Cautious")
    if opcrie == 2:
        rie = 40
        print("Profile: Moderated")
    if opcrie == 3:
        rie = 30
        print("Profile: Bold")
    op = input("Is ok ? Y/n:n")
    if op == "Y":
        player[nif] = {"name": nombre, "human": True, "bank": False, "initialCard": "", "type": rie, "bet": 0,
                       "points": 0, "cards": [], "roundPoints": 0}
        return player
    if op == "n":
        return"""

'''def new_nif(dict={}):
    while True:
        try:
            lista=[]
            for i in dict.keys():
                lista.append(i)
            letrasDni = ["T", "R", "W", "A", "G", "M", "Y", "F", "P", "D", "X", "B", "N",
                         "J", "Z", "S", "Q", "V", "H", "L", "L", "C", "K", "E"]
            dni=input("DNI of the new Player:  ")
            if len(dni)<9 and not dni[-1].isalpha() and not dni[:8].isdigit(): # comprova que es adequat el format
                raise ValueError ("El NIF no te un format adequat (8 números i una lletra)")
            if letrasDni[int(dni[:8]) % 23] == dni[8]: # comprova que la lletra es correcte
                raise ValueError("El NIF no te la lletra correcta")
            if dni in lista:
                raise ValueError("El NIF ya esta en us")
            else:
                return dni.upper()
        except ValueError as e:
                print(e)'''
players = { "11115555A":
{ "name":"Mario" ,"human":False,"bank" :False,"ini t i a lCa rd" :"" ,"prior i t y " :0,"type" :40,"bet" :4,"points" :0,"cards" :[],"roundPoints" :0},
"22225555A":
{ "name":"Pedro" ,"human":True,"bank" :False,"ini t i a lCa rd" :"" ,"prior i t y " :0,"type" :40,"bet" :4,"points" :0,"cards" :[],"roundPoints" :0},"49883035Z":
{ "name":"Alex" ,"human":True,"bank" :False,"ini t i a lCa rd" :"" ,"prior i t y " :0,"type" :40,"bet" :4,"points" :0,"cards" :[],"roundPoints" :0},"49883035D":
{ "name":"Pepito" ,"human":False,"bank" :False,"ini t i a lCa rd" :"" ,"prior i t y " :0,"type" :40,"bet" :4,"points" :0,"cards" :[],"roundPoints" :0}
}
listaid=[]

'''for i in players.keys():
    if players[i]["human"]==True:
        listaidh.append([i,players[i]["name"]])
    if players[i]["human"]==False:
        listaidb.append(i)
print(listaidh)
print(listaidb)
listaid=[]
cad=""
for i in listaidh:
    for j in listaidb:
        print(i,players[i]["name"],str(players[i]["type"]),j,players[j]["name"],str(players[j]["type"]))
print(cad)'''
def ordenar(lista):
    for pasadas in range(len(lista) - 1):
        for i in range(len(lista) - 1 - pasadas):
            if lista[i] > lista[i + 1]:  # ordena de manera descendent
                lista[i], lista[i + 1] = lista[i + 1], lista[i]
    return lista

def tablaRemo(dict={}):
    listaidh=[]
    listanamh=[]
    listatyh=[]
    listaidb=[]
    listanamb=[]
    listatyb=[]
    for key in dict.keys():
        if dict[key]["human"] == True:
            listaidh.append(key)
            listaidh=ordenar(listaidh)
        if dict[key]["human"] == False:
            listaidb.append(key)
            listaidb = ordenar(listaidb)
    for j in listaidh:
        listanamh.append(dict[j]["name"])
        if dict[j]["type"]==50:
            listatyh.append("Bold")
        if dict[j]["type"]==40:
            listatyh.append("Moderated")
        if dict[j]["type"]==30:
            listatyh.append("Cautious")

    for h in listaidb:
        listanamb.append(dict[h]["name"])
        if dict[h]["type"]==50:
            listatyb.append("Bold")
        if dict[h]["type"]==40:
            listatyb.append("Moderated")
        if dict[h]["type"]==30:
            listatyb.append("Cautious")
    num=0
    while num!=len(listaidh):
        if len(listaidh) > len(listaidb):
            listaidb.append(" ")
            listanamb.append(" " )
            listatyb.append(" " )
        else:
            listaidh.append(" " )
            listanamh.append(" " )
            listatyh.append(" " )
        num+=1
    num=0
    print("*"*35+"Select Players"+"*"*35)
    print("{:>25} {:>14} {:>25}".format("Boot Players", "||", "Human Players"))
    print("-"*80)
    print("{:<10} {:<15} {:<10} {:<5} {:<10} {:<15} {:<10}".format("ID", "NAME","TYPE","||","ID", "NAME","TYPE"))
    print("*" * 80)
    while num!=len(listaidh):

        print("{:<10} {:<15} {:<10} {:<5} {:<10} {:<15} {:<10}".format(listaidh[num], listanamh[num],listatyh[num],"||",listaidb[num],listanamb[num],listatyb[num]))
        'print(listaidh[num],listanamh[num],listatyh[num],listaidb[num],listanamb[num],listatyb[num])'
        num += 1
    print("*" * 80)

tablaRemo(players)





