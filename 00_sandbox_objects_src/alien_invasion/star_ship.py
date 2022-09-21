"""
Project Name: 'mini-games'
Version: 0.1

Description: Alien Invasion (2D Game)

Ihor Cheberiak (c) 2021
https://www.linkedin.com/in/ihor-cheberiak/
"""

import pygame


class StarShip:
	def __init__(self, ai_game) -> None:
		self.screen = ai_game.screen
		self.screen_rect = ai_game.screen.get_rect()

		self.settings_game = ai_game.settings_game
		self.settings_images = ai_game.settings_images

		self.image_ship = pygame.image.load(self.settings_images.ship_image)
		self.ship_rect = self.image_ship.get_rect()
		self.ship_rect.midbottom = self.screen_rect.midbottom

		self.ship_moving_UP: bool  = False
		self.ship_moving_DOWN: bool = False
		self.ship_moving_RIGHT: bool = False
		self.ship_moving_LEFT: bool = False

		self.speed_X: float = float(self.ship_rect.x)
		self.speed_Y: float = float(self.ship_rect.y)

	def creation_ship(self) -> None:
		self.screen.blit(self.image_ship, self.ship_rect)

	def update_moving_ship(self) -> None:
		if self.ship_moving_UP:
			self.speed_Y -= self.settings_game.ship_moving_speed
		if self.ship_moving_DOWN:
			self.speed_Y += self.settings_game.ship_moving_speed
		if self.ship_moving_RIGHT:
			self.speed_X += self.settings_game.ship_moving_speed
		if self.ship_moving_LEFT:
			self.speed_X -= self.settings_game.ship_moving_speed

		self.ship_rect.x = self.speed_X
		self.ship_rect.y = self.speed_Y
