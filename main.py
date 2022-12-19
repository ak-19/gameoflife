from setup import Setup

from game import Game

setup = Setup()

display = setup.get_display()

game = Game(display)

game.run_loop()

setup.quit()