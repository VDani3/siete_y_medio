import random
from dictionary import *
import os
import pyfiglet         # libreria para los titulos
import mysql.connector  # libreria para conectarse a mysql
import datetime         # libreria para obtener la hora del sistema

#De antes
def clear():
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")
        
def getOpt(textOpts="",inputOptText="",rangeList=[], titulo = "", additional = ""):
    while True:
        try:
            print(textOpts)
            op=input(inputOptText)
            if op.isdigit() and int(op) in rangeList:#Comprova si es un digit i esta en la llista de permessos i sino printa un error i torna a preguntar
                return int(op)
            else:
                raise ValueError("El valor introduit no es correcte")
        except ValueError as e:
            print(e)
            input()
            clear()
            titulos(titulo)
            if additional != "":
                print(additional)

def new_nif(dict={}):
    while True:
        try:
            lista=[]
            for i in dict.keys():
                lista.append(i)
            letrasDni = ["T", "R", "W", "A", "G", "M", "Y", "F", "P", "D", "X", "B", "N",
                         "J", "Z", "S", "Q", "V", "H", "L", "L", "C", "K", "E"]
            dni=input(" "*30+"DNI of the new Player:  ")
            if len(dni)<9 and not dni[-1].isalpha() and not dni[:8].isdigit(): # comprova que es adequat el format
                raise ValueError ("El NIF no te un format adequat (8 números i una lletra)")
            if letrasDni[int(dni[:8]) % 23] == dni[8].lower(): # comprova que la lletra es correcte
                raise ValueError("El NIF no te la lletra correcta")
            if dni.upper() in lista:
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
    titulos("BBDD Players")
    nombre=""
    while not nombre.isalpha():
        nombre = input(" "*30+"Enter your name: ")
    clear()
    titulos("BBDD Players")
    print(" "*30+"Name: ",nombre)
    nif = new_nif(dict)
    clear()
    titulos("BBDD Players")
    print(" "*30+"Name: ", nombre)
    print(" "*30+"DNI: ", nif)
    menurie=" "*30+"1) Cautious \n"+" "*30+"2) Moderated\n"+" "*30+"3) Bold"
    print(" "*30+"Select Profile For The New Boot:\n")
    opcrie=getOpt(menurie,"Option: ",[1, 2, 3],"BDD Players")
    clear()
    titulos("BBDD Players")
    print(" "*30+"Name: ", nombre)
    print(" "*30+"DNI: ", nif)
    if opcrie==1:
        rie=30
        bet = 5
        print(" "*30+"Profile: Cautious")
    if opcrie == 2:
        rie = 40
        bet = 4
        print(" "*30+"Profile: Moderated")
    if opcrie == 3:
        rie = 50
        bet = 3
        print(" "*30+"Profile: Bold")
    op=input(" "*30+"Is ok ? Y/n:n")
    if op == "Y" or op == "y":
        dict[nif] = {"name": nombre, "human": True, "bank": False, "initialCard": "", "type": rie, "bet": bet,
                       "points": 0, "cards": [], "roundPoints": 0}
        newPlayer_db(nif, dict[nif])
        return dict
    if op == "n"or op == "N":
        return dict

def addPlayerB(dict={}):
    clear()
    titulos("BBDD Players")
    nombre = ""
    while not nombre.isalpha():
        nombre = input(" "*30+"Enter your name: ")
    clear()
    titulos("BBDD Players")
    print(" "*30+"Name: ", nombre)
    nif = nif_ale(dict)
    clear()
    titulos("BBDD Players")
    print(" "*30+"Name: ", nombre)
    print(" "*30+"DNI: ", nif)
    print(" "*30+"Select Profile For The New Boot:\n")
    menurie = " "*30+"1) Cautious\n"+" "*30+"2) Moderated\n"+" "*30+"3) Bold"
    opcrie = getOpt(menurie, "Option: ", [1, 2, 3],"BBDD Players")
    clear()
    titulos("BBDD Players")
    print(" "*30+"Name: ", nombre)
    print(" "*30+"DNI: ", nif)
    if opcrie == 1:
        rie = 30
        bet=5
        print(" "*30+"Profile: Cautious")
    if opcrie == 2:
        rie = 40
        bet=4
        print(" "*30+"Profile: Moderated")
    if opcrie == 3:
        rie = 50
        bet=3
        print(" "*30+"Profile: Bold")
    op = input(" "*30+"Is ok ? Y/n: ")
    if op == "Y" or op == "y":
        dict[nif] = {"name": nombre, "human": False, "bank": False, "initialCard": "", "type": rie, "bet": bet,
                       "points": 0, "cards": [], "roundPoints": 0}
        newPlayer_db(nif, dict[nif])
        return dict
    if op == "n"or op == "N":
        return dict

