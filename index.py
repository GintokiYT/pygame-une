import pygame, sys

pygame.init()

# Define colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

# Define window size
size = (800, 500)

# Create a window
screen = pygame.display.set_mode(size)

# Controls FPS
clock = pygame.time.Clock()

# Cords for position
cord_x = 400
cord_y = 200

# Speed for object
speed_x = 3
speed_y = 3

while True: 
  for event in pygame.event.get():
    print(event)
    if event.type == pygame.QUIT:
      sys.exit()
  
  if(cord_x > 720 or cord_x < 0):
    speed_x *= -1 
  if(cord_y > 420 or cord_y < 0):
    speed_y *= -1 

  cord_x += speed_x
  cord_y += speed_y
  # Background
  screen.fill(WHITE)
  # Zone drawing
  pygame.draw.rect(screen, RED, (cord_x, cord_y, 80, 80))
  # Update window
  pygame.display.flip()
  clock.tick(60)