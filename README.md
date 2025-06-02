# powershell-game
### What is this project?
powershell-game is a small application/video game framework for Windows Powershell built with the `curses` python library. 
### How to Run:
Ensure that python is installed. In Windows Powershell, change to the project directory and run `python main.py` 

### How its made:
This project was made with a video game in mind, but all functionality applies to a general application. 

#### Screens
One of the most fundamental components of a video game is having distinct "screens" that separate the functionality of the game, such as having a welcome "screen" and a distinct game "screen," in which each are separately loaded when commanded to change state. In `curses`, the `stdscr` object represents this idea of a screen, where windows with buffers of characters may be placed on top of and refreshed with characters.
\
To mimic the concept of having multiple screens, I created a `Screen()` superclass that implements some basic functionality of a screen:

- Keyboard character input from `stdin` stored in a `deque`
- A stored list of windows that a user would like to associate with a screen
- Read/Write methods to global buffers, allowing cross communication of screen

The constructor of a subclass should set up the windows of a desired screen using `curses.newwin()` and add them to the class window list with `self.add_windows(...)`. A subclass of should also necessarily override the `handle_input()` method, allowing for user interaction with key-presses.

#### Event Loop
The event loop uses fixed time steps to run based on the set value of `FRAMES_PER_SECOND` in `main.py`. A variable `curr_screen` maintains a reference to a derived `Screen()` object, which in each loop will be checked for events and redraw the screen. Changes to the screen should be made with the `Screen.tick()` function, which is called every frame.

#### Manager Modules
To allow for cross communication of screens, modules `screen_manager` and `buffer_manager` are implemented. The screen manager can generate and change the `curr_screen` object if requested by the event handler, and the buffer manager maintains lists accessible by each screen to store and retrieve necessary data between screen changes.

#### Tile Maps
In general gaming/application development, screens and art are manually created by developers/designers, and the same must be done here. A `TileMap` object represents the content of a curses window by transforming an array of integers numbered `0, 1, 2, ... , N-1` into Unicode characters using a dictionary mapping. The Unicode string can be extracted from the `TileMap` object, and written to a window using `<window>.addstr(<map>.string)`.

### Improvements (TODO):
- Refactor `handle_input()` to `handle_event()` to generalize inputs in the event loop
- Move screen redraw inside of event check
- Place screens inside of a directory and automate the creation of `screen_manager` and `buffer_manager`
