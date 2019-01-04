import pygame

from pygame.sprite import Group
from settings import Settings
from ship import Ship
from game_stats import GameStats
from button import Button
import game_functions as gf


def run_game():
	# Инициализирует pygame, settings и объект экрана.
	pygame.init()
	pygame.display.set_caption("Alien Invasion")
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
	# Экземпляр для хранения игровой статистики.
	stats = GameStats(ai_settings)
	# Создание кнопки Play.
	play_button = Button(ai_settings, screen, 'Play')
	
	# Запуск основного цикла игры.
	while True:
		# Отслеживает событие клавиатуры и мыши.
		gf.check_events(ai_settings, screen, stats, play_button, ship, aliens, bullets)
		if stats.game_active:
			ship.update()
			gf.update_bullets(ai_settings, screen, ship, aliens, bullets)
			gf.update_aliens(ai_settings, stats, screen, ship, aliens, bullets)
			gf.update_screen(ai_settings, screen, stats, ship, aliens, bullets, play_button)
			rel_y = bcgd_y % bcgd.get_rect().height
			screen.blit(bcgd, (0, rel_y - bcgd.get_rect().height))
			if rel_y < ai_settings.screen_width:
				screen.blit(bcgd, (0, rel_y))
			bcgd_y += 3


run_game()
