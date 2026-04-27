import pygame

class Cuphead: 
    """ A class to manage Cuphead. """
    def __init__(self, ai_game):
        """ Initialize Cuphead and set his starting position. """
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()
        
        # Load the Cuphead image and get its rect.
        self.image = pygame.image.load('assets/cuphead.bmp')
        self.rect = self.image.get_rect()
        
        # Start each new Cuphead at the bottom center of the screen.
        self.rect.center = self.screen_rect.center
        
    def blitme(self):
        """Draw Cuphead at his current location."""
        self.screen.blit(self.image, self.rect)
            