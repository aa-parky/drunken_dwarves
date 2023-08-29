import pygame
import sys

# Initialize pygame
pygame.init()

# Window size
window_size = (800, 600)
max_scrollable_area = (1456, 816)

# Create the main surface
screen = pygame.display.set_mode(window_size)
pygame.display.set_caption("Scrollable Window")

# Load the background image
background_image = pygame.image.load("test.png").convert()

# Colors
white = (255, 255, 255)
black = (0, 0, 0)
grid_color = (200, 200, 200)
grid_alpha = 50  # Opacity between 0 (transparent) and 255 (opaque)
grid_surface = pygame.Surface(window_size, pygame.SRCALPHA)  # Create a transparent surface for the grid


# Font for displaying coordinates
font = pygame.font.Font(None, 24)

# Set initial scroll position to center of the image
scroll_x = (max_scrollable_area[0] - window_size[0]) // 2
scroll_y = (max_scrollable_area[1] - window_size[1]) // 2


# Scroll speed
scroll_speed = 5

# Grid properties
grid_size = 32

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # Handle key presses for scrolling
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                scroll_y -= scroll_speed
            elif event.key == pygame.K_DOWN:
                scroll_y += scroll_speed
            elif event.key == pygame.K_LEFT:
                scroll_x -= scroll_speed
            elif event.key == pygame.K_RIGHT:
                scroll_x += scroll_speed
            elif event.key == pygame.K_0:  # "0" key to re-center
                scroll_x = (max_scrollable_area[0] - window_size[0]) // 2
                scroll_y = (max_scrollable_area[1] - window_size[1]) // 2

    # Apply bounds checking to scroll position
    if scroll_x < 0:
        scroll_x = 0
    elif scroll_x > max_scrollable_area[0] - window_size[0]:
        scroll_x = max_scrollable_area[0] - window_size[0]

    if scroll_y < 0:
        scroll_y = 0
    elif scroll_y > max_scrollable_area[1] - window_size[1]:
        scroll_y = max_scrollable_area[1] - window_size[1]

    # Get mouse coordinates
    mouse_x, mouse_y = pygame.mouse.get_pos()

    # Clear the screen
    screen.fill(white)

    # Blit the background image
    screen.blit(background_image, (-scroll_x, -scroll_y))

    # Calculate visible area
    visible_area = pygame.Rect(scroll_x, scroll_y, window_size[0], window_size[1])

    # Draw grid
    grid_surface.fill((0, 0, 0, 0))  # Clear the grid surface with transparent color

    for x in range(0, window_size[0], grid_size):
        for y in range(0, window_size[1], grid_size):
            pygame.draw.rect(grid_surface, grid_color + (grid_alpha,),
                             (x, y, grid_size, grid_size), 1)

    screen.blit(grid_surface, (0, 0))  # Blit the grid surface onto the main screen

    # Display mouse coordinates
    mouse_coords_text = font.render(f"Mouse: ({mouse_x}, {mouse_y})", True, black)
    screen.blit(mouse_coords_text, (10, 10))

    pygame.display.flip()

pygame.quit()
sys.exit()

