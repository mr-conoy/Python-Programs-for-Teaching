import pygame
import random

# Initialize pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 400, 400  # Reduced size for easier testing
GRID_SIZE = 20

# Colors
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

# Screen setup
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

# Snake setup
snake_pos = [[100, 100]]  # Start at a position near the center
snake_dir = (GRID_SIZE, 0)  # Initial movement direction
speed = 5  # Starting speed of the snake

# Food setup function
def get_random_food_position():
    return [random.randint(0, (WIDTH // GRID_SIZE) - 1) * GRID_SIZE, 
            random.randint(0, (HEIGHT // GRID_SIZE) - 1) * GRID_SIZE]

food_pos = get_random_food_position()

# Function to move the snake
def move_snake():
    # Calculate new head position
    new_head = [round(snake_pos[0][0] + snake_dir[0]), round(snake_pos[0][1] + snake_dir[1])]
    snake_pos.insert(0, new_head)  # Add the new head at the start of the snake
    
    # Check if snake head is on the food position
    if snake_pos[0] == food_pos:
        print("Food eaten!")  # Debug: confirms food is eaten
        return True  # Snake has eaten the food
    else:
        snake_pos.pop()  # Remove last segment if no food eaten
        return False

# Function to check for collisions with walls or itself
def check_collision():
    head = snake_pos[0]
    # Check wall collisions
    if head[0] < 0 or head[0] >= WIDTH or head[1] < 0 or head[1] >= HEIGHT:
        return True
    # Check self collision
    if head in snake_pos[1:]:
        return True
    return False

# Function to draw the game elements
def draw():
    screen.fill(WHITE)  # Clear screen with white background
    # Draw snake
    for segment in snake_pos:
        pygame.draw.rect(screen, GREEN, pygame.Rect(segment[0], segment[1], GRID_SIZE, GRID_SIZE))
    # Draw food
    pygame.draw.rect(screen, RED, pygame.Rect(food_pos[0], food_pos[1], GRID_SIZE, GRID_SIZE))
    pygame.display.flip()  # Update the display

# Main game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            # Change direction based on arrow keys
            if event.key == pygame.K_UP and snake_dir != (0, GRID_SIZE):
                snake_dir = (0, -GRID_SIZE)
            elif event.key == pygame.K_DOWN and snake_dir != (0, -GRID_SIZE):
                snake_dir = (0, GRID_SIZE)
            elif event.key == pygame.K_LEFT and snake_dir != (GRID_SIZE, 0):
                snake_dir = (-GRID_SIZE, 0)
            elif event.key == pygame.K_RIGHT and snake_dir != (-GRID_SIZE, 0):
                snake_dir = (GRID_SIZE, 0)

    # Move the snake and check if it ate the food
    if move_snake():
        # Reposition food to a new random location
        food_pos = get_random_food_position()
        print(f"New food position: {food_pos}")  # Debug: shows new food position
        speed += 1  # Increase the speed when food is eaten

    # Check for collisions with walls or itself
    if check_collision():
        print("Game Over")
        running = False

    # Draw everything on the screen
    draw()
    clock.tick(speed)  # Control the game speed, which increases as `speed` increases

# Quit pygame
pygame.quit()

