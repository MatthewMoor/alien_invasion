import pygame
from settings import Settings


class Ship():
	
	def __init__(self, screen):
		"""Инициализирует корабль и задает его начальную позицию. """
		self.screen = screen
		self.ai_settings = Settings()
		
		# Загрузка изображения корабля
		self.image = pygame.image.load('images/rocket_man.png')
		self.rect = self.image.get_rect()
		self.screen_rect = screen.get_rect()
		# Каждый новый корабль появляется у нижнего края экрана
		self.rect.centerx = self.screen_rect.centerx
		self.rect.centery = self.screen_rect.centery
		self.rect.bottom = self.screen_rect.bottom
		self.moving_right = False
		self.moving_left = False
		self.moving_up = False
		self.moving_down = False
		# Сохранение вещественной координаты центра корабля.
		self.center = float(self.rect.centerx)
		self.center_y = float(self.rect.centery)
		
	def update(self):
		"""Обновляет позиции корабля с учетом флага"""
		if self.moving_right and self.rect.right < self.screen_rect.right:
			self.center += self.ai_settings.ship_speed_factor
		if self.moving_left and self.rect.left > 0:
			self.center -= self.ai_settings.ship_speed_factor
		if self.moving_up:
			self.center_y -= self.ai_settings.ship_speed_factor
		if self.moving_down:
			self.center_y += self.ai_settings.ship_speed_factor
		# Обновление атрибута rect на основании self.center.
		self.rect.centerx = self.center
		self.rect.centery = self.center_y
		
	def blitme(self):
		"""Рисует корабль текущей позиции.  """
		self.screen.blit(self.image, self.rect)