def ordenar(lista):
    for pasadas in range(len(lista) - 1):
        for i in range(len(lista) - 1 - pasadas):
            if lista[i] > lista[i + 1]:  # ordena de manera descendent
                lista[i], lista[i + 1] = lista[i + 1], lista[i]
    return lista

def tablaRemo(dict={},lista=[]):
    listaidh=[]
    listanamh=[]
    listatyh=[]
    listaidb=[]
    listanamb=[]
    listatyb=[]
    for key in lista:
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
    print("{:>25} {:>14} {:>25}".format("Human Players", "||", "Boot Players"))
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
        if len(i) < 2:
            if type(i) == str and len(i) == 0:
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
            if baraja[cartas[i]]["value"] < baraja[cartas[i+1]]["value"] or (baraja[cartas[i]]["value"] < baraja[cartas[i+1]]["value"] and baraja[cartas[i]]["priority"] < baraja[cartas[i+1]]["priority"]):
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
    res = []
    for id in players:
        if player_dict[id]["points"] > 0:
            res.append(id)
    players = res
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
        result[id]["points"] = 20
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

def bankCheck(players_game):
    players = list(players_game.keys())
    for id in players:
        if players_game[id]["bank"]:
            return id

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
    activePlayers = ordenar(activePlayers)
    players = players_dict
    #Banca gana puntos primero
    for id in activePlayers:
        playerPoints = players[id]["roundPoints"]
        bankPoints = players[bank]["roundPoints"]
        if bankPoints > playerPoints:               #Si la banca tiene mas puntos que la persona
            if bankPoints < 7.5:                    #Si tiene menos de 7.5
                player_bet = players[id]["bet"]
                while player_bet != 0 and players[id]["points"] != 0:
                    player_bet -= 1
                    players[id]["points"] -= 1
                    players[bank]["points"] += 1
                    #Si tienen los mismos puntos 
        elif bankPoints == playerPoints:
            if bankPoints <= 7.5:
                player_bet = players[id]["bet"]
                while player_bet != 0 and players[id]["points"] != 0:
                    player_bet -= 1
                    players[id]["points"] -= 1
                    players[bank]["points"] += 1
        elif bankPoints < playerPoints:
                if bankPoints == 7.5:
                    player_bet = players[id]["bet"]
                    while player_bet != 0 and players[id]["points"] != 0:
                        player_bet -= 1
                        players[id]["points"] -= 1
                        players[bank]["points"] += 1
                elif bankPoints <= 7.5 and playerPoints > 7.5:
                    player_bet = players[id]["bet"]
                    while player_bet != 0 and players[id]["points"] != 0:
                        player_bet -= 1
                        players[id]["points"] -= 1
                        players[bank]["points"] += 1
    #Banca reparte despues
    for id in activePlayers:
        if id != bank:
            playerPoints = players[id]["roundPoints"]
            bankPoints = players[bank]["roundPoints"]
            if bankPoints > playerPoints:               #Si la banca tiene mas puntos que la persona
                if bankPoints > 7.5:                  #Si tiene mas de 7.5
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
            #Si tiene menos puntos la banca que el jugador
            elif bankPoints < playerPoints:
                if bankPoints < 7.5 and playerPoints < 7.5:
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
    print("Now {} it's the bank.")
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
            if getAnotherCard <= player["type"] or player["roundPoints"] == 0.5:
                card = getCard(cards)
                player["cards"].append(card)
                player["roundPoints"] += cards[card]["realValue"]
                continue
            else:
                break
        else:
            break
    return player

