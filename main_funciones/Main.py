
import random

import os

def clear():
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")
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
def new_nif(dict={}):
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
                print(e)
def nif_ale(dict={}):
    while True:
        cad = ""
        lista = []
        for i in dict.keys():
            lista.append(i)
        for i in range(1, 9):
            cad = cad + str(random.randint(0, 9))
        letrasDni = ["T", "R", "W", "A", "G", "M", "Y", "F", "P", "D", "X", "B", "N",
                     "J", "Z", "S", "Q", "V", "H", "L", "L", "C", "K", "E"]
        nif=cad + letrasDni[int(cad) % 23]
        if nif not in lista:
            return nif
def addPlayer(dict={}):
    clear()
    nombre=""
    while not nombre.isalpha():
        nombre = input("Enter your name: ")
    clear()
    print("Name: ",nombre)
    nif = new_nif(dict)
    clear()
    print("Name: ", nombre)
    print("DNI: ", nif)
    menurie="1) Cautious»\n2) Moderated\n3) Bold"
    print("Select Profile For The New Boot:\n")
    opcrie=getOpt(menurie,"Option: ",[1, 2, 3])
    clear()
    print("Name: ", nombre)
    print("DNI: ", nif)
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
    if op == "Y" or op == "y":
        dict[nif] = {"name": nombre, "human": True, "bank": False, "initialCard": "", "type": rie, "bet": 0,
                       "points": 0, "cards": [], "roundPoints": 0}
        return dict
    if op == "n"or op == "N":
        return dict

def addPlayerB(dict={}):
    clear()
    nombre = ""
    while not nombre.isalpha():
        nombre = input("Enter your name: ")
    clear()
    print("Name: ", nombre)
    nif = nif_ale(dict)
    clear()
    print("Name: ", nombre)
    print("DNI: ", nif)
    print("Select Profile For The New Boot:\n")
    menurie = "1) Cautious»\n2) Moderated\n3) Bold"
    opcrie = getOpt(menurie, "Option: ", [1, 2, 3])
    clear()
    print("Name: ", nombre)
    print("DNI: ", nif)
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
    if op == "Y" or op == "y":
        dict[nif] = {"name": nombre, "human": False, "bank": False, "initialCard": "", "type": rie, "bet": 0,
                       "points": 0, "cards": [], "roundPoints": 0}
        return dict
    if op == "n"or op == "N":
        return dict
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


menu00="1) Add/Remove/Show Players\n2) Settings\n3) Play Game\n4) Ranking\n5) Reports\n6) Exit"
menu01="1)New Human Player\n2)New Boot\n3)Show/Remote Players\n4)Go back"
menu02="1)Set Game Players\n2)Set Card's Deck\n3)Set Max Rounds (Default 5 Rounds)\n4)Go back"
menu03="1) View Stats\n2) View Game Stats\n3) Set Bet\n4) Order Card\n5) Automatic\n6) Stand"
menu04="1)Players With More Earnings\n2)Players With More Games Played\n3)Players With More Minutes Played\n4)Go back"
menu05="1) Initial card more repeated by each user," \
       "\n   only users who have played a minimum of 3 games.\n" \
       "2) Player who makes the highest bet per game,\n" \
       "   find the round whit the highest bet.\n" \
       "3) Player who makes the lowest bet per game.\n" \
       "4) Percentage of rounds won per player in each game\n" \
       "   (%), as well as their average bet for the game.\n" \
       "5) List of games won by Bots.\n" \
       "6) Round won by the bank in each game.\n" \
       "7) Number of users have been the bank in each game." \
       "8) Average bet per game.\n" \
       "9) Average bet of the firs round of each game.\n" \
       "10) Average bet of the last round of each game.\n" \
       "11) Go back"

menu22="1)ESP-ESP\n2)POK-POK\n0)GO BACK\n"
listajagadores=[]
salir=True
flg_00=True
flg_01 = False
flg_02 = False
flg_03 = False
flg_04 = False
flg_05 = False
players = { "11115555A":
{ "name":"Mario" ,"human":False,"bank" :False,"ini t i a lCa rd" :"" ,"prior i t y " :0,"type" :40,"bet" :4,"points" :0,"cards" :[],"roundPoints" :0},
"22225555A":
{ "name":"Pedro" ,"human":True,"bank" :False,"ini t i a lCa rd" :"" ,"prior i t y " :0,"type" :40,"bet" :4,"points" :0,"cards" :[],"roundPoints" :0},"49883035Z":
{ "name":"Alex" ,"human":True,"bank" :False,"ini t i a lCa rd" :"" ,"prior i t y " :0,"type" :40,"bet" :4,"points" :0,"cards" :[],"roundPoints" :0},"49883035D":
{ "name":"Pepito" ,"human":False,"bank" :False,"ini t i a lCa rd" :"" ,"prior i t y " :0,"type" :40,"bet" :4,"points" :0,"cards" :[],"roundPoints" :0}
}

