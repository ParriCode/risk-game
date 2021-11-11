import colorama as cr
import os
tablero = {
"eeuu"     : {"name" : "eeuu"     ,"armi": 0,"player": -1,"continent": "north america"},
"china"    : {"name" : "china"    ,"armi": 0,"player": -1,"continent": "asia"},
"alemania" : {"name" : "alemania" ,"armi": 0,"player": -1,"continent": "europa"},
"brasil"   : {"name" : "brasil"   ,"armi": 0,"player": -1,"continent": "sur america"},
"australia": {"name" : "australia","armi": 0,"player": -1,"continent": "oceania"}
}
players = {}
#clase del jugador
class player:
    def __init__(self,name,id):
        self.name = name
        self.armi = 0
        self.new_armi = 10
        self.id = id
        self.country_list = []
    def AddCountry(self,country):
        self.country_list.append(country)
    def NewArmi(self,n):
        self.new_armi += n
        self.armi -= n

#Comienza el juego
init_trooper_player = 0
n_players = int(input("Cuatos jugadores van a jugar ?: "))
if n_players > 6 or n_players < 2: print(cr.Fore.RED+"ERROR , el maximo de jugadores son 6"+cr.Fore.RESET); quit()
if n_players == 2: init_trooper_player = 40
if n_players == 3: init_trooper_player = 35
if n_players == 4: init_trooper_player = 30
if n_players == 5: init_trooper_player = 25
if n_players == 6: init_trooper_player = 20

for singer_player in range(n_players):
    player_name = input(f"nombre del jugador {singer_player}? :")
    players.update({singer_player: player(player_name,singer_player)})
os.system("clear") #limpia la consola
print(cr.Fore.CYAN+cr.Style.BRIGHT+"Fase de colocación de tropas"+cr.Fore.RESET+cr.Style.RESET_ALL)
nid = 0
count_for_trooper= init_trooper_player*n_players
while True:
    os.system("clear")
    enable_countries = ""
    disable_countries = ""
    for c in tablero.keys():
        if tablero[c]["player"] == nid or tablero[c]["player"] == -1:
            enable_countries  += c+"  "+str(tablero[c]["armi"])+"\n"
        else:
            disable_countries += c+"  "+str(tablero[c]["armi"])+"\n"

    print("Paises disponibles")
    print(cr.Fore.GREEN +enable_countries+cr.Fore.RESET)
    print(cr.Fore.RED + disable_countries + cr.Fore.RESET)
    gate = False
    n_tropas = players[nid].new_armi
    players[nid].NewArmi(-1)

    if players[nid].new_armi > 0:
        print(f"Turno de {players[nid].name} // tropas restates {players[nid].new_armi}" )
        country = input(f"Escoge país para asignar tropas: ")
        for c in tablero.keys():
            if country == c:
                gate = True
                if tablero[c]["player"] == -1 or tablero[c]["player"] == nid:
                    tablero[country]["armi"] += 1
                    tablero[country]["player"] = nid

    nid += 1
    if nid >= n_players: nid = 0
    count_for_trooper += 1
    if count_for_trooper>10*4:break
   # print(tablero)
nid = 0
while True:
    quit()

