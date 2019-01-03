class Settings():
	"""Класс для хранения всех настроек игры Alien Invasion."""
	
	def __init__(self):
		""" Инициализирует настройки игры Alien Invasion."""
		# Параметры экрана
		self.screen_width = 1200
		self.screen_height = 800
		self.bg_color = ()
		self.ship_speed_factor = 1.7
		self.ship_limit = 3
		self.alien_speed_factor = 2.7
		# Параметры пули
		self.bullet_speed_factor = 4
		self.bullet_width = 5
		self.bullet_height = 25
		self.bullet_color = 250, 0, 150
		self.bullets_allowed = 6
		# Управление скоростью пришельца так сказатб.
		self.fleet_drop_speed = 10
		self.fleet_direction = 1


