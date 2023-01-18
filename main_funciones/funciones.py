import random
from dictionary import *
import os

#De antes
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
    elif opcrie == 2:
        rie = 40
        print("Profile: Moderated")
    elif opcrie == 3:
        rie = 30
        print("Profile: Bold")
    op=input("Is ok ? Y/n:n")
    if op == "Y" or op == "y":
        dict[nif] = {"name": nombre, "human": True, "bank": False, "initialCard": "", "type": rie, "bet": 0,
                       "points": 0, "cards": [], "roundPoints": 0}
        return dict
    elif op == "n"or op == "N":
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
    elif opcrie == 2:
        rie = 40
        print("Profile: Moderated")
    elif opcrie == 3:
        rie = 30
        print("Profile: Bold")
    op = input("Is ok ? Y/n:n")
    if op == "Y" or op == "y":
        dict[nif] = {"name": nombre, "human": False, "bank": False, "initialCard": "", "type": rie, "bet": 0,
                       "points": 0, "cards": [], "roundPoints": 0}
        return dict
    elif op == "n"or op == "N":
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
        elif dict[key]["human"] == False:
            listaidb.append(key)
            listaidb = ordenar(listaidb)
    for j in listaidh:
        listanamh.append(dict[j]["name"])
        if dict[j]["type"]==50:
            listatyh.append("Bold")
        elif dict[j]["type"]==40:
            listatyh.append("Moderated")
        elif dict[j]["type"]==30:
            listatyh.append("Cautious")
    for h in listaidb:
        listanamb.append(dict[h]["name"])
        if dict[h]["type"]==50:
            listatyb.append("Bold")
        elif dict[h]["type"]==40:
            listatyb.append("Moderated")
        elif dict[h]["type"]==30:
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


#Apartado de 3)Play Game
def CheckNotEmpty(msj1, msj2, *par):
    for i in par:
        if len(i) == 0:
            if type(i) == str:
                print(msj1)
            elif type(i) == list:
                print(msj2)
            input("Press Enter to Continue")
            return True
    return False

def setGamePriority(players, baraja, player_dict):
    barajac = list(baraja.keys())
    cartas = []
    for player in range(0,len(players)):
        cartas.append(barajac[random.randint(0,len(barajac)-1)])
    for pasada in range(0,len(players)-1):    
        for i in range(0,len(players)-pasada-1):
            if baraja[cartas[i]]["value"] > baraja[cartas[i+1]]["value"] or (baraja[cartas[i]]["value"] > baraja[cartas[i+1]]["value"] and baraja[cartas[i]]["priority"] > baraja[cartas[i+1]]["priority"]):
                cartas[i], cartas[i+1] = cartas[i+1], cartas[i]
                players[i], players[i+1] = players[i+1], players[i]
    priority = []
    for i in cartas:
        priority.append(i)
    for card in range(0,len(priority)):            #poner numero de prioridad
        priority[card] = baraja[cartas[card]]["value"]
        priority[card] = card+1
    for id in players:              #Poner la prioridad y la carta inicial el el diccionario de los jugadores
        player_dict[id]["initialCard"] = cartas[players.index(id)]
        player_dict[id]["priority"] = priority[players.index(id)]
    player_dict[players[len(players)-1]]["bank"] = True     #setear banca
    return player_dict

def ordenarPlayers(player_dict):
    players = list(player_dict.keys())
    for id in players:
        if player_dict[id]["points"] <= 0:
            players = players.remove[id]
    for pasada in range(0,len(players)-1):    
        for i in range(0,len(players)-pasada-1):
            if player_dict[players[i]]["priority"] > player_dict[players[i+1]]["priority"]:
                players[i], players[i+1] = players[i+1], players[i]
    return players

def orderByPoints(players, player_dict):
    for pasada in range(0,len(players)-1):    
        for i in range(0,len(players)-pasada-1):
            if player_dict[players[i]]["points"] < player_dict[players[i+1]]["points"]:
                players[i], players[i+1] = players[i+1], players[i]
    return players

def setPlayers(ids,players = {}):
    result = {}
    for id in ids:
        result[id] = players[id]
        result[id]["points"]  = 20
    return result

