from main_screen import MainScreen
from stat_screen import StatScreen
from game_screen import GameScreen
from death_screen import DeathScreen

'''
screen_manager.py

Manager class that maps a name of a requested string to an object
'''
screens = {
	"main" : MainScreen,
	"stat" : StatScreen,
	"game" : GameScreen,
	"death" : DeathScreen,
}

# From the event loop, calling handle_screen("main", stdscr) will return MainScreen() object
def handle_screen(new_screen, stdscr):
	return screens[new_screen](stdscr=stdscr)