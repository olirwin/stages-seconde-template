## RUBIKA - SNAKE GAME

#### IMPORTS ####
import pygame
import random

#### COLOUR DEFINITION ####

white  = (255, 255, 255)
yellow = (255, 255, 102)
black  = (0, 0, 0)
red    = (213, 50, 80)
green  = (0, 255, 0)
blue   = (50, 153, 213)

# Step 1: Defining the window's graphical variables

# Step 2.3: Showing a square in the window
def draw_square(x: int, y: int, colour: tuple):
    pygame.draw.rect()

# Step 4: Showing multiple squares from a list of positions and a colour

# Step 3.1: Get a random number between 0 and max (excluded)

# Step 3.2: Get random coordinates in the zone

# Print a message at the top left of the screen in Comic Sans MS, size 20
def print_message(message: str) :
    console.blit(pygame.font.SysFont("comicsansms", 20).render(message, True, white), [0, 0])

# Step 7: Direction according to the pressed key

# Step 9: Getting the new position in the current direction

# Step 10: Checking is the position is in the game area

# One game turn
def game_turn(snake, end, direction, food):
    # Step 6.1: Show the food

    # Step 6.2: Show the score

    # Step 6.3: Show the snake

    # Update display
    pygame.display.update()

    # Retrieve pressed keys
    for event in pygame.event.get():
        # Step 8.1: × is pressed, exit the game

        # Step 8.2: a key is pressed, update direction
        print(event)

    # Step 11: If the snake is moving

    # Step 12: Is the snake eating?

    return snake, end, direction, food

# Initialisation of the game window ==> do not delete
pygame.init()
# Step 2.1: replace 100,100 by using the correct variables
console = pygame.display.set_mode((100,100))

# Set window title
pygame.display.set_caption("Snake by Rubika_BI1_Anim3D")

# Step 5: Game elements variables


# the clock to make the time move
clock = pygame.time.Clock()
tick = 1

# Step 6.4: As long as the game is not over
while False :
    # Step 2.2: colour the background
    console.fill()

    # Update the elements
    snake_positions, game_end, snake_direction, food_position = game_turn(snake_positions, game_end, snake_direction, food_position)
    clock.tick(tick)

# End of game
print("Game Over")
pygame.quit()
quit()