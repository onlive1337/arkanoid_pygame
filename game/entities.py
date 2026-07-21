import pygame

import settings as cfg

class Paddle:
    """ Our main player, Paddle, moves only horizontally. """

    def __init__(self) -> None:
        self.rect = pygame.Rect(0, 0, cfg.PADDLE_WIDTH, cfg.PADDLE_HEIGHT)
        self.rect.midbottom = (cfg.WIDTH // 2, cfg.HEIGHT - 20)
        self.speed = cfg.PADDLE_SPEED
        self.vx = 0
        self.extended = False
        self.laser = False

    def move(self, keys: pygame.key.ScancodeWrapper):
        """ Moves the Paddle if the key is pressed. """
        self.vx = 0
        if keys[pygame.K_LEFT]:
            self.vx = -self.speed
        elif keys[pygame.K_RIGHT]:
            self.vx = self.speed
        
        self.rect.x += self.vx

    def draw(self, screen: pygame.Surface) -> None:
        """ Renders the Paddle on the screen. """
        pygame.draw.rect(screen, cfg.PADDLE_COLOR, self.rect, border_radius=5)
