import pygame
import random

class Food(object):
	def __init__(self, window):
		self.size = 25
		self.eaten = False
		self.x, self.y = self.get_coords(window)
		
	def get_coords(self, window):
		uneven = True
		while uneven:
			x = random.randint(0, window.get_width()-self.size)
			y = random.randint(0, window.get_height()-self.size)

			if x % self.size == 0 and y % self.size == 0:
				uneven = False
		
		return x, y

	def draw(self, window):
		if self.eaten:
			self.x, self.y = self.get_coords(window)
			self.eaten = False

		pygame.draw.rect(window, (0,255,0), (self.x, self.y, self.size, self.size))
