import pygame, sys

pygame.init()

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)

size = (800, 500)
screen = pygame.display.set_mode(size)
clock = pygame.time.Clock()

coord_x = 0
coord_y = 0

x_speed = 0
y_speed = 0

while True:
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      sys.exit()
    # Events keyboard
    if event.type == pygame.KEYDOWN:
      if event.key == pygame.K_LEFT:
        x_speed -= 5
      if event.key == pygame.K_RIGHT:
        x_speed += 5
      if event.key == pygame.K_UP:
        y_speed -= 5
      if event.key == pygame.K_DOWN:
        y_speed += 5
    if event.type == pygame.KEYUP:
      if event.key == pygame.K_LEFT:
        x_speed = 0
      if event.key == pygame.K_RIGHT:
        x_speed = 0
      if event.key == pygame.K_UP:
        y_speed = 0
      if event.key == pygame.K_DOWN:
        y_speed = 0

  # Background
  screen.fill(WHITE)

  coord_x += x_speed
  if coord_x > 700:
    coord_x -= 5
  if coord_x < 0:
    coord_x += 5

  coord_y += y_speed
  if coord_y > 400:
    coord_y -= 5
  if coord_y < 0:
    coord_y += 5

  pygame.draw.rect(screen, RED, (coord_x, coord_y, 100, 100))

  pygame.display.flip()
  clock.tick(60)  



