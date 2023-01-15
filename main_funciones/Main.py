import random
from funciones import *
from dictionary import *
import os

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
listajugadores=[]
carta = ""
rounds = 5
salir=True
flg_00=True
flg_01 = False
flg_02 = False
flg_03 = False
flg_04 = False
flg_05 = False


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
            addPlayer(players_registered)
            print(players_registered)
        if opc1 == 2:
            addPlayerB(players_registered)
            print(players_registered)
        if opc1 == 3:
            while True:
                listasid=[]
                tablaRemo(players_registered)
                op=input("Option ( -id to remove players, -1 to exit ): ")
                for id in  players_registered.keys():
                    listasid.append(id)
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
        opc2=getOpt(menu02,"Option: ",rangeList=[1,2,3,4])
        if opc2==1:
            clear()
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
                tablaRemo(players_registered)
                op = input("Option ( id to add to play,-id to remove players,sh to show actual players in the game, -1 to go back ): ")
                listasid = []
                for id in players_registered.keys():
                    listasid.append(id)
                if op in listasid and op not in listajugadores:
                    listajugadores.append(op)
                    print("*" * 20 + "Actuals Players In Game" + "*" * 20)
                    for j in listajugadores:
                        print("{:<10} {:<10} {:<10} {:<10}  ".format("Player ID", "Name", "Human","Typed"))
                        print("*"*80)

                        print("{:<10} {:<10} {:<10} {:<10}  ".format(j, players_registered[j]["name"], players_registered[j]["human"], players_registered[j]["type"]))
                        input("Press enter to continue")
                elif op[1:] in listasid and op[0]=="-":
                    listajugadores.remove(op[1:])
                    print("*" * 20 + "Actuals Players In Game" + "*" * 20)
                    if len(listajugadores) > 0:
                        for i in listajugadores:
                            print("{:<10} {:<10} {:<10} {:<10}  ".format("Player ID", "Name", "Human","Typed"))
                            print("*" * 80)
                            print("{:<10} {:<10} {:<10} {:<10}  ".format(i, players_registered[i]["name"], players_registered[i]["human"], players_registered[i]["type"]))
                            input("Press enter to continue")
                    else:
                        print("*" * 20 + "Actuals Players In Game" + "*" * 20)
                        print("There is no players in game")
                        input("Press enter to continue")
                elif op=="sh":
                    if len(listajugadores)>0:
                        for i in listajugadores:
                            print("{:<10} {:<10} {:<10} {:<10}  ".format("Player ID", "Name", "Human", "Typed"))
                            print("*" * 80)
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
        #Temp
        carta="ESP"
        listajugadores = ["11115555A","49883035D"]
        #Checkear que ni la baraja ni la lista de jugadores esten vacios
        mal = CheckNotEmpty("Has de elegir una baraja","No hay jugadores seleccionados",carta, listajugadores)
        if mal:
            flg_00, flg_03 = True, False
            continue
        #Empieza el juego
        roundgame = 0
        bank = ""
        avaliable_cards = setCards(cartas)
        players_game = setPlayers(listajugadores,players_registered)
        players_game = quitBank(players_game)
        players_game = setGamePriority(list(players_game.keys()), cartas, players_game)         #Orden inicial de los jugadores, setear la banca
        players_game_keys = list(players_game.keys())
        while roundgame < rounds or len(active_players) > 1:
            active_players = ordenarPlayers(players_game)                                          #Lista de jugadores activos con puntos ordenada
            players_game = resetCardsAndPoints(players_game)                                       #Resetear puntos de la ronda y las cartas de cada jugador
            avaliable_cards = setCards(cartas)                                                               #Resetear las cartas disponibles
            for id in active_players:                                                              #Empieza la ronda de los jugadores NO banca
                if players_game[id]["human"] == False and players_game[id]["bank"] == False:
                    players_game[id] = roundBot(players_game[id],avaliable_cards)
                    avaliable_cards = removeCardsFromDeck(players_game[id],avaliable_cards)
                elif players_game[id]["human"] == False and players_game[id]["bank"] == False:
                    #Codigo para el player
                    continue
            for banca in active_players:
                if players_game[banca]["human"] == False and players_game[banca]["bank"] == True:
                    players_game[banca] = roundBankBot(players_game[banca],avaliable_cards,players_game,banca)
                    bank = banca
            players_game = pointsGiving(active_players,players_game, bank)
            active_players = checkLosers(active_players,players_game)
            players_game = checkChangeBank(active_players,players_game,bank)
            #printear
            for printear in players_game_keys:
               print(printear+" points have: "+str(players_game[printear]["points"])+ " c: "+str(players_game[printear]["cards"])+" rounPoints: "+str(players_game[printear]["roundPoints"]))
            print(active_players)
            input()
            clear()
            roundgame += 1
        print("Ganador:" + str(players_game[active_players[0]]["name"]))    
        input()
        flg_00 = True
        flg_03 = False
        clear()
        # opc4 = getOpt(menu03, "Option:", rangeList=[1, 2, 3, 4,5,6])

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
