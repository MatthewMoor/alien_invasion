import pygame

from pygame.sprite import Group
from settings import Settings
from ship import Ship
import game_functions as gf


def run_game():
	# Инициализирует pygame, settings и объект экрана.
	pygame.init()
	ai_settings = Settings()
	screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
	pygame.display.set_caption("Alien Invasion")
	ship = Ship(screen)
	# Хранение пуль
	bullets = Group()
	aliens = Group()
	bcgd = pygame.image.load('images/back.jpg').convert()
	bcgd_y = 0
	gf.create_fleet(ai_settings, screen, ship, aliens)
	
	# Запуск основного цикла игры.
	while True:
		# Отслеживает событие клавиатуры и мыши.
		gf.check_events(ai_settings, screen, ship, bullets)
		ship.update()
		gf.update_bullets(bullets)
		gf.update_aliens(ai_settings, aliens)
		gf.update_screen(ai_settings, screen, ship, aliens, bullets)
		rel_y = bcgd_y % bcgd.get_rect().height
		screen.blit(bcgd, (0, rel_y - bcgd.get_rect().height))
		if rel_y < ai_settings.screen_width:
			screen.blit(bcgd, (0, rel_y))
		bcgd_y += 3


run_game()
