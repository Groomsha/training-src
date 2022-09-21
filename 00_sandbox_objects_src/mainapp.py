"""
Project Name: 'mini-games'
Version: 0.1

Description: Mini Games App

Ihor Cheberiak (c) 2021
https://www.linkedin.com/in/ihor-cheberiak/
"""

from typing import Optional

import alien_invasion


class MainGames:
	def __init__(self) -> None:
		self.game: Optional = None

		self.alien_invasion()

	def alien_invasion(self) -> None:
		print("Start Game: Alien Invasion")
		self.game = alien_invasion.AlienInvasionMain()
		self.game.run_game()


if __name__ == '__main__':
	main_games_switch = MainGames()
