import pygame
import random
import sys

# Initialize Pygame
pygame.init()

# Screen dimensions
WIDTH = 800
HEIGHT = 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))

# Colors
WHITE = (255, 255, 255)
RED = (200, 0, 0)
BLUE = (0, 100, 255)
BLACK = (0, 0, 0)

# Player settings
player_size = 50
player_pos = [WIDTH // 2, HEIGHT - 2 * player_size]

# Enemy settings
enemy_size = 50
enemy_pos = [random.randint(0, WIDTH - enemy_size), 0]
enemy_list = [enemy_pos]
SPEED = 10

score = 0
clock = pygame.time.Clock()
game_over = False

def draw_enemies(enemies):
    for en_pos in enemies:
        pygame.draw.rect(screen, RED, (en_pos[0], en_pos[1], enemy_size, enemy_size))

def update_enemy_positions(enemies, score):
    for idx, en_pos in enumerate(enemies):
        if en_pos[1] >= 0 and en_pos[1] < HEIGHT:
            en_pos[1] += SPEED
        else:
            enemies.pop(idx)
            score += 1
    return score

def collision_check(enemies, p_pos):
    for en_pos in enemies:
        if (en_pos[0] < p_pos[0] < en_pos[0] + enemy_size or p_pos[0] < en_pos[0] < p_pos[0] + player_size) and \
           (en_pos[1] < p_pos[1] < en_pos[1] + enemy_size or p_pos[1] < en_pos[1] < p_pos[1] + player_size):
            return True
    return False

# Main Game Loop
while not game_over:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

    # Movement Logic
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and player_pos[0] > 0:
        player_pos[0] -= 10
    if keys[pygame.K_RIGHT] and player_pos[0] < WIDTH - player_size:
        player_pos[0] += 10

    screen.fill(BLACK)

    # Drop enemies
    if len(enemy_list) < 10 and random.random() < 0.1:
        x_pos = random.randint(0, WIDTH - enemy_size)
        enemy_list.append([x_pos, 0])

    score = update_enemy_positions(enemy_list, score)
    
    if collision_check(enemy_list, player_pos):
        game_over = True
        break

    draw_enemies(enemy_list)
    pygame.draw.rect(screen, BLUE, (player_pos[0], player_pos[1], player_size, player_size))

    clock.tick(30)
    pygame.display.update()

print(f"Game Over! Final Score: {score}")