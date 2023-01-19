
import random
from funciones import *
from dictionary import *
import pyfiglet # libreria para los titulos
import os

menu00=" "*30+"1) Add/Remove/Show Players\n"+" "*30+"2) Settings\n"+" "*30+"3) Play Game\n"+" "*30+"4) Ranking\n"+" "*30+"5) Reports\n"+" "*30+"6) Exit"
menu01=" "*30+"1)New Human Player\n"+" "*30+"2)New Boot\n"+" "*30+"3)Show/Remove Players\n"+" "*30+"4)Go back"
menu02=" "*30+"1)Set Game Players\n"+" "*30+"2)Set Card's Deck\n"+" "*30+"3)Set Max Rounds (Default 5 Rounds)\n"+" "*30+"4)Go back"
menu03=" "*30+"1) View Stats\n"+" "*30+"2) View Game Stats\n"+" "*30+"3) Set Bet\n"+" "*30+"4) Order Card\n"+" "*30+"5) Automatic\n"+" "*30+"6) Stand"
menu04=" "*30+"1)Players With More Earnings\n"+" "*30+"2)Players With More Games Played\n"+" "*30+"3)Players With More Minutes Played\n"+" "*30+"4)Go back"
menu05=" "*30+"1) Initial card more repeated by each user," \
       "\n"+" "*30+"   only users who have played a minimum of 3 games.\n" \
       +" "*30+"2) Player who makes the highest bet per game,\n" \
       +" "*30+"  find the round whit the highest bet.\n" \
       +" "*30+"3) Player who makes the lowest bet per game.\n" \
       +" "*30+"4) Percentage of rounds won per player in each game\n" \
       +" "*30+"   (%), as well as their average bet for the game.\n" \
       +" "*30+"5) List of games won by Bots.\n" \
       +" "*30+"6) Round won by the bank in each game.\n" \
       +" "*30+"7) Number of users have been the bank in each game.\n" \
       +" "*30+"8) Average bet per game.\n" \
       +" "*30+"9) Average bet of the firs round of each game.\n" \
       +" "*30+"10) Average bet of the last round of each game.\n" \
       +" "*30+"11) Go back"
menu3h=" "*30+"1) View Stats\n"+" "*30+"2) View Game Stats\n"+" "*30+"3) Set Bet\n"+" "*30+"4) Order Card\n"+" "*30+"5) Automatic Play\n"+" "*30+"6) Stand"
menu22=" "*30+"1)ESP-ESP\n"+" "*30+"2)POK-POK\n"+" "*30+"0)GO BACK\n"
listajugadores=[]
carta = "ESP"
rounds = 5
salir=True
flg_00=True
flg_01 = False
flg_02 = False
flg_03 = False
flg_04 = False
flg_05 = False
cartas = esp

