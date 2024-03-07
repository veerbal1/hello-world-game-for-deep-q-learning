import pygame
import random

from dqn_agent import DQNAgent
import numpy as np

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

# Initialize the DQN agent
state_size = 4 # [box_x, box_y, dot_x, dot_y]
action_size = 4 # [move_left, move_right, move_up, move_down]
agent = DQNAgent(state_size, action_size)

# Main game loop
running = True
while running:
    state = np.array(box_pos + dot_pos) # Convert to numpy array
    action = agent.act(state) # Get the action from the agent
    reward = 0 # Initialize the reward
    done = False # Initialize done
    
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            done = True
            
    if action == 0: # Move left
                box_pos[0] = max(0, box_pos[0] - 10)  # Move left, don't go outside the window
    elif action == 1: # Move right
                box_pos[0] = min(window_size[0] - box_size[0], box_pos[0] + 10)  # Move right
    elif action == 2: # Move up
                box_pos[1] = max(0, box_pos[1] - 10)  # Move up
    elif action == 3: # Move down
                box_pos[1] = min(window_size[1] - box_size[1], box_pos[1] + 10)  # Move down
                
                
             # Check if the box and dot overlap
    if pygame.Rect(box_pos[0], box_pos[1], *box_size).colliderect(pygame.Rect(dot_pos[0], dot_pos[1], *dot_size)):
                # Reposition the dot
                dot_pos = [random.randint(0, window_size[0] - dot_size[0]), random.randint(0, window_size[1]-dot_size[1])]
                
                # Increase score
                score += 1
                reward = 1
    
    next_state = np.array(box_pos + dot_pos) # Convert to numpy array
    agent.remember(state, action, reward, next_state, done) # Store the experience in memory
    
    if len(agent.memory) > 32:
        agent.replay(32)
    
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