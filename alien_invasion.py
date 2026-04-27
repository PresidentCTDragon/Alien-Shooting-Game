import sys
import pygame
from settings import Settings
from ship import Ship
#from cuphead import Cuphead

class AlienInvasion:
    """ Class to manage game assets and initialize the game. """     
    def __init__(self):
        pygame.init()
        self.settings = Settings()
        self.clock = pygame.time.Clock()
        # Dimensions of the screen    
        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption("Alien Invasion")
        self.ship = Ship(self)
        #self.cuphead = Cuphead(self)
    
    def run_game(self):
        """ Start the main loop for the game. """
        while True:
            # Watch for keyboard and mouse events.       
            self._check_events()
            self._update_screen()
            self.clock.tick(60) # make it run at 60fps
    
    def _check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
    
    # Redraw the screen during each pass through the loop
    def _update_screen(self):
        self.screen.fill(self.settings.bg_color)
        self.ship.blitme()
        #self.cuphead.blitme()
        # Make the most recently drawn screen visible.
        pygame.display.flip()

if __name__ == '__main__':
    ## Make a game instance and run the game.
    ai = AlienInvasion()
    ai.run_game()