def setCards(cards):
    resultados = {}
    cards_list = list(cards.keys())
    for id in cards_list:
        resultados[id] = cards[id]
    return resultados

def resetCardsAndPoints(players_dict):
    players = list(players_dict.keys())
    for id in players:
        players_dict[id]["cards"] = []
        players_dict[id]["roundPoints"] = 0
    return players_dict

def getCard(cards):
    cards_list = list(cards.keys())
    card = cards_list[random.randint(0,len(cards_list)-1)]
    return card

def roundBot(player, cards):
    player["cards"] = []
    while True:
        card = getCard(cards)
        player["cards"].append(card)
        player["roundPoints"] += cards[card]["realValue"]
        cards = removeCardsFromDeck(player, cards)
        if player["roundPoints"] < 7.5:
            getAnotherCard = random.randint(0,100)
            if getAnotherCard <= player["type"] or player["roundPoints"] == 0.5:
                continue
            else:
                break
        else:
            break
    return player

def checkWins(bank,players, points):
    loseIn = []
    winIn = []
    posiblepointwin = 0
    posiblepointlose = 0
    finalPoint = 0
    playerList = list(players.keys())
    for id in playerList:
        if points <= players[id]["roundPoints"] and players[id]["bank"] == False and players[id]["roundPoints"] <= 7.5:
            loseIn.append(id)
        else:
            winIn.append(id)
    for id in winIn:
        posiblepointwin += players[id]["bet"]
    for id in loseIn:
        posiblepointlose -= players[id]["bet"]
    finalPoint += posiblepointwin
    finalPoint -= posiblepointlose
    if finalPoint < 0:
        if -1* finalPoint > players[bank]["points"]:
            return False
    getAnotherCard = random.randint(0,100)
    if getAnotherCard <= players[bank]["type"]:
        return False
    else: 
        return True

def roundBankBot(bank,cards,players,bank_id):
    bank["cards"] = []
    while True:
        card = getCard(cards)
        bank["cards"].append(card)
        bank["roundPoints"] += cards[card]["realValue"]
        cards = removeCardsFromDeck(bank, cards)
        if bank["roundPoints"] < 7.5:
            getAnotherCard = checkWins(bank_id, players, bank["roundPoints"])
            if not getAnotherCard:
                continue
            else:
                break
        else:
            break
    return bank

def removeCardsFromDeck(player,avaliable_cards):
    cardsToRemove = player["cards"]
    cards = list(avaliable_cards.keys())
    result = {}
    for card in cards:
        if card not in cardsToRemove:
            result[card] = avaliable_cards[card]
    return result

def pointsGiving(activePlayers,players_dict, bank):
    players = players_dict
    for id in activePlayers:
        if id != bank:
            playerPoints = players[id]["roundPoints"]
            bankPoints = players[bank]["roundPoints"]
            if bankPoints > playerPoints:               #Si la banca tiene mas puntos que la persona
                if bankPoints < 7.5:                    #Si tiene menos de 7.5
                    player_bet = players[id]["bet"]
                    while player_bet != 0 and players[id]["points"] != 0:
                        player_bet -= 1
                        players[id]["points"] -= 1
                        players[bank]["points"] += 1
                elif bankPoints > 7.5:                  #Si tiene mas de 7.5
                    if playerPoints < 7.5:             #Y el jugador tiene menos de 7.5
                        player_bet = players[id]["bet"]
                        while player_bet != 0 and players[bank]["points"] != 0:
                            player_bet -= 1
                            players[id]["points"] += 1
                            players[bank]["points"] -= 1
                    elif playerPoints == 7.5:
                        player_bet = players[id]["bet"]*2
                        while player_bet != 0 and players[bank]["points"] != 0:
                            player_bet -= 1
                            players[id]["points"] += 1
                            players[bank]["points"] -= 1
            #Si tienen los mismos puntos 
            elif bankPoints == playerPoints:
                if bankPoints <= 7.5:
                    player_bet = players[id]["bet"]
                    while player_bet != 0 and players[id]["points"] != 0:
                        player_bet -= 1
                        players[id]["points"] -= 1
                        players[bank]["points"] += 1
            #Si tiene menos puntos la banca que el jugador
            elif bankPoints < playerPoints:
                if bankPoints == 7.5:
                    player_bet = players[id]["bet"]
                    while player_bet != 0 and players[id]["points"] != 0:
                        player_bet -= 1
                        players[id]["points"] -= 1
                        players[bank]["points"] += 1
                elif bankPoints <= 7.5 and playerPoints > 7.6:
                    player_bet = players[id]["bet"]
                    while player_bet != 0 and players[id]["points"] != 0:
                        player_bet -= 1
                        players[id]["points"] -= 1
                        players[bank]["points"] += 1
                elif bankPoints < 7.5 and playerPoints < 7.5:
                    player_bet = players[id]["bet"]
                    while player_bet != 0 and players[bank]["points"] != 0:
                        player_bet -= 1
                        players[id]["points"] += 1
                        players[bank]["points"] -= 1
                elif playerPoints == 7.5:
                    player_bet = players[id]["bet"]*2
                    while player_bet != 0 and players[bank]["points"] != 0:
                        player_bet -= 1
                        players[id]["points"] += 1
                        players[bank]["points"] -= 1
    return players    