def roundPlayer(player_id,cards,players_game,roundgame,active_players,name,banca,players_game_keys, menu3h):
    while True:
        clear()                                                                                 
        titulos("Seven And Half")                                                               
        print("Round "+str(roundgame) +" Turn of "+player_id["name"])                   
        opt = getOpt(menu3h, " " * 30 + "Option: ", [1, 2, 3, 4, 5, 6],"Seven And Half","Round "+str(roundgame) +" Turn of "+player_id["name"])
        if opt == 1:
            clear()                                                                             
            titulos("Seven And Half")                                                           
            Stats_player(active_players, players_game, players_registered,name)  # printa las Stats idividuales
            input()
            clear()
        elif opt == 2:
            clear()                                                                             
            titulos("Seven And Half")                                                           
            print(" " * 30 + "Round " + str(roundgame) + " Turn of " + players_game[banca]["name"])      # printa las estats de la ronda de LA BANCA
            print(print_ronda(players_game_keys, players_game, players_registered))             
            input(" " * 50 + "Enter to continue\n") 
            clear()
        elif opt == 3:
            player_id["bet"] = setBet(player_id["points"])
            clear()
        elif opt == 4:
            card = getCard(cards)
            player_id["cards"].append(card)
            player_id["roundPoints"] += cards[card]["realValue"]
            print("You got "+card+" ("+cards[card]["literal"]+")"+"\nNow you have "+str(player_id["roundPoints"])+"points.")
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

def checkWinner(active_players, players,roundgame):
    titulos("Game Over")
    if len(active_players) == 1:
        print(" "*15+"The winner is : "+str(active_players[0])+" - "
              + str(players_registered[active_players[0]]["name"]) + " in "
              +str(roundgame-1)+" rounds, whith "
              +str(players_registered[active_players[0]]["points"])+" points")                              
        input(" "*30+"Enter to continue")
    else:
        active_players = orderByPoints(active_players, players)
        print("{} wins with {} points!".format(players[active_players[0]]["name"], players[active_players[0]]["points"]))
        
def titulos(titulo="",extra=""):
    if extra=="":
        print("*" * 90)
    else:
        print("*"*34+"  "+extra+"  "+"*"*34)
    print(pyfiglet.figlet_format(titulo, justify="center"))
    print("*" * 90 + "\n")

def print_ronda(players_game_keys,players_game,players_registered):
    cadpo = "Points: ".ljust(20)
    cadn = "Name: ".ljust(20)
    cadh = "Human: ".ljust(20)
    cadp = "Priority: ".ljust(20)
    cadt = "Type: ".ljust(20)
    cadba = "Bank: ".ljust(20)
    cadbe = "Bet: ".ljust(20)
    cadc = "Cards: ".ljust(20)
    cadr = "RoundPoints:".ljust(20)
    for printear in players_game_keys:
        cart = ""
        cadn += players_registered[printear]["name"].ljust(30)
        cadh += str(players_registered[printear]["human"]).ljust(30)
        cadp += str(players_registered[printear]["priority"]).ljust(30)
        cadt += str(players_registered[printear]["type"]).ljust(30)
        cadba += str(players_registered[printear]["bank"]).ljust(30)
        cadbe += str(players_registered[printear]["bet"]).ljust(30)
        cadpo += str(players_game[printear]["points"]).ljust(30)
        for j in players_registered[printear]["cards"]:
            cart+=j+" "
        cadc += cart.ljust(30)
        cadr += str(players_registered[printear]["roundPoints"]).ljust(30)
        # print("Name:"+players_registered[printear]["name"]+"\nHuman:"+str(players_registered[printear]["human"])+"\nPriority:"+str(players_registered[printear]["priority"])+"\nType:"+str(players_registered[printear]["type"])+"\nBank:"+str(players_registered[printear]["bank"])+"\nBet:"+str(players_registered[printear]["bet"])+"\nPoints: "+str(players_game[printear]["points"])+ "\nCards: "+str(players_game[printear]["cards"])+"\nrounPoints: "+str(players_game[printear]["roundPoints"]))
    cadmaster = cadn + "\n" + cadh + "\n" + cadp + "\n" + cadt + "\n" + cadba + "\n" + cadbe + "\n" + cadpo + "\n" + cadc + "\n" + cadr + "\n"
    print()
    return cadmaster

