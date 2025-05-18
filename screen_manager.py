from main_screen import MainScreen
from stat_screen import StatScreen
from game_screen import GameScreen

screens = {
	"main" : MainScreen,
	"stat" : StatScreen,
	"game" : GameScreen
}

def handle_screen(new_screen, stdscr):
	return screens[new_screen](stdscr=stdscr)