def checkLosers(active_players,players_dict):
    for id in active_players:
        if players_dict[id]["points"] <= 0:
            active_players.remove(id)
    return active_players

def setBank(nextBank, players_dict):
    players = list(players_dict.keys())
    for id in players:
        if id == nextBank:
            players_dict[id]["bank"] = True
        else:
           players_dict[id]["bank"] = False 
    return players_dict

def checkChangeBank(active_players,players_dict,bank):
    if not bank in active_players:
        players_dict[bank]["bank"] = False
        players_dict[active_players[len(active_players)-1]]["bank"] = True
    for id in active_players:
        if players_dict[id]["roundPoints"] == 7.5:
            players_dict = setBank(id,players_dict)
    return players_dict

def quitBank(players):
    player_list = list(players.keys())
    for id in player_list:
        players[id]["bank"] = False
    return players


def setBet(points):
    while True:
        num = input("Set the new Bet: ")
        if num.isnumeric():
            num = int(num)
            if num <= points:
                return num
            else:
                print("The new Bet has to be between 1 and "+str(points))
        else:
            print(num+" is  not a number")

def roundauto(player, cards):
    while True:
        if len(player["cards"]) == 0:
            card = getCard(cards)
            player["cards"].append(card)
            player["roundPoints"] += cards[card]["realValue"]
        if player["roundPoints"] < 7.5:
            getAnotherCard = random.randint(0,100)
            if getAnotherCard <= player["type"]:
                card = getCard(cards)
                player["cards"].append(card)
                player["roundPoints"] += cards[card]["realValue"]
                continue
            else:
                break
        else:
            break
    return player


def roundPlayer(player_id,cards):
    while True:
        opt = getOpt(textOpts="1)View Stats 2)View Game Stats 3)Set Bet 4)Order Card 5)Automatic Play 6)Stand \n",inputOptText="Option: ",rangeList=[1,2,3,4,5,6])
        if opt == 1:
            print("stats")
            input()
            clear()
        elif opt == 2:
            print("gameStats")
            input()
            clear()
        elif opt == 3:
            bet = setBet(player_id["points"])
            clear()
        elif opt == 4:
            card = getCard(cards)
            player_id["cards"].append(card)
            player_id["roundPoints"] += cards[card]["realValue"]
            print("You got "+card+"("+cards[card]["literal"]+")"+"\n Now you have "+str(player_id["roundPoints"])+"points.")
            cards = removeCardsFromDeck(player_id, cards)
            input()
            clear()
        elif opt == 5:
            player_id = roundauto(player_id, cards)
            break
        elif opt == 6 and len(player_id["cards"]) >= 1:
            break
        else:
            print("You need at least one card for be able to stand.")
            input()
            clear()
        if player_id["roundPoints"] > 7.5:
            break
    return player_id

def checkWinner(active_players, players):
    if len(active_players) == 1:
        print("{} wins with {} points!".format(players[active_players[0]]["name"], players[active_players[0]]["points"]))
    else:
        active_players = orderByPoints(active_players, players)
        print("{} wins with {} points!".format(players[active_players[0]]["name"], players[active_players[0]]["points"]))

