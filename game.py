import colorama as cr
import os
tablero = {
"alaska"                  : {"name" : "Alaska"                ,"armi": 0,"player": -1,"continent": "north_america"},
"northwest_territory"     : {"name" : "Northwest Territory"   ,"armi": 0,"player": -1,"continent": "north_america"},
"alberta"                 : {"name" : "Alberta"               ,"armi": 0,"player": -1,"continent": "north_america"},
"ontario"                 : {"name" : "Ontario"               ,"armi": 0,"player": -1,"continent": "north_america"},
"werstern united states"  : {"name" : "Werstern United States","armi": 0,"player": -1,"continent": "north_america"},
"centeur america"         : {"name" : "Centeur America"       ,"armi": 0,"player": -1,"continent": "north_america"},
"eastern united states"   : {"name" : "Eastern United States" ,"armi": 0,"player": -1,"continent": "north_america"},
"quebec"                  : {"name" : "Quebec"                ,"armi": 0,"player": -1,"continent": "north_america"},
"greenland"               : {"name" : "Greenland"             ,"armi": 0,"player": -1,"continent": "north_america"},

"venezuela"               : {"name" : "Venezuela"   ,"armi": 0,"player": -1,"continent": "sourth_america"},
"Peru"                    : {"name" : "Venezuela"   ,"armi": 0,"player": -1,"continent": "sourth_america"},
"Argentina"               : {"name" : "Argentina"   ,"armi": 0,"player": -1,"continent": "sourth_america"},
"brasil"                  : {"name" : "brasil"      ,"armi": 0,"player": -1,"continent": "sourth_america"},

"iceland"                 : {"name" : "Iceland"        ,"armi": 0,"player": -1,"continent": "europe"},
"Scandinavia"             : {"name" : "Scandinavia"    ,"armi": 0,"player": -1,"continent": "europe"},
"gread_britain"           : {"name" : "Great Britain"  ,"armi": 0,"player": -1,"continent": "europe"},
"werst_europe"            : {"name" : "Werst Europe"   ,"armi": 0,"player": -1,"continent": "europe"},
"north_europe"            : {"name" : "North Europe"   ,"armi": 0,"player": -1,"continent": "europe"},
"ukraini"                 : {"name" : "Ukraini"        ,"armi": 0,"player": -1,"continent": "europe"},
"sourth_europe"           : {"name" : "Sourth Europe"  ,"armi": 0,"player": -1,"continent": "europe"},

"north_africa"            : {"name" : "North Africa"   ,"armi": 0,"player": -1,"continent": "africa"},
"egyipt"                  : {"name" : "North Africa"   ,"armi": 0,"player": -1,"continent": "africa"},
"east_africa"             : {"name" : "North Africa"   ,"armi": 0,"player": -1,"continent": "africa"},
"congo"                   : {"name" : "North Africa"   ,"armi": 0,"player": -1,"continent": "africa"},
"sourth_africa"           : {"name" : "Sourth Africa"  ,"armi": 0,"player": -1,"continent": "africa"},
"madalagascar"            : {"name" : "Madalasgar"     ,"armi": 0,"player": -1,"continent": "africa"},

"ural"               : {"name" : "Ural"            ,"armi": 0,"player": -1,"continent": "asia"},
"siberia"            : {"name" : "Siberia"         ,"armi": 0,"player": -1,"continent": "asia"},
"afghanistan"        : {"name" : "Afghanistan"     ,"armi": 0,"player": -1,"continent": "asia"},
"middle_east"        : {"name" : "Middle East"     ,"armi": 0,"player": -1,"continent": "asia"},
"yakutsk"            : {"name" : "Yakutsk"         ,"armi": 0,"player": -1,"continent": "asia"},
"irkust"             : {"name" : "Irkust"          ,"armi": 0,"player": -1,"continent": "asia"},
"mongolia"           : {"name" : "Mongolia"        ,"armi": 0,"player": -1,"continent": "asia"},
"china"              : {"name" : "China"           ,"armi": 0,"player": -1,"continent": "asia"},
"india"              : {"name" : "India"           ,"armi": 0,"player": -1,"continent": "asia"},
"sourteast_asia"     : {"name" : "SourthEast Asia" ,"armi": 0,"player": -1,"continent": "asia"},
"japan"              : {"name" : "Japan"           ,"armi": 0,"player": -1,"continent": "asia"},
"kaimchatka"         : {"name" : "Kaimchatka"      ,"armi": 0,"player": -1,"continent": "asia"},

"indonesia"        : {"name" : "Australia"        ,"armi": 0,"player": -1,"continent": "oceania"},
"new_guinea"       : {"name" : "Australia"        ,"armi": 0,"player": -1,"continent": "oceania"},
"eastern_australia": {"name" : "Eastern Australia","armi": 0,"player": -1,"continent": "oceania"},
"western_australia": {"name" : "Western Australia","armi": 0,"player": -1,"continent": "oceania"}
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
    def AddNewArmy(self,n):
        self.new_armi += n
    def SubArmi(self,n):
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
    players[nid].SubArmi(-1)

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
    player_countries = players[nid].country_list
    n_countries = len(player_countries)

    players[nid].AddNewArmy(int(n_countries/5)+3)
    print()
    nid +=1
    if nid > n_players: nid = 0