while salir:
    while flg_00:
        clear()
        opc=getOpt(menu00,"Option: ",[1,2,3,4,5,6])
        if opc==1:
            clear()
            flg_00 = False
            flg_01 = True

        if opc==2:
            clear()
            print()
            flg_00 = False
            flg_02 = True

        if opc==3:
            clear()
            print()
            flg_00 = False
            flg_03 = True

        if opc==4:
            clear()
            print()
            flg_00 = False
            flg_04 = True
        if opc==5:
            clear()
            print()
            flg_00 = False
            flg_05 = True
        if opc==6:
            flg_00 = False
            salir=False

    while flg_01:
        clear()
        opc1 = getOpt(menu01, "Option: ", [1, 2, 3, 4])
        if opc1 == 1:
            addPlayer(players)
            print(players)
        if opc1 == 2:
            addPlayerB(players)
            print(players)

        if opc1 == 3:
            while True:
                listasid=[]
                tablaRemo(players)
                op=input("Option ( -id to remove players, -1 to exit ): ")
                for id in  players.keys():
                    listasid.append(id)
                if op[1:] in listasid:
                    del players[op[1:]]
                elif op=="-1":
                    break
                else:
                    print("="*50+"Invalid option"+"="*50)
                    input("Press enter to continue")
                clear()

        if opc1 == 4:
            flg_00 = True
            flg_01 = False
    while flg_02:
        clear()
        opc2=getOpt(menu02,"Option: ",rangeList=[1,2,3,4])
        if opc2==1:
            clear()

            print("*"*20 + "Actuals Players In Game"+"*"*20)
            if len(listajagadores)==0:
                print("There is no players in game")
                input("Press enter to continue")
            else:
                for i in listajagadores:
                    print(i, players[i]["name"], players[i]["human"], players[i]["type"])
                    input("Press enter to continue")

            while True:
                clear()
                tablaRemo(players)
                op = input("Option ( id to add to play,-id to remove players,sh to show actual players in the game, -1 to go back ): ")
                listasid = []
                for id in players.keys():
                    listasid.append(id)
                if op in listasid and op not in listajagadores:
                    listajagadores.append(op)
                    print("*" * 20 + "Actuals Players In Game" + "*" * 20)
                    for j in listajagadores:
                        print("{:<10} {:<10} {:<10} {:<10}  ".format("Player ID", "Name", "Human","Typed"))
                        print("*"*80)

                        print("{:<10} {:<10} {:<10} {:<10}  ".format(j, players[j]["name"], players[j]["human"], players[j]["type"]))
                        input("Press enter to continue")

                elif op[1:] in listasid and op[0]=="-":
                    listajagadores.remove(op[1:])
                    print("*" * 20 + "Actuals Players In Game" + "*" * 20)
                    if len(listajagadores) > 0:
                        for i in listajagadores:
                            print("{:<10} {:<10} {:<10} {:<10}  ".format("Player ID", "Name", "Human","Typed"))
                            print("*" * 80)
                            print("{:<10} {:<10} {:<10} {:<10}  ".format(i, players[i]["name"], players[i]["human"], players[i]["type"]))
                            input("Press enter to continue")

                    else:
                        print("*" * 20 + "Actuals Players In Game" + "*" * 20)
                        print("There is no players in game")
                        input("Press enter to continue")

                elif op=="sh":
                    if len(listajagadores)>0:
                        for i in listajagadores:
                            print("{:<10} {:<10} {:<10} {:<10}  ".format("Player ID", "Name", "Human", "Typed"))
                            print("*" * 80)
                            print("{:<10} {:<10} {:<10} {:<10}  ".format(i, players[i]["name"], players[i]["human"], players[i]["type"]))
                            input("Press enter to continue")
                    else:
                        print("*"*20 + "Actuals Players In Game"+"*"*20)
                        print("There is no players in game")
                        input("Press enter to continue")

                elif op=="-1":
                    break
                else:
                    print("=" * 50 + "Invalid option" + "=" * 50)
                    input("Press enter to continue")

            print()
        if opc2==2:
            cartas = getOpt(menu22, "Option: ", rangeList=[1, 2, 0])
            if cartas==1:
                print("Established Card Deck ESP, Baraja Española\n")
                input("Enter to continue")
                carta="ESP"
            if cartas==2:
                print("Established Card Deck POK, Baraja de Poker\n")
                input("Enter to continue")
                carta = "POK"
            clear()
        if opc2==3:
            clear()
            rounds=input("Max Rounds: ")
            print("Established maxim of rounds to: ",rounds)
            input("Enter to continue")
            clear()

        if opc2==4:
            flg_00 = True
            flg_02 = False
    while flg_03:
        clear()
        opc4 = getOpt(menu03, "Option:", rangeList=[1, 2, 3, 4,5,6])


    while flg_04 :
        clear()
        opc4 = getOpt(menu04, "Option:", rangeList=[1, 2, 3,4])
        print("*" * 75)
        print("{:<10} {:<25} {:<10} {:<10}  {:<10}".format("Player ID", "Name", "Earnings", "Games Played", "Minutes Played"))
        print("*"*75)
        if opc4==1:
            print()
        if opc4==2:
            print()
        if opc4==3:
            print()
        if opc4==4:
            flg_00 = True
            flg_04 = False
    while flg_05:
        clear()
        opc5 = getOpt(menu05, "Option:", rangeList=[1, 2, 3,4,5,6,7,8,9,10,11])
        if opc5==11:
            flg_00 = True
            flg_05 = False
            clear()
