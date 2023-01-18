
players_registered = { "11115555A":{ "name":"Mario" ,"human":False,"bank" :False,"initialCard" :"" ,"priority":0,"type" :40,"bet" :4,"points" :0,"cards" :[],"roundPoints" :0},
            "22225555A":{ "name":"Pedro" ,"human":True,"bank" :False,"initialCard" :"" ,"priority" :0,"type" :40,"bet" :4,"points" :0,"cards" :[],"roundPoints" :0},
            "49883035Z":{ "name":"Alex" ,"human":True,"bank" :False,"initialCard" :"" ,"priority" :0,"type" :40,"bet" :4,"points" :0,"cards" :[],"roundPoints" :0},
            "49883035D":{ "name":"Pepito" ,"human":False,"bank" :False,"initialCard" :"" ,"priority" :0,"type" :40,"bet" :4,"points" :0,"cards" :[],"roundPoints" :0}
}

#value como valor de la carta (del dibujito) y relValue como valor en el juego
esp = {
    "O01": { "literal" : "As de Oros" , "value" : 1, "priority" : 1, "realValue" : 1},
    "O02": { "literal" : "Dos de Oros" , "value" : 2, "priority" : 1, "realValue" : 2},
    "O03": { "literal" : "Tres de Oros" , "value" : 3, "priority" : 1, "realValue" : 3},
    "O04": { "literal" : "Cuatro de Oros" , "value" : 4, "priority" : 1, "realValue" : 4},
    "O05": { "literal" : "Cinco de Oros" , "value" : 5, "priority" : 1, "realValue" : 5},
    "O06": { "literal" : "Seis de Oros" , "value" : 6, "priority" : 1, "realValue" : 6},
    "O07": { "literal" : "Siete de Oros" , "value" : 7, "priority" : 1, "realValue" : 7},
    "O010": { "literal" : "Diez de Oros" , "value" : 10, "priority" : 1, "realValue" : 0.5},
    "O011": { "literal" : "Once de Oros" , "value" : 11, "priority" : 1, "realValue" : 0.5},
    "O012": { "literal" : "DOCE de Oros" , "value" : 12, "priority" : 1, "realValue" : 0.5},
    "C01": { "literal" : "As de Copas" , "value" : 1, "priority" : 2, "realValue" : 1},
    "C02": { "literal" : "Dos de Copas" , "value" : 2, "priority" : 2, "realValue" : 2},
    "C03": { "literal" : "Tres de Copas" , "value" : 3, "priority" : 2, "realValue" : 3},
    "C04": { "literal" : "Cuatro de Copas" , "value" : 4, "priority" : 2, "realValue" : 4},
    "C05": { "literal" : "Cinco de Copas" , "value" : 5, "priority" : 2, "realValue" : 5},
    "C06": { "literal" : "Seis de Copas" , "value" : 6, "priority" : 2, "realValue" : 6},
    "C07": { "literal" : "Siete de Copas" , "value" : 7, "priority" : 2, "realValue" : 7},
    "C010": { "literal" : "Diez de Copas" , "value" : 10, "priority" : 2, "realValue" : 0.5},
    "C011": { "literal" : "Once de Copas" , "value" : 11, "priority" : 2, "realValue" : 0.5},
    "C012": { "literal" : "DOCE de Copas" , "value" : 12, "priority" : 2, "realValue" : 0.5},
    "E01": { "literal" : "As de Espadas" , "value" : 1, "priority" : 3, "realValue" : 1},
    "E02": { "literal" : "Dos de Espadas" , "value" : 2, "priority" : 3, "realValue" : 2},
    "E03": { "literal" : "Tres de Espadas" , "value" : 3, "priority" : 3, "realValue" : 3},
    "E04": { "literal" : "Cuatro de Espadas" , "value" : 4, "priority" : 3, "realValue" : 4},
    "E05": { "literal" : "Cinco de Espadas" , "value" : 5, "priority" : 3, "realValue" : 5},
    "E06": { "literal" : "Seis de Espadas" , "value" : 6, "priority" : 3, "realValue" : 6},
    "E07": { "literal" : "Siete de Espadas" , "value" : 7, "priority" : 3, "realValue" : 7},
    "E010": { "literal" : "Diez de Espadas" , "value" : 10, "priority" : 3, "realValue" : 0.5},
    "E011": { "literal" : "Once de Espadas" , "value" : 11, "priority" : 3, "realValue" : 0.5},
    "E012": { "literal" : "DOCE de Espadas" , "value" : 12, "priority" : 3, "realValue" : 0.5},
    "B01": { "literal" : "As de Bastos" , "value" : 1, "priority" : 4, "realValue" : 1},
    "B02": { "literal" : "Dos de Bastos" , "value" : 2, "priority" : 4, "realValue" : 2},
    "B03": { "literal" : "Tres de Bastos" , "value" : 3, "priority" : 4, "realValue" : 3},
    "B04": { "literal" : "Cuatro de Bastos" , "value" : 4, "priority" : 4, "realValue" : 4},
    "B05": { "literal" : "Cinco de Bastos" , "value" : 5, "priority" : 4, "realValue" : 5},
    "B06": { "literal" : "Seis de Bastos" , "value" : 6, "priority" : 4, "realValue" : 6},
    "B07": { "literal" : "Siete de Bastos" , "value" : 7, "priority" : 4, "realValue" : 7},
    "B010": { "literal" : "Diez de Bastos" , "value" : 10, "priority" : 4, "realValue" : 0.5},
    "B011": { "literal" : "Once de Bastos" , "value" : 11, "priority" : 4, "realValue" : 0.5},
    "B012": { "literal" : "DOCE de Bastos" , "value" : 12, "priority" : 4, "realValue" : 0.5}
}