def Stats_player (active_players,players_game,players_registered,name):
    print("*"*37+" "+"Stats of "+name+" "+"*"*37)
    for id in active_players:
        if players_game[id]["name"] == name:
            print(" " * 30 + "Name".ljust(20) + players_game[id]["name"] + "\n" + " " * 30 + "Type".ljust(20) + str(
            players_registered[id]["type"]) + "\n"
              + " " * 30 + "Human".ljust(20) + str(players_registered[id]["human"]) + "\n"
              + " " * 30 + "Bank".ljust(20) + str(players_registered[id]["bank"]) + "\n"
              + " " * 30 + "Initialcard".ljust(20) + str(players_registered[id]["initialCard"]) + "\n"
              + " " * 30 + "priority".ljust(20) + str(players_registered[id]["priority"]) + "\n"
              + " " * 30 + "bet".ljust(20) + str(players_registered[id]["bet"]) + "\n"
              + " " * 30 + "points".ljust(20) + str(players_registered[id]["points"]) + "\n"
              + " " * 30 + "cards".ljust(20) + str(players_registered[id]["cards"]) + "\n"
              + " " * 30 + "roundPoints".ljust(20) + str(players_registered[id]["roundPoints"]))


config = {
    'host':'13.93.30.179', 
    'port':'3306',
    'user':'user', 
    'password':'user1234+', 
    'database':'siete_y_medio_db'}
conexion = mysql.connector.connect(**config)
cursor = conexion.cursor()

def getPlayers_db():
    cursor.execute("select * from player;")
    players = cursor.fetchall()
    for player in players:
        if player[3] == 1:
            players_registered[player[0]] = {"name":player[1], "human":True, "bank":False,"initialCard":"","priority":0, "type":player[2], "bet":(player[2]/10),"points":0,"cards":[],"roundPoints":0}
        else:
            players_registered[player[0]] = {"name":player[1], "human":False, "bank":False,"initialCard":"","priority":0, "type":player[2], "bet":(player[2]/10),"points":0,"cards":[],"roundPoints":0}

def newPlayer_db(id, player):
    name = player["name"]
    if player["human"]:
        human = "1"
    else:
        human = "0"
    risk = str(player["type"])
    ins = 'insert into player(player_id, player_name, player_risk, human) values("'+id+'","'+name+'",'+risk+','+human+');'
    cursor.execute(ins)
    conexion.commit()

def deletePlayer_db(id):
    cursor.execute('delete from player where player_id="'+id+'";')
    conexion.commit()

# cardgame BD
def generateGameID():
    cursor.execute('select * from cardgame')
    cardgame = cursor.fetchall()
    for id in cardgame:
        lastID = int(str(id[0]))
    lastID = lastID+1
    return lastID
    
def collectStarterGameInfo(active_players, carta):
    id = generateGameID()
    numPlayers = 0
    for i in active_players:
        numPlayers+=1
    startHour = str(datetime.datetime.now())
    print(startHour)
    startHour = startHour[:19]
    print(startHour)
    deckID = carta.lower()
    cardgameInfo[id] = {"players":numPlayers, "rounds":0, "start_hour":startHour, "end_hour":"", "deck":deckID}
    return id

def sendStarterGameInfo_db(id):
    game = cardgameInfo[id]
    cursor.execute('insert into cardgame values ('+str(id)+','+str(game["players"])+',0,"'+game["start_hour"]+'","2023-01-01 00:00:00","'+game["deck"]+'")')
    conexion.commit()

def collectEndGameInfo(id, roundNum):
    endHour = str(datetime.datetime.now())
    endHour = endHour[:19]
    cardgameInfo[id]["rounds"] = roundNum
    cardgameInfo[id]["end_hour"] = endHour
    cursor.execute('update cardgame set rounds="'+str(roundNum)+'" where cardgame_id="'+str(id)+'"')
    cursor.execute('update cardgame set end_hour="'+endHour+'" where cardgame_id="'+str(id)+'"')
    conexion.commit()

