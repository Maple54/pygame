from states import State
import os, time, pygame


class main_game(State):
    def __init__(self, game):
        State.__init__(self, game)
  
        

    def update(self, delta_time, actions):
      pass

    def render(self, display):
        display.fill('Red')
        self.game.draw_text(display, "Main Game", (0,0,0), self.game.GAME_W/2, self.game.GAME_H/2 )