cartas = esp

pok = {
    "C01": { "literal" : "As de Corazones" , "value" : 1, "priority" : 1, "realValue" : 1},
    "C02": { "literal" : "Dos de Corazones" , "value" : 2, "priority" : 1, "realValue" : 2},
    "C03": { "literal" : "Tres de Corazones" , "value" : 3, "priority" : 1, "realValue" : 3},
    "C04": { "literal" : "Cuatro de Corazones" , "value" : 4, "priority" : 1, "realValue" : 4},
    "C05": { "literal" : "Cinco de Corazones" , "value" : 5, "priority" : 1, "realValue" : 5},
    "C06": { "literal" : "Seis de Corazones" , "value" : 6, "priority" : 1, "realValue" : 6},
    "C07": { "literal" : "Siete de Corazones" , "value" : 7, "priority" : 1, "realValue" : 7},
    "C011": { "literal" : "J de Corazones" , "value" : 11, "priority" : 1, "realValue" : 0.5},
    "C012": { "literal" : "Q de Corazones" , "value" : 12, "priority" : 1, "realValue" : 0.5},
    "C013": { "literal" : "K de Corazones" , "value" : 13, "priority" : 1, "realValue" : 0.5},
    "T01": { "literal" : "As de Treboles" , "value" : 1, "priority" : 2, "realValue" : 1},
    "T02": { "literal" : "Dos de Treboles" , "value" : 2, "priority" : 2, "realValue" : 2},
    "T03": { "literal" : "Tres de Treboles" , "value" : 3, "priority" : 2, "realValue" : 3},
    "T04": { "literal" : "Cuatro de Treboles" , "value" : 4, "priority" : 2, "realValue" : 4},
    "T05": { "literal" : "Cinco de Treboles" , "value" : 5, "priority" : 2, "realValue" : 5},
    "T06": { "literal" : "Seis de Treboles" , "value" : 6, "priority" : 2, "realValue" : 6},
    "T07": { "literal" : "Siete de Treboles" , "value" : 7, "priority" : 2, "realValue" : 7},
    "T011": { "literal" : "J de Treboles" , "value" : 11, "priority" : 2, "realValue" : 0.5},
    "T012": { "literal" : "Q de Treboles" , "value" : 12, "priority" : 2, "realValue" : 0.5},
    "T013": { "literal" : "K de Treboles" , "value" : 13, "priority" : 2, "realValue" : 0.5},
    "P01": { "literal" : "As de Picas" , "value" : 1, "priority" : 3, "realValue" : 1},
    "P02": { "literal" : "Dos de Picas" , "value" : 2, "priority" : 3, "realValue" : 2},
    "P03": { "literal" : "Tres de Picas" , "value" : 3, "priority" : 3, "realValue" : 3},
    "P04": { "literal" : "Cuatro de Picas" , "value" : 4, "priority" : 3, "realValue" : 4},
    "P05": { "literal" : "Cinco de Picas" , "value" : 5, "priority" : 3, "realValue" : 5},
    "P06": { "literal" : "Seis de Picas" , "value" : 6, "priority" : 3, "realValue" : 6},
    "P07": { "literal" : "Siete de Picas" , "value" : 7, "priority" : 3, "realValue" : 7},
    "P011": { "literal" : "J de Picas" , "value" : 11, "priority" : 3, "realValue" : 0.5},
    "P012": { "literal" : "Q de Picas" , "value" : 12, "priority" : 3, "realValue" : 0.5},
    "P013": { "literal" : "K de Picas" , "value" : 13, "priority" : 3, "realValue" : 0.5},
    "D01": { "literal" : "As de Diamantes" , "value" : 1, "priority" : 4, "realValue" : 1},
    "D02": { "literal" : "Dos de Diamantes" , "value" : 2, "priority" : 4, "realValue" : 2},
    "D03": { "literal" : "Tres de Diamantes" , "value" : 3, "priority" : 4, "realValue" : 3},
    "D04": { "literal" : "Cuatro de Diamantes" , "value" : 4, "priority" : 4, "realValue" : 4},
    "D05": { "literal" : "Cinco de Diamantes" , "value" : 5, "priority" : 4, "realValue" : 5},
    "D06": { "literal" : "Seis de Diamantes" , "value" : 6, "priority" : 4, "realValue" : 6},
    "D07": { "literal" : "Siete de Diamantes" , "value" : 7, "priority" : 4, "realValue" : 7},
    "D011": { "literal" : "J de Diamantes" , "value" : 11, "priority" : 4, "realValue" : 0.5},
    "D012": { "literal" : "Q de Diamantes" , "value" : 12, "priority" : 4, "realValue" : 0.5},
    "D013": { "literal" : "K de Diamantes" , "value" : 13, "priority" : 4, "realValue" : 0.5}
}






