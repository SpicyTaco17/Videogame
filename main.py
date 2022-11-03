# Sources:
# Reference for overall game creation: https://coderslegacy.com/python/python-pygame-tutorial/
# How to set font: https://www.folkstalk.com/2022/10/how-to-write-a-font-in-pygame-with-code-examples.html#:~:text=How%20do%20you%20initialize%20a%20font%3F%201%20initialize,color.%20text%20%3D%20font.render%20%28%E2%80%9CStart%20game%E2%80%9D%2C%20True%2C%20%28255%2C255%2C255%29
# Moving a sprite: https://pythonprogramming.altervista.org/pygame-3-move-sprite/#:~:text=Moving%20a%20sprite%20with%20arrow%20keys%201%20import,4%20create%20the%20loop%20to%20move%20the%20sprite
# Using images: https://www.geeksforgeeks.org/python-display-images-with-pygame/

# Importing all libraries / modules
import pygame as pg
import sys
from pygame.locals import *
import random, time
 
# Initializing the game
pg.init()
 
# Setting fps for game
FPS = 60
FramePerSec = pg.time.Clock()

# Defining color values
BLUE  = (0, 0, 255)
RED   = (255, 0, 0)
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
 
# Defining variables for game dimensions and player / sprite attributes
SCREEN_WIDTH = 600
SCREEN_HEIGHT = 600
SPEED = 5
SCORE = 0
HEALTH = 100000
 
# Creating different fonts and texts
font = pg.font.SysFont("Verdana", 60)
font_small = pg.font.SysFont("Verdana", 20)
font_xs = pg.font.SysFont("Verdana", 11)
game_over = font.render("Game Over", True, BLACK)
difficulty = font_xs.render("Increasing Difficulty", True, RED)
value = font_small.render("Your health is at: " + str(HEALTH), True, RED)

# Variable for background street image
background = pg.image.load("road.jpg")

# Displaying white screen with caption set to: Game
DISPLAY = pg.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
DISPLAY.fill(WHITE)
pg.display.set_caption("Game")

# First enemy class
class Enemy1(pg.sprite.Sprite):
    def __init__(self):
        super().__init__()
        # Using image of car facing upwards
        self.image = pg.image.load("car_up.png")
        self.rect = self.image.get_rect()
        # Car is allowed to move vertically at 900 and horizontally from any coordinate between 1085 and 1170
        self.rect.center = (random.randint(1085, 1170), 900)  
 
    def move(self):
        global SCORE
        # Moves downwards at set speed
        self.rect.move_ip(0, SPEED)
        if (self.rect.top > 600):
            # Increases score
            SCORE += 1
            # Returns car back to starting coordinates once passing boundary
            self.rect.center = (random.randint(1085, 1170), 900)

# Second enemy class
class Enemy2(pg.sprite.Sprite):
    def __init__(self):
        super().__init__()
        # Reusing image of car facing upwards although traveling in the opposite direction
        self.image = pg.image.load("car_up.png")
        self.rect = self.image.get_rect()
        # Car is allowed to move vertically at 1900 and horizontally from any coordinate between 1085 and 1170
        self.rect.center = (random.randint(1085, 1170), 1900)
 
    def move(self):
        global SCORE
        self.rect.move_ip(0, -SPEED)
        if (self.rect.top < -30):
            # Increases score
            SCORE += 1
            # Returns car back to starting coordinates once passing boundary
            self.rect.center = (random.randint(1085, 1170), 1900)

# Third enemy class
class Enemy3(pg.sprite.Sprite):
    def __init__(self):
        super().__init__()
        # Using image of car facing to the right
        self.image = pg.image.load("car_right.png")
        self.rect = self.image.get_rect()
        # Car is allowed to move horizontally at 500 and vertically from any coordinate between 570 and 650
        self.rect.center = (500, random.randint(570, 650))  
 
    def move(self):
        global SCORE
        self.rect.move_ip(SPEED, 0)
        if (self.rect.right > 2200):
            # Increases score
            SCORE += 1
            # Returns car back to starting coordinates once passing boundary
            self.rect.center = (500, random.randint(570, 650))

# Fourth enemy class
class Enemy4(pg.sprite.Sprite):
    def __init__(self):
        super().__init__()
        # Using image of car facing to the left
        self.image = pg.image.load("car_left.png")
        self.rect = self.image.get_rect()
        # Car is allowed to move horizontally at 500 and vertically from any coordinate between 440 and 530
        self.rect.center = (800, random.randint(440, 530))  
 
    def move(self):
        global SCORE
        self.rect.move_ip(-SPEED, 0)
        if (self.rect.right < 500):
            # Increases score
            SCORE += 1
            # Returns car back to starting coordinates once passing boundary
            self.rect.center = (1000, random.randint(440, 530))

