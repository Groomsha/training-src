"""
Project Name: 'mini-games'
Version: 0.1

Description: Alien Invasion (2D Game)

Ihor Cheberiak (c) 2021
https://www.linkedin.com/in/ihor-cheberiak/
"""

import sys

import pygame

import alien_invasion as game


class AlienInvasionMain:
	""""Main Game Class"""

	def __init__(self) -> None:
		pygame.init()

		self.settings_game = game.SettingsGame()
		self.settings_images = game.SettingsImages()

		pygame.display.set_caption("Alien Invasion")
		self.screen = pygame.display.set_mode((self.settings_game.display_width, self.settings_game.display_height))

		self.ship = game.StarShip(self)

	def run_game(self) -> None:
		while True:
			for event in pygame.event.get():
				if event.type == pygame.KEYDOWN:
					self._event_game_keydown(event)

				if event.type == pygame.KEYUP:
					self._event_game_keyup(event)

				self._game_exit(event)

			self.ship.update_moving_ship()
			self._update_display()

	def _event_game_keydown(self, event) -> None:
		if event.key == pygame.K_UP:
			self.ship.ship_moving_UP = True
		elif event.key == pygame.K_DOWN:
			self.ship.ship_moving_DOWN = True
		elif event.key == pygame.K_RIGHT:
			self.ship.ship_moving_RIGHT = True
		elif event.key == pygame.K_LEFT:
			self.ship.ship_moving_LEFT = True

	def _event_game_keyup(self, event) -> None:
		if event.key == pygame.K_UP:
			self.ship.ship_moving_UP = False
		elif event.key == pygame.K_DOWN:
			self.ship.ship_moving_DOWN = False
		elif event.key == pygame.K_RIGHT:
			self.ship.ship_moving_RIGHT = False
		elif event.key == pygame.K_LEFT:
			self.ship.ship_moving_LEFT = False

	def _update_display(self) -> None:
		self.screen.fill(self.settings_game.display_background)
		self.ship.creation_ship()

		pygame.display.flip()

	def _game_exit(self, event) -> None:
		if event.type == pygame.QUIT:
			sys.exit()
		elif event.type == pygame.KEYDOWN:
			if event.key == pygame.K_q:
				sys.exit()
