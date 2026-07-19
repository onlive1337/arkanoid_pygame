import pygame
from settings import *

def main():
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Arkanoid")
    clock = pygame.time.Clock()

    running = True
    while running:
        # Обработка событий
        for event in pygame.event.get():
            if event.type == pygame.QUIT:   # нажатие на крестик
                running = False

        # Заливка фона (пока чёрный)
        screen.fill(BLACK)

        # Здесь будет отрисовка объектов

        pygame.display.flip()   # обновление экрана
        clock.tick(FPS)         # ограничение FPS

    pygame.quit()

if __name__ == "__main__":
    main()