# Player class
class Player(pg.sprite.Sprite):
    def __init__(self):
        super().__init__()
        # I created an image of a circle in Adobe Illustrator as the player sprite
        self.image = pg.image.load("ball.png")
        self.rect = self.image.get_rect()
        # Places sprite at the center of the screen
        self.rect.center = (290, 930)
        
    def move(self):
        pressed_keys = pg.key.get_pressed()
        # Can move up if y value is greater than 0
        if self.rect.y > 0:
            # If up arrow key pressed
            if pressed_keys[K_UP] or pressed_keys[K_w]:
                # Can't move up if in these x or y value boundaries
                if self.rect.y < 250 and self.rect.x < 240:
                    pass
                # Can't move up if in these x or y value boundaries
                elif self.rect.y < 250 and self.rect.x > 320:
                    pass
                # If all requirements met, move up
                else:
                    self.rect.move_ip(0, -5)
        # Can move down if y value is less than 560
        if self.rect.y < 560:
            # If down arrow key pressed
            if pressed_keys[K_DOWN] or pressed_keys[K_s]:
                # Can't move down if in these x or y value boundaries
                if self.rect.y > 320 and self.rect.x < 240:
                    pass
                # Can't move down if in these x or y value boundaries
                elif self.rect.y > 320 and self.rect.x > 320:
                    pass
                # If all requirements met, move down
                else:
                    self.rect.move_ip(0,5)
        # Can move left if x value is greater than 0
        if self.rect.x > 0:
            # If left arrow key pressed
            if pressed_keys[K_LEFT] or pressed_keys[K_a]:
                # Can't move left if in these x or y value boundaries
                if self.rect.y < 240 and self.rect.x < 245:
                    pass
                # Can't move left if in these x or y value boundaries
                elif self.rect.y > 330 and self.rect.x < 245:
                    pass
                # If all requirements met, move left
                else:
                    self.rect.move_ip(-5, 0)
        # Can move right if x value is less than 560
        if self.rect.x < 560:
            # If right arrow key pressed
            if pressed_keys[K_RIGHT] or pressed_keys[K_d]:
                # Can't move right if in these x or y value boundaries
                if self.rect.y < 240 and self.rect.x > 310:
                    pass
                # Can't move right if in these x or y value boundaries
                elif self.rect.y > 330 and self.rect.x > 310:
                    pass
                # If all requirements met, move right
                else:
                    self.rect.move_ip(5, 0)
                   
# Assign sprites to variables       
P1 = Player()
E1 = Enemy1()
E2 = Enemy2()
E3 = Enemy3()
E4 = Enemy4()
 
# Assign enemy sprites to group
enemies = pg.sprite.Group()
enemies.add(E1)
enemies.add(E2)
enemies.add(E3)
enemies.add(E4)
# Assign all sprites to group
all_sprites = pg.sprite.Group()
all_sprites.add(P1)
all_sprites.add(E1)
all_sprites.add(E2)
all_sprites.add(E3)
all_sprites.add(E4)
 
# Game loop
while True:
       
    # Loops through all occuring events 
    for event in pg.event.get():
        if event.type == QUIT:
            pg.quit()
            sys.exit()
    # Display background at these coordinates
    DISPLAY.blit(background, (0, 0))
    # Display score
    scores = font_small.render(str(SCORE), True, BLACK)
    # If the score is divisible by 5 (excluding 0)
    if SCORE % 5 == 0 and SCORE != 0:
        # Display both the score as red and the difficulty increasing message
        scores = font_small.render(str(SCORE), True, RED)
        DISPLAY.blit(difficulty, (250, 10))
        # Increase the speed of the cars
        SPEED += 0.01
    # Display scores in top left
    DISPLAY.blit(scores, (10, 10))
    # Display health value towards middle of screen
    DISPLAY.blit(value, (250, 250))

    # In the case of all sprites
    for entity in all_sprites:
        # Alter size to scale
        img = pg.transform.scale(entity.image, (50, 40))
        DISPLAY.blit(img, entity.rect)
        # Move all entities
        entity.move()
 
    # If collision occurs between the player and an enemy
    if pg.sprite.spritecollideany(P1, enemies):
        # Decrease the health
        HEALTH -= 10

    # If the health of the player is at its lowest
    if HEALTH <= 0:
        # Fill the screen red and display "game over"
        DISPLAY.fill(RED)
        DISPLAY.blit(game_over, (30,250))
        # Update all sprites by removeing them   
        pg.display.update()
        for entity in all_sprites:
            entity.kill()
        # Wait for 2 seconds
        time.sleep(2)
        # Quit / exit the game
        pg.quit()
        sys.exit()        
    # Update display and run game at set FPS 
    pg.display.update()
    FramePerSec.tick(FPS)
