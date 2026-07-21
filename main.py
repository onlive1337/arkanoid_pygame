import pygame
import settings as cfg
from screens.game_screen import run as game_screen
from game.entities import Paddle

def main():
    pygame.init()
    screen = pygame.display.set_mode((cfg.WIDTH, cfg.HEIGHT))
    pygame.display.set_caption("Arkanoid")
    clock = pygame.time.Clock()

    running = True
    paddle = Paddle()

    while running:
        # Main Loop
        screen.fill(cfg.BLACK)

        # Update Section
        keys = pygame.key.get_pressed()

        paddle.move(keys)

        # Draw Section
        paddle.draw(screen)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:   # Press "close" button
                running = False


        pygame.display.flip()   # Screen Update
        clock.tick(cfg.FPS)         # FPS (Frames Per Second)

    pygame.quit()

if __name__ == "__main__":
    main()
