import pygame

class Snake(object):
	def __init__(self, x, y, length=2):
		self.x = x
		self.y = y
		self.length = length
		self.right = True
		self.left = False
		self.up = False
		self.down = False
		self.width = 25
		self.height = 25
		self.coords = [(self.x, self.y), (self.x-self.width, self.y)]
		self.vel = self.width

	def draw(self, window):
		new_coords = []

		if self.right:
			new_coords.append((self.coords[0][0] + self.vel, self.coords[0][1]))

		elif self.left:
			new_coords.append((self.coords[0][0] - self.vel, self.coords[0][1]))

		elif self.up:
			new_coords.append((self.coords[0][0], self.coords[0][1] - self.vel))

		elif self.down:
			new_coords.append((self.coords[0][0], self.coords[0][1] + self.vel))

		for i in range(1, len(self.coords)):
			new_coords.append((self.coords[i-1][0], self.coords[i-1][1]))

		self.coords = new_coords

		for point in self.coords:
			pygame.draw.rect(window, (255,0,0), (point[0], point[1], self.width, self.height), 2)

		self.x = self.coords[0][0]
		self.y = self.coords[0][1]



	def add_length(self):
		pass