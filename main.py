import pygame
import snake
import food
import menu

# Initializes the pygame environment
pygame.init()

S_WIDTH, S_HEIGHT = 800, 750
WIN = pygame.display.set_mode((S_WIDTH, S_HEIGHT))
pygame.display.set_caption('Snake')

clock = pygame.time.Clock()

score_font = pygame.font.SysFont('comicsans', 40)

player = snake.Snake(250, 250)

snack = food.Food(WIN)

def main():
	# Waiting Screen Loop
	run = True
	while run:
		clock.tick(60)
		for event in pygame.event.get():
			if event.type == pygame.KEYDOWN:
				run = False
			if event.type == pygame.QUIT:
				run = False

		draw_waiting_screen()

	score = 0
	# Game Loop
	run = True
	while run:
		clock.tick(12)

		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				run = False

		# Check collision between snake and walls
		hit = False
		if player.right:
			if player.x + player.vel + player.width > S_WIDTH:
				player.vel = 0
				hit = True
		elif player.left:
			if player.x - player.vel < 0:
				player.vel = 0
				hit = True
		elif player.up:
			if player.y - player.vel < 0:
				player.vel = 0
				hit = True
		elif player.down:
			if player.y + player.vel + player.height > S_HEIGHT:
				player.vel = 0
				hit = True

		if hit:
			print('Game Over.... You hit a wall!')
			run = False

		# Check collision between snake and itself
		for c in player.coords[1:]:
			if player.x == c[0] and player.y == c[1]:
				player.vel = 0
				print('Game Over, You hit yourself')
				run = False

		# Collision between snake and food
		hit = False
		if player.right:
			if player.y == snack.y and player.x + player.width == snack.x:
				hit = True
				player.add_length()
				snack.eaten = True
			elif player.x == snack.x and player.y == snack.y:
				hit = True
				player.add_length()
				snack.eaten = True
		elif player.left:
			if player.y == snack.y and player.x == snack.x + snack.size:
				hit = True
				player.add_length()
				snack.eaten = True
			elif player.x == snack.x and player.y == snack.y:
				hit = True
				player.add_length()
				snack.eaten = True
		elif player.up:
			if player.x == snack.x and player.y - player.height == snack.y:
				hit = True
				player.add_length()
				snack.eaten = True
			elif player.x == snack.x and player.y == snack.y:
				hit = True
				player.add_length()
				snack.eaten = True
		elif player.down:
			if player.x == snack.x and player.y == snack.y - snack.size:
				hit = True
				player.add_length()
				snack.eaten = True
			elif player.x == snack.x and player.y == snack.y:
				hit = True
				player.add_length()
				snack.eaten = True

		if hit:
			score += 1

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

		redraw_window(score)

	pygame.quit()


def redraw_window(score):
	WIN.fill((0, 0, 0))

	text = score_font.render('Score: ' + str(score), 1, (255,255,255))
	WIN.blit(text, (S_WIDTH-text.get_width()-10, 10))

	player.draw(WIN)

	snack.draw(WIN)

	pygame.display.update()

def draw_waiting_screen():
	WIN.fill((0,0,0))
	m = menu.Menu()
	m.draw(WIN)
	pygame.display.update()

if __name__ == '__main__':
	main()
