import pygame
import time
import os

# Initialize Pygame
pygame.init()

# Set up the screen
screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
screen_width, screen_height = screen.get_size()

# Load digit images
image_folder = os.path.join(os.path.dirname(__file__), "assets")
digit_images = {str(i): pygame.image.load(os.path.join(image_folder, f"{i}.png")) for i in range(10)}

# Scale images to fit the screen
digit_width = screen_width // 10
digit_height = screen_height // 2
digit_images = {k: pygame.transform.scale(img, (digit_width, digit_height)) for k, img in digit_images.items()}

# Define functions
def render_time(current_time):
    """Displays the current time on the screen."""
    x_position = screen_width // 2 - digit_width * 3  # Start drawing in the middle of the screen

    for char in current_time:
        if char == ":":
            x_position += digit_width // 2  # Adjust for the colon spacing
            continue
        
        digit = digit_images[char]
        screen.blit(digit, (x_position, screen_height // 2 - digit_height // 2))
        x_position += digit_width  # Move to the next position

def flip_animation(old_digit, new_digit, x, y):
    """Creates a flipping animation for digit changes."""
    for i in range(1, 11):
        # Clear the area
        screen.fill((0, 0, 0), (x, y, digit_width, digit_height))

        # Top half of the old digit
        scale = digit_height * (11 - i) // 10
        offset = (digit_height - scale) // 2
        old_part = pygame.transform.scale(old_digit, (digit_width, scale))
        screen.blit(old_part, (x, y + offset))

        pygame.display.flip()
        pygame.time.delay(50)

        # Bottom half of the new digit
        new_part = pygame.transform.scale(new_digit, (digit_width, scale))
        screen.blit(new_part, (x, y + offset))

        pygame.display.flip()
        pygame.time.delay(50)

# Main game loop
running = True
last_time = ""  # Store the last displayed time for comparison

while running:
    # Clear the screen
    screen.fill((0, 0, 0))  # Black background

    # Get current time as HHMMSS
    current_time = time.strftime("%H%M%S")

    # Check for time changes and animate flips
    if last_time:
        for i, char in enumerate(current_time):
            if last_time[i] != char:  # If the digit has changed
                x = screen_width // 2 - digit_width * 3 + i * digit_width
                y = screen_height // 2 - digit_height // 2
                flip_animation(digit_images[last_time[i]], digit_images[char], x, y)

    # Render the current time
    render_time(current_time)
    pygame.display.flip()

    # Update last time
    last_time = current_time

    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:  # Exit on Escape key
                running = False

    pygame.time.delay(100)  # Delay to control frame rate

pygame.quit()
