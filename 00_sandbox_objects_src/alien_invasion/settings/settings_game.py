"""
Project Name: 'mini-games'
Version: 0.1

Description: Alien Invasion (2D Game)

Ihor Cheberiak (c) 2021
https://www.linkedin.com/in/ihor-cheberiak/
"""

from typing import Tuple


class SettingsGame:
	def __init__(self) -> None:
		# PyGame Display Settings
		self.display_width: int = 1200
		self.display_height: int = 800
		self.display_background: Tuple = (230, 230, 230)

		# PyGame Ship Settings
		self.ship_moving_speed: float = 1.5
