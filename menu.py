import pygame

class Menu(object):
	def __init__(self):
		self.font = pygame.font.SysFont('comicsans', 80)

	def draw(self, window):
		text = self.font.render('Press any key to begin...', 1, (255,130,255))
		window.blit(text, (window.get_width()-text.get_width()-70, 250))