while salir:
    while flg_00:
        clear()
        titulos("Seven And  Half Esteve Terradas i illa")                                       #
        opc=getOpt(menu00," "*30+"Option: ",[1,2,3,4,5,6])
        if opc==1:
            clear()
            flg_00 = False
            flg_01 = True
        if opc==2:
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
        titulos("BBDD Players")                                                                         #
        opc1 = getOpt(menu01, " "*30+"Option: ", [1, 2, 3, 4])
        if opc1 == 1:
            addPlayer(players_registered)


        if opc1 == 2:
            addPlayerB(players_registered)

        if opc1 == 3:
            clear()
            titulos("BBDD Players")                                                                     #
            while True:
                listasid=[]
                for id in  players_registered.keys():
                    listasid.append(id)
                tablaRemo(players_registered,listasid)
                op=input(" "*20+"Option ( -id to remove players, -1 to exit ): ")

                if op[1:] in listasid:
                    del players_registered[op[1:]]
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
        titulos("Settings")                                                                             #
        opc2=getOpt(menu02," "*30+"Option: ",rangeList=[1,2,3,4])
        if opc2==1:
            clear()
            listaj=[]
            op=""
            titulos("Settings")
            print("*"*20 + "Actuals Players In Game"+"*"*20)
            if len(listajugadores)==0:
                print("There is no players in game")
                input("Press enter to continue")
            else:
                for i in listajugadores:
                    print(i, players_registered[i]["name"], players_registered[i]["human"], players_registered[i]["type"])
                input("Press enter to continue")
            while True:
                clear()
                titulos("Settings")
                for key in players_registered:
                    if key not in listaj and key not in listajugadores:
                        listaj.append(key)
                if len(listajugadores) >= 6:
                    print("*"*20 + "You have the maximum players"+"*"*20 )
                    input("Press enter to continue")
                    break
                tablaRemo(players_registered,listaj)
                op = input("Option ( id to add to play,-id to remove players,sh to show actual players in the game, -1 to go back ): ")
                listasid = []
                for id in players_registered.keys():
                    listasid.append(id)
                if op in listasid and op not in listajugadores and len(listajugadores)<=6:

                    listajugadores.append(op)
                    listaj.remove(op)
                    print("*" * 20 + "Actuals Players In Game" + "*" * 20)
                    print("{:<10} {:<10} {:<10} {:<10}  ".format("Player ID", "Name", "Human", "Typed"))
                    print("*" * 80)
                    for j in listajugadores:

                        print("{:<10} {:<10} {:<10} {:<10}  ".format(j, players_registered[j]["name"], players_registered[j]["human"], players_registered[j]["type"]))
                    input("Press enter to continue")
                elif op[1:] in listasid and op[0]=="-":
                    listajugadores.remove(op[1:])
                    print("*" * 20 + "Actuals Players In Game" + "*" * 20)
                    if len(listajugadores) > 0:
                        print("{:<10} {:<10} {:<10} {:<10}  ".format("Player ID", "Name", "Human", "Typed"))
                        print("*" * 80)
                        for i in listajugadores:
                            print("{:<10} {:<10} {:<10} {:<10}  ".format(i, players_registered[i]["name"], players_registered[i]["human"], players_registered[i]["type"]))
                        input("Press enter to continue")
                    else:
                        print("*" * 20 + "Actuals Players In Game" + "*" * 20)
                        print("There is no players in game")
                        input("Press enter to continue")
                elif op=="sh":
                    if len(listajugadores)>0:
                        print("{:<10} {:<10} {:<10} {:<10}  ".format("Player ID", "Name", "Human", "Typed"))
                        print("*" * 80)
                        for i in listajugadores:
                            print("{:<10} {:<10} {:<10} {:<10}  ".format(i, players_registered[i]["name"], players_registered[i]["human"], players_registered[i]["type"]))
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
            clear()
            titulos("Settings")                                                                         #
            cartas = getOpt(menu22, " "*30+"Option: ", rangeList=[1, 2, 0])
            if cartas==1:
                print("Established Card Deck ESP, Baraja Española\n")
                input("Enter to continue")
                cartas = setCards(esp)
                carta = "ESP"
            if cartas==2:
                print("Established Card Deck POK, Baraja de Poker\n")
                input("Enter to continue")
                cartas = setCards(pok)
                carta = "POK"
            clear()
        if opc2==3:
            while True:
                clear()
                titulos("Settings")
                print("Maximum 30")#
                rounds=input("Max Rounds: ")
                if int(rounds)<=30:
                    break
            print("Established maxim of rounds to: ",rounds)
            input("Enter to continue")
            clear()
        if opc2==4:
            flg_00 = True
            flg_02 = False

    while flg_03:
        #Temp

        #Checkear que ni la baraja ni la lista de jugadores esten vacios
        mal = CheckNotEmpty("Has de elegir una baraja","No hay jugadores seleccionados",carta, listajugadores)
        if mal:
            flg_00, flg_03 = True, False
            continue
        #Empieza el juego
        roundgame = 0
        avaliable_cards = setCards(cartas)
        players_game = setPlayers(listajugadores,players_registered)
        players_game = quitBank(players_game)
        players_game = setGamePriority(list(players_game.keys()), cartas, players_game)         #Orden inicial de los jugadores, setear la banca
        players_game_keys = list(players_game.keys())
        active_players = ordenarPlayers(players_game) 
        while roundgame < int(rounds) and len(active_players) > 1:
            bank = bankCheck(players_game)
            clear()
            titulos("Seven And Half")
            passed = False
            active_players = ordenarPlayers(players_game)                                          #Lista de jugadores activos con puntos ordenada
            players_game = resetCardsAndPoints(players_game)                                       #Resetear puntos de la ronda y las cartas de cada jugador
            avaliable_cards = setCards(cartas)                                                               #Resetear las cartas disponibles
            for id in active_players:
                name=players_game[id]["name"]                                                               #Empieza la ronda de los jugadores NO banca
                if players_game[id]["human"] == False and players_game[id]["bank"] == False:       #Si es Bot
                    clear()
                    titulos("Seven And Half") 
                    players_game[id] = roundBot(players_game[id],avaliable_cards)
                    avaliable_cards = removeCardsFromDeck(players_game[id],avaliable_cards)
                    print( "Round "+str(roundgame) +" Turn of "+players_game[id]["name"])
                    print(print_ronda(players_game_keys, players_game, players_registered))# printa las estats de la ronda de LOS PLAYERS
                    input(" "*50+"Enter to continue\n")
                elif players_game[id]["human"] == True and players_game[id]["bank"] == False and passed == False:      #Si es humano
                    players_game[id] = roundPlayer(players_game[id],avaliable_cards,players_game,roundgame,active_players,name,bank,players_game_keys,menu3h)
                    avaliable_cards = removeCardsFromDeck(players_game[id],avaliable_cards)
                    passed = True
            for banca in active_players:
                if players_game[banca]["human"] == False and players_game[banca]["bank"] == True:   #Si es bot y Banca
                    players_game[banca] = roundBankBot(players_game[banca],avaliable_cards,players_game,banca)
                    clear()                                                                                 #
                    titulos("Seven And Half")                                                               #
                    print(" "*30+"Round " + str(roundgame) + " Turn of " + players_game[banca]["name"])     # printa las estats de la ronda de LA BANCA
                    print(print_ronda(players_game_keys, players_game, players_registered))                 #
                    input(" "*50+"Enter to continue\n")                                                     #
                elif players_game[banca]["human"] == True and players_game[banca]["bank"] == True and passed == False:      #Si es humano y Banca

                    players_game[banca] = roundPlayer(players_game[banca],avaliable_cards,players_game,roundgame,active_players,name,banca,players_game_keys, menu3h)
                    avaliable_cards = removeCardsFromDeck(players_game[banca],avaliable_cards)
                    passed = True
            players_game = pointsGiving(active_players,players_game, bank)
            active_players = checkLosers(active_players,players_game)
            players_game = checkChangeBank(active_players,players_game,bank)
            #printear
            clear()
            titulos("Seven And Half","STATS AFTER ROUND "+str(roundgame))                                   #
            print(print_ronda(players_game_keys, players_game, players_registered))                         #
            roundgame += 1
            exitj = input(" " * 30 + "Enter to continue to new Round, exit to leave game: ")
            if exitj == "exit":
                break
        clear()
        if exitj != "exit":
            checkWinner(active_players, players_game,roundgame)
            input()
        flg_00 = True
        flg_03 = False
        clear()
    while flg_04 :
       clear()
       titulos("Ranking")                                                                                #
       opc4 = getOpt(menu04, " "*30+"Option:", rangeList=[1, 2, 3,4])
       if opc4==1:
           print()
           print("*" * 75)
           print("{:<10} {:<25} {:<10} {:<10}  {:<10}".format("Player ID", "Name", "Earnings", "Games Played",
                                                              "Minutes Played"))
           print("*" * 75)
           input()
       if opc4==2:
           print()
           print("*" * 75)
           print("{:<10} {:<25} {:<10} {:<10}  {:<10}".format("Player ID", "Name", "Earnings", "Games Played",
                                                              "Minutes Played"))
           print("*" * 75)
           input()
       if opc4==3:
           print()
           print("*" * 75)
           print("{:<10} {:<25} {:<10} {:<10}  {:<10}".format("Player ID", "Name", "Earnings", "Games Played",
                                                              "Minutes Played"))
           print("*" * 75)
           input()
       if opc4==4:
           flg_00 = True
           flg_04 = False  
    while flg_05:
        clear()
        titulos("Reports")                                                                              #
        opc5 = getOpt(menu05, " "*30+"Option:", rangeList=[1, 2, 3,4,5,6,7,8,9,10,11])
        if opc5==11:
            flg_00 = True
            flg_05 = False
            clear()
