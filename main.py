import pygame
import snake
import food

# Initializes the pygame environment
pygame.init()

S_WIDTH, S_HEIGHT = 800, 750
WIN = pygame.display.set_mode((S_WIDTH, S_HEIGHT))
pygame.display.set_caption('Snake')

clock = pygame.time.Clock()

player = snake.Snake(250, 250)

snack = food.Food(WIN)

def main():
	# Game Loop
	run = True
	while run:
		clock.tick(12)

		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				run = False

		keys = pygame.key.get_pressed()

		# Up
		if keys[pygame.K_w]:
			player.up = True
			player.down = False
			player.left = False
			player.right = False
		# Left
		elif keys[pygame.K_a]:
			player.up = False
			player.down = False
			player.left = True
			player.right = False
		# Down
		elif keys[pygame.K_s]:
			player.up = False
			player.down = True
			player.left = False
			player.right = False
		# Right
		elif keys[pygame.K_d]:
			player.up = False
			player.down = False
			player.left = False
			player.right = True

		redraw_window()

	pygame.quit()


def redraw_window():
	WIN.fill((0, 0, 0))

	player.draw(WIN)

	snack.draw(WIN)

	pygame.display.update()

if __name__ == '__main__':
	main()
