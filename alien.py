import pygame
from pygame.sprite import Sprite


class Alien(Sprite):
    """Класс представляющий пришельцев."""
    def __init__(self, ai_settings, screen):
        """Создает пришельца и задает начальную позицию."""
        super(Alien, self).__init__()
        self.screen = screen
        self.ai_settings = ai_settings

        # Загрузка изображения пришельца
        self.image = pygame.image.load('images/rocket.png')
        self.rect = self.image.get_rect()

        # Координаты пришельцев.
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # Сохранение точной позиции пришельца.
        self.x = float(self.rect.x)

    def check_edges(self):
        """ Возвращает True, если пришелец находится на краю экрана."""
        screen_rect = self.screen.get_rect()
        if self.rect.right >=screen_rect.right:
            return True
        elif self.rect.left <= 0:
            return True

    def update(self):
        """ Перемещает пришельца вправо."""
        self.x += self.ai_settings.alien_speed_factor * self.ai_settings.fleet_direction
        self.rect.x = self.x

    def blitme(self):
        """ Вывходит пришельцев в текущем положении."""
        self.screen.blit(self.image, self.rect)
