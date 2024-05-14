import pygame

pygame.init()

screen_width = 720
screen_height = 405

screen = pygame.display.set_mode([screen_width, screen_height])
clock = pygame.time.Clock()

status = False

background = pygame.image.load("./src/assets/img/word.png").convert()
original_player_image = pygame.image.load("./src/assets/img/mario.png").convert_alpha()

# Rotar la imagen original para que el jugador mire hacia la derecha por defecto
player_image = original_player_image
player_angle = 0

# Obstaculos
box1 = pygame.image.load("./src/assets/img/box.png").convert()
box2 = pygame.image.load("./src/assets/img/box.png").convert()
box3 = pygame.image.load("./src/assets/img/box.png").convert()

# Posiciones de los obstáculos
box1_rect = box1.get_rect()
box1_rect.topleft = (48, 261)

box2_rect = box2.get_rect()
box2_rect.topleft = (456, 165)

box3_rect = box3.get_rect()
box3_rect.topleft = (480, 165)

# Crear fuente para el mensaje de colisión
collision_font = pygame.font.Font(None, 36)

# Posición y velocidad inicial del jugador
player_x = 25
player_y = screen_height - 50  # Aparece 50 píxeles más arriba del suelo
player_vel_x = 0
player_vel_y = 0
gravity = 0.5
jump_force = -10
player_rect = original_player_image.get_rect()
can_jump = True  # Variable para rastrear si el jugador puede saltar
on_ground = False  # Variable para rastrear si el jugador está en el suelo
collision_with_obstacle = False  # Variable para rastrear si el jugador colisiona con un obstáculo

move = 2.5  # Variable de movimiento

while not status:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            status = True

        # Manejar eventos de teclado
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                player_vel_x = move
                player_image = original_player_image
                player_angle = 0
            elif event.key == pygame.K_LEFT:
                player_vel_x = -move
                player_image = pygame.transform.flip(original_player_image, True, False)
                player_angle = 0
            elif event.key == pygame.K_SPACE and can_jump and on_ground:
                player_vel_y = jump_force
                can_jump = False  # Desactivar la capacidad de saltar
                on_ground = False  # El jugador ya no está en el suelo
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT and player_vel_x > 0:
                player_vel_x = 0
            elif event.key == pygame.K_LEFT and player_vel_x < 0:
                player_vel_x = 0

    # Aplicar gravedad al jugador
    player_vel_y += gravity
    player_x += player_vel_x

    # Evitar que el jugador salga de la pantalla horizontalmente
    if player_x < 0:
        player_x = 0
    elif player_x > screen_width - player_rect.width:
        player_x = screen_width - player_rect.width

    # Aplicar movimiento vertical al jugador
    player_y += player_vel_y

    # Evitar que el jugador salga de la pantalla verticalmente
    if player_y > screen_height - player_rect.height - 50:  # Limitar la caída a 50 píxeles por encima del suelo
        player_y = screen_height - player_rect.height - 50
        player_vel_y = 0
        can_jump = True  # Restablecer la capacidad de saltar una vez que el jugador toca el suelo
        on_ground = True  # El jugador está de vuelta en el suelo

    # Verificar y corregir colisiones con los obstáculos
    if player_rect.colliderect(box1_rect):
        if player_vel_x > 0:
            player_x = min(player_x, box1_rect.left - player_rect.width)
        elif player_vel_x < 0:
            player_x = max(player_x, box1_rect.right)
        collision_with_obstacle = True
    elif player_rect.colliderect(box2_rect):
        if player_vel_x > 0:
            player_x = min(player_x, box2_rect.left - player_rect.width)
        elif player_vel_x < 0:
            player_x = max(player_x, box2_rect.right)
        collision_with_obstacle = True
    elif player_rect.colliderect(box3_rect):
        if player_vel_x > 0:
            player_x = min(player_x, box3_rect.left - player_rect.width)
        elif player_vel_x < 0:
            player_x = max(player_x, box3_rect.right)
        collision_with_obstacle = True
    else:
        collision_with_obstacle = False

    # Actualizar el rectángulo de colisión del jugador
    player_rect.topleft = (player_x, player_y)

    # Dibujar elementos en la pantalla  
    screen.blit(background, [0, 0])
    rotated_player_image = pygame.transform.rotate(player_image, player_angle)
    rotated_rect = rotated_player_image.get_rect(center=player_rect.center)
    screen.blit(rotated_player_image, rotated_rect.topleft)
    screen.blit(box1, box1_rect)
    screen.blit(box2, box2_rect)
    screen.blit(box3, box3_rect)

    # Verificar colisiones y mostrar el mensaje de colisión si es necesario
    if collision_with_obstacle:
        collision_message = collision_font.render("¡Colisión!", True, (255, 0, 0))
        screen.blit(collision_message, (300, 50))
        # Detener el movimiento vertical del jugador después de la colisión
        player_vel_y = 0

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
