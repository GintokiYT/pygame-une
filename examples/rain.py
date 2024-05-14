import pygame, sys, random

pygame.init()

WHITE = (255, 255, 255)
RED = (255, 0, 0)

size = (800, 500)
screen = pygame.display.set_mode(size)
clock = pygame.time.Clock()

cord_list = []
for i in range(60):
  x = random.randint(0, 800)
  y = random.randint(0, 500)
  cord_list.append([x, y])

while True: 
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      sys.exit()  

  # Background  
  screen.fill(WHITE)

  for coord in cord_list:
    x = coord[0]
    y = coord[1]
    pygame.draw.circle(screen, RED, (x, y), 2)
    coord[1] += 1
    if coord[1] > 500:
      coord[1] = 0
  
  pygame.display.flip()
  clock.tick(30)