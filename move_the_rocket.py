import sys
import pygame
from settings import Settings
from rocket import Rocket


class MoveTheRocket:
    """ Class to manage game assets and initialize the game. """     
    def __init__(self):
        pygame.init()
        self.settings = Settings()
        self.clock = pygame.time.Clock()
        # Dimensions of the screen    
        self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        self.settings.screen_width = self.screen.get_rect().width
        self.settings.screen_height = self.screen.get_rect().height
        pygame.display.set_caption("Move the Rocket")
        self.rocket = Rocket(self)
    
    def run_game(self):
        """ Start the main loop for the game. """
        while True:
            # Watch for keyboard and mouse events.       
            self._check_events()
            self.rocket.update()
            self._update_screen()
            self.clock.tick(60) # make it run at 60fps
    
    def _check_events(self):
        """ Respond to keypresses and mouse events. """
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
            
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)
                    
    def _check_keydown_events(self, event):
        """ Respond to keypresses """
        if event.key == pygame.K_RIGHT:
            self.rocket.moving_right = True
                    
        elif event.key == pygame.K_LEFT:
            self.rocket.moving_left = True
            
        elif event.key == pygame.K_UP:
            self.rocket.moving_up = True
            
        elif event.key == pygame.K_DOWN:
            self.rocket.moving_down = True
            
        elif event.key == pygame.K_q:
            sys.exit()
            
            
    def _check_keyup_events(self, event):
        """ Respond to key releases """
        if event.key == pygame.K_RIGHT:
            self.rocket.moving_right = False            
                    
        elif event.key == pygame.K_LEFT:
            self.rocket.moving_left = False

        elif event.key == pygame.K_UP:
            self.rocket.moving_up = False

        elif event.key == pygame.K_DOWN:
            self.rocket.moving_down = False


    # Redraw the screen during each pass through the loop
    def _update_screen(self):
        self.screen.fill(self.settings.bg_color)
        self.rocket.blitme()
        # Make the most recently drawn screen visible.
        pygame.display.flip()

if __name__ == '__main__':
    ## Make a game instance and run the game.
    ai = MoveTheRocket()
    ai.run_game()