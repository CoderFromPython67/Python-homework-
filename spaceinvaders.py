import pygame
import math
import random

# Constants
SCREEN_WIDTH = 1920
SCREEN_HEIGHT = 1080

PLAYER_START_X = 370
PLAYER_START_Y = 480

ENEMY_START_Y_MIN = 50
ENEMY_START_Y_MAX = 150

ENEMY_X_SPEED = 4
ENEMY_Y_SPEED = 40

BULLET_SPEED = 10
COLLISION_DISTANCE = 27

pygame.init()

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Space Invader")

background = pygame.image.load("bg.jpg")
background = pygame.transform.scale(background, (SCREEN_WIDTH, SCREEN_HEIGHT))

icon = pygame.image.load("enemy.png")
pygame.display.set_icon(icon)

# Player
playerIMG = pygame.image.load("player.WEBP")
playerX = PLAYER_START_X
playerY = PLAYER_START_Y
playerX_CHANGE = 0

# Enemy
enemyIMG = []
enemyX = []
enemyY = []
enemyX_CHANGE = []
enemyY_CHANGE = []

num_of_enemies = 8

for i in range(num_of_enemies):
    enemyIMG.append(pygame.image.load("enemy.png"))
    enemyX.append(random.randint(0, SCREEN_WIDTH - 64))
    enemyY.append(random.randint(ENEMY_START_Y_MIN, ENEMY_START_Y_MAX))
    enemyX_CHANGE.append(ENEMY_X_SPEED)
    enemyY_CHANGE.append(ENEMY_Y_SPEED)

# Bullet
bulletIMG = pygame.image.load("bullet.png")
bulletX = 0
bulletY = playerY
bulletY_CHANGE = BULLET_SPEED
bullet_state = "ready"

# Score
score_value = 0
font = pygame.font.Font("freesansbold.ttf", 32)
textX = 10
textY = 10

over_font = pygame.font.Font("freesansbold.ttf", 64)


def show_score(x, y):
    score = font.render("Score : " + str(score_value), True, (255, 255, 255))
    screen.blit(score, (x, y))


def game_over_text():
    over_text = over_font.render("GAME OVER", True, (255, 255, 255))
    screen.blit(over_text, (550, 400))


def player(x, y):
    screen.blit(playerIMG, (x, y))


def enemy(x, y, i):
    screen.blit(enemyIMG[i], (x, y))


def fire_bullet(x, y):
    global bullet_state
    bullet_state = "fire"
    screen.blit(bulletIMG, (x + 16, y + 10))


def isCollision(enemyX, enemyY, bulletX, bulletY):
    distance = math.sqrt((enemyX - bulletX) ** 2 + (enemyY - bulletY) ** 2)
    return distance < COLLISION_DISTANCE


running = True
game_over = False

while running:

    screen.fill((0, 0, 0))
    screen.blit(background, (0, 0))

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:

            if event.key == pygame.K_LEFT:
                playerX_CHANGE = -5

            if event.key == pygame.K_RIGHT:
                playerX_CHANGE = 5

            if event.key == pygame.K_SPACE:
                if bullet_state == "ready":
                    bulletX = playerX
                    bulletY = playerY
                    fire_bullet(bulletX, bulletY)

        if event.type == pygame.KEYUP:

            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                playerX_CHANGE = 0

    # Player movement
    playerX += playerX_CHANGE

    if playerX < 0:
        playerX = 0

    if playerX > SCREEN_WIDTH - 64:
        playerX = SCREEN_WIDTH - 64

    # Enemy movement
    for i in range(num_of_enemies):

        if enemyY[i] > 440:
            game_over = True
            for j in range(num_of_enemies):
                enemyY[j] = 2000
            break

        enemyX[i] += enemyX_CHANGE[i]

        if enemyX[i] <= 0:
            enemyX_CHANGE[i] = ENEMY_X_SPEED
            enemyY[i] += enemyY_CHANGE[i]

        elif enemyX[i] >= SCREEN_WIDTH - 64:
            enemyX_CHANGE[i] = -ENEMY_X_SPEED
            enemyY[i] += enemyY_CHANGE[i]

        # Collision
        if isCollision(enemyX[i], enemyY[i], bulletX, bulletY):
            bulletY = playerY
            bullet_state = "ready"

            score_value += 1

            enemyX[i] = random.randint(0, SCREEN_WIDTH - 64)
            enemyY[i] = random.randint(ENEMY_START_Y_MIN, ENEMY_START_Y_MAX)

        enemy(enemyX[i], enemyY[i], i)

    # Bullet movement
    if bullet_state == "fire":
        fire_bullet(bulletX, bulletY)
        bulletY -= bulletY_CHANGE

    if bulletY <= 0:
        bulletY = playerY
        bullet_state = "ready"

    player(playerX, playerY)

    show_score(textX, textY)

    if game_over:
        game_over_text()

    pygame.display.update()

pygame.quit()