# for id in activePlayers:
#         playerPoints = players[id]["roundPoints"]
#         bankPoints = players[bank]["roundPoints"]
#         if bankPoints > 7.5:
#             if playerPoints == 7.5 and players[id]["bank"] == False:
#                 player_bet = players[id]["bet"]*2
#                 while player_bet != 0 and players[id]["points"] != 0:
#                     player_bet -= 1
#                     players[id]["points"] += 1
#                     players[bank]["points"] -= 1
#             elif playerPoints < 7.5 and players[id]["bank"] == False:
#                 player_bet = players[id]["bet"]
#                 while player_bet != 0 and players[id]["points"] != 0:
#                     player_bet -= 1
#                     players[id]["points"] += 1
#                     players[bank]["points"] -= 1
#         else:
#             if playerPoints > 7.5 and players[id]["bank"] == False:
#                 player_bet = players[id]["bet"]
#                 while player_bet != 0 and players[id]["points"] != 0:
#                     player_bet -= 1
#                     players[id]["points"] -= 1
#                     players[bank]["points"] += 1
#             if playerPoints == 7.5 and players[id]["bank"] == False:
#                 player_bet = players[id]["bet"]*2
#                 while player_bet != 0 and players[id]["points"] != 0:
#                     player_bet -= 1
#                     players[id]["points"] += 1
#                     players[bank]["points"] -= 1
#             elif playerPoints < bankPoints and players[id]["bank"] == False:
#                 player_bet = players[id]["bet"]
#                 while player_bet != 0 and players[id]["points"] != 0:
#                     player_bet -= 1                                                 
#                     players[id]["points"] -= 1
#                     players[bank]["points"] += 1
#             elif playerPoints > bankPoints and players[id]["bank"] == False:
#                 player_bet = players[id]["bet"]
#                 while player_bet != 0 and players[bank]["points"] != 0:
#                     player_bet -= 1
#                     players[id]["points"] += 1
#                     players[bank]["points"] -= 1