# player_game BD
def generateGamePlayerID(lastID):
    if gamePlayerInfo != "":
        for id in gamePlayerInfo:
            lastID = int(str(id)[0])
        lastID += 1
    else:
        lastID = 1
    return lastID

def collectStarterGamePlayerInfo(active_players,players_game,cardgameID,roundgame):
    id = generateGamePlayerID(roundgame)
    idplayer = active_players[0]
    player = players_game[idplayer]
    gamePlayerInfo[id] = {idplayer:{"cardgameID":cardgameID, "initialCard":player["initialCard"], "startingPoints":20, "endingPoints":0}}
    for idplayer in active_players[1:]:
        player = players_game[idplayer]
        gamePlayerInfo[id][idplayer] = {"cardgameID":cardgameID, "initialCard":player["initialCard"], "startingPoints":20, "endingPoints":0}
    return id

def collectEndGamePlayerInfo(active_players,players_game,id):
    for idplayer in active_players:
        player = players_game[idplayer]
        gamePlayerInfo[id][idplayer]["endingPoints"] = player["points"]

def sendGamePlayerInfo_db(gamePlayerInfoID,active_players):
    gamePlayer = gamePlayerInfo[gamePlayerInfoID]
    car = "B01"
    for idplayer in active_players:
        cursor.execute('insert into player_game values ('+str(gamePlayer[idplayer]["cardgameID"])+',"'+idplayer+'","'+car+'",'+str(gamePlayer[idplayer]["startingPoints"])+','+str(gamePlayer[idplayer]["endingPoints"])+')')
    conexion.commit()

# player_game BD
def generateRoundInfoID(lastID):
    for id in roundInfo:
        lastID = int(str(id)[0])
    lastID = lastID+1
    return lastID

def collectRoundInfo1(active_players,players_game,roundID,cardgameID):
    id = generateRoundInfoID(roundID)
    idplayer = active_players[0]
    player = players_game[idplayer]
    if player["bank"]:
        player["bank"] = 1
    else:
        player["bank"] = 0
    roundInfo[id] = {idplayer:{"cardgameID":cardgameID, "roundNum":roundID, "playerID":idplayer, "isBank":player["bank"], "betPoints":player["bet"], "cards_value":player["roundPoints"], "startingRoundPoints":player["points"], "endingRoundPoints":0}}
    for idplayer in active_players[1:]:
        player = players_game[idplayer]
        roundInfo[id][idplayer] = {"cardgameID":cardgameID, "roundNum":roundID, "playerID":idplayer, "isBank":player["bank"], "betPoints":player["bet"], "cards_value":player["roundPoints"], "startingRoundPoints":player["points"], "endingRoundPoints":0}
    return id

def collectRoundInfo2(active_players,players_game,id):
    for idplayer in active_players:
        player = players_game[idplayer]
        roundInfo[id][idplayer]["endingRoundPoints"] = player["points"]

def sendRoundInfo_db(roundInfoID,active_players):
    round = roundInfo[roundInfoID]
    for idplayer in active_players:
        cursor.execute('insert into player_game_round values ('+str(round[idplayer]["cardgameID"])+','+str(round[idplayer]["roundNum"])+',"'+round[idplayer]["playerID"]+'",'+str(round[idplayer]["isBank"])+','+str(round[idplayer]["betPoints"])+','+str(round[idplayer]["cards_value"])+','+str(round[idplayer]["startingRoundPoints"])+','+str(round[idplayer]["endingRoundPoints"])+')')
    conexion.commit()

#Ranking

def ranking(num):
    if num == 1:
        select = 'select * from profits'
    elif num == 2:
        select = 'select * from games_played'
    elif num == 3:
        select = 'select * from minutes_played'
    
    cursor.execute(select)
    ranking = cursor.fetchall()
    return ranking


#Reports

