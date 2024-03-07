import pygame
import random

# Initialize Pygame
pygame.init()

# Set the dimensions of the window
window_size = (600, 400)

# Create the window
window = pygame.display.set_mode(window_size)

# Define the box
box_size = (50,50)
box_color = (255, 0, 0) # Red
box_pos = [random.randint(0, window_size[0] - box_size[0]), random.randint(0, window_size[1]-box_size[1])]

# Define the dot
dot_size = (10,10)
dot_color = (0, 255, 0) # Green
dot_pos = [random.randint(0, window_size[0] - dot_size[0]), random.randint(0, window_size[1]-dot_size[1])]

# Initialize score
score = 0

# Define the font for the score text
font = pygame.font.Font(None, 36)

# Main game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                box_pos[0] = max(0, box_pos[0] - 10)  # Move left, don't go outside the window
            elif event.key == pygame.K_RIGHT:
                box_pos[0] = min(window_size[0] - box_size[0], box_pos[0] + 10)  # Move right
            elif event.key == pygame.K_UP:
                box_pos[1] = max(0, box_pos[1] - 10)  # Move up
            elif event.key == pygame.K_DOWN:
                box_pos[1] = min(window_size[1] - box_size[1], box_pos[1] + 10)  # Move down
                
                
             # Check if the box and dot overlap
            if pygame.Rect(box_pos[0], box_pos[1], *box_size).colliderect(pygame.Rect(dot_pos[0], dot_pos[1], *dot_size)):
                # Reposition the dot
                dot_pos = [random.randint(0, window_size[0] - dot_size[0]), random.randint(0, window_size[1]-dot_size[1])]
                
                # Increase score
                score += 1
            
    window.fill((0,0,0)) # Clear the window
    pygame.draw.rect(window, box_color, pygame.Rect(box_pos[0], box_pos[1], *box_size))
    pygame.draw.rect(window, dot_color, pygame.Rect(dot_pos[0], dot_pos[1], *dot_size)) # Draw the dot
    
    # Draw the score
    score_text = font.render("Score: " + str(score), True, (255, 255, 255))
    window.blit(score_text, (10, 10))
    
     # Update the window
    pygame.display.flip()

# Quit Pygame
pygame.quit()