import os
import pygame
import random
import time

# Grundeinstellungen
class Settings:
    WINDOW_WIDTH = 800
    WINDOW_HEIGHT = 600
    FPS = 60
    FILE_PATH = os.path.dirname(os.path.abspath(__file__))
    IMAGE_PATH = os.path.join(FILE_PATH, "images")

# Spielerklasse
class Player:
    def __init__(self, image_path):
        self.image = pygame.image.load(image_path)
        self.image = pygame.transform.scale(self.image, (40, 40))
        self.width = self.image.get_width()
        self.height = self.image.get_height()
        self.x = Settings.WINDOW_WIDTH // 2
        self.y = Settings.WINDOW_HEIGHT - self.height
        self.speed = 4

    def move(self, keys):
        if keys[pygame.K_LEFT]:
            self.x -= self.speed
        if keys[pygame.K_RIGHT]:
            self.x += self.speed
        self.x = max(0, min(Settings.WINDOW_WIDTH - self.width, self.x))

    def draw(self, screen):
        screen.blit(self.image, (self.x, self.y))

# Hindernisklasse
class MovingObstacle:
    def __init__(self, image_path, x, y, speed_x, size):
        self.image = pygame.image.load(image_path)
        self.image = pygame.transform.scale(self.image, size)
        self.width = self.image.get_width()
        self.height = self.image.get_height()
        self.x = x
        self.y = y
        self.speed_x = speed_x

    def move(self):
        self.x += self.speed_x
        if self.x < -self.width:
            self.x = Settings.WINDOW_WIDTH
        elif self.x > Settings.WINDOW_WIDTH:
            self.x = -self.width

    def draw(self, screen):
        screen.blit(self.image, (self.x, self.y))

# Hauptfunktion
def main():
    pygame.init()
    screen = pygame.display.set_mode((Settings.WINDOW_WIDTH, Settings.WINDOW_HEIGHT))
    clock = pygame.time.Clock()

    # Spieler und Hindernisse
    player = Player(os.path.join(Settings.IMAGE_PATH, "player.png"))
    obstacles = [
        MovingObstacle(os.path.join(Settings.IMAGE_PATH, "car1.png"), 200, 100, -3, (80, 60)),
        MovingObstacle(os.path.join(Settings.IMAGE_PATH, "car2.png"), 400, 200, 3, (100, 80)),
    ]

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        keys = pygame.key.get_pressed()
        player.move(keys)

        screen.fill((0, 0, 0))
        player.draw(screen)

        for obstacle in obstacles:
            obstacle.move()
            obstacle.draw(screen)

        pygame.display.flip()
        clock.tick(Settings.FPS)

    pygame.quit()

if __name__ == "__main__":
    main()
