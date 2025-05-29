from main_screen import MainScreen
from stat_screen import StatScreen
from game_screen import GameScreen
from death_screen import DeathScreen

screens = {
	"main" : MainScreen,
	"stat" : StatScreen,
	"game" : GameScreen,
	"death" : DeathScreen,
}

def handle_screen(new_screen, stdscr):
	return screens[new_screen](stdscr=stdscr)