import pygame
from classes.Game import Game

# Setting up the title of the game, and the window size:
game_title = 'Initial ABCross D'
screen_width = 800
screen_height = 800

# Initializing PYGAME:
pygame.init()

#Running the game:
game = Game(game_title, screen_width, screen_height, 'background.png')
game.run_game_loop(1)

# Leaving PYGAME:
pygame.quit()
quit()