def report(num):
    if num == 2:
        form = 'select cardgame_id, player_id , max(bet_points) "Apuesta mas alta" from player_game_round where cardgame_id = cardgame_id   group by 1, 2;'
    elif num == 3:
        form = 'select cardgame_id, player_id , min(bet_points) "Apuesta mas baja" from player_game_round where is_bank = 0 and cardgame_id = cardgame_id group by 1, 2;'
    elif num == 5:
        form = 'select cardgame_id, max(ending_round_points-starting_round_points) from player_game_round where player_id in (select player_id from player where human=0) and cardgame_id = cardgame_id group by 1;'
    elif num == 7:
        form = 'select cardgame_id, count(distinct player_id) from player_game_round where is_bank = 1 and cardgame_id = cardgame_id group by 1;'
    elif num == 8:
        form = 'select cardgame_id, avg(bet_points) from player_game_round where bet_points >= (select avg(bet_points) from player_game_round where cardgame_id = cardgame_id) group by 1;'
    elif num == 9:
        form = 'select cardgame_id, avg(bet_points) from player_game_round where bet_points >= (select avg(bet_points) from player_game_round where cardgame_id = cardgame_id) and round_num = 1 group by 1;'
    elif num == 10:
        form = 'select cardgame_id, avg(bet_points) from player_game_round where bet_points >= (select avg(bet_points) from player_game_round where cardgame_id = cardgame_id) and round_num = (select max(round_num) from player_game_round) group by cardgame_id;'
    cursor.execute(form)
    report = cursor.fetchall()
    return report

def createXML(num, data):
    sep = os.linesep
    tab = " "*4
    tab2 = tab + tab
    xml = '<?xml version="1.0" encoding="UTF-8"?>' + sep + '<!DOCTYPE informes SYSTEM "informes.dtd">' + sep + '<informes>' + sep 
    if num == 2:
        xml += tab + '<informe2 id="id_2">' + sep + tab2 + '<cardgame_id>' + str(data[0]) + '</cardgame_id>' + sep + tab2 + '<player_id>' + str(data[1]) + '</player_id>' + sep + tab2 + '<max_betpoints>' + str(data[2]) + '</max_bet_points>' + sep + tab + '</informe2>'
    elif num == 3:
        xml += tab + '<informe3 id="id_3">' + sep + tab2 + '<cardgame_id>' + str(data[0]) + '</cardgame_id>' + sep + tab2 + '<player_id>' + str(data[1]) + '</player_id>' + sep + tab2 + '<min_betpoints>' + str(data[2]) + '</min_bet_points>' + sep + tab + '</informe3>'
    elif num == 5:
        xml += tab + '<informe5 id="id_5">' + sep + tab2 + '<cardgame_id>' + str(data[0]) + '</cardgame_id>' + sep + tab2 + '<points_won>' + str(data[1]) + '</points_won>' + sep + tab + '</informe5>'
    elif num == 7:
        xml += tab + '<informe7 id="id_7">' + sep + tab2 + '<cardgame_id>' + str(data[0]) + '</cardgame_id>' + sep + tab2 + '<user_bank>' + str(data[1]) + '</user_bank>' + sep + tab + '</informe7>'
    elif num == 8:
        xml += tab + '<informe8 id="id_8">' + sep + tab2 + '<cardgame_id>' + str(data[0]) + '</cardgame_id>' + sep + tab2 + '<average_bet>' + str(data[1]) + '</average_bet>' + sep + tab + '</informe8>'
    elif num == 9:
        xml += tab + '<informe9 id="id_9">' + sep + tab2 + '<cardgame_id>' + str(data[0]) + '</cardgame_id>' + sep + tab2 + '<num_round>' + str(data[1]) + '</num_round>' + sep + tab + '</informe9>'
    elif num == 10:
        xml += tab + '<informe10 id="id_10">' + sep + tab2 + '<cardgame_id>' + str(data[0]) + '</cardgame_id>' + sep + tab2 + '<num_round>' + str(data[1]) + '</num_round>' + sep + tab + '</informe10>'
    xml += sep + '</informes>'
    file = 1
    while True:
        if os.path.isfile('./informes/informe'+str(file)+'.xml'):
            break
        else:
            file += 1
    file = open('./informes/informe'+str(file)+'.xml', "a")
    file.write(xml)
    file.close()










