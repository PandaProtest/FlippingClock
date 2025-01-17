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
digit_images = {
    str(i): pygame.image.load(os.path.join(image_folder, f"{i}.png")) for i in range(10)
}

# Define padding and digit dimensions
side_padding = screen_width // 100
top_bottom_padding = screen_height // 20
digit_spacing = 5  # Padding between hours and minutes
digit_width = (screen_width - 2 * side_padding - digit_spacing) // 4
digit_height = screen_height - 2 * top_bottom_padding
digit_images = {
    k: pygame.transform.scale(img, (digit_width, digit_height)) for k, img in digit_images.items()
}

# Flipping animation for a pair of digits
def flip_pair_animation(old_digits, new_digits, x_positions, y_position):
    """Animate flipping a pair of digits (hours or minutes) in unison."""
    duration = 10  # Number of steps in the animation
    for phase in range(duration):
        pygame.draw.rect(screen, (0, 0, 0), (x_positions[0], y_position, digit_width * 2 + digit_spacing, digit_height))

        for i in range(2):  # Animate both digits in the pair
            old_digit = old_digits[i]
            new_digit = new_digits[i]
            x_position = x_positions[i]

            if phase < duration / 2:  # First half: old digit shrinks
                shrink_height = int(digit_height * (1 - phase / (duration / 2)))
                temp_digit = pygame.transform.scale(old_digit, (digit_width, shrink_height))
                screen.blit(temp_digit, (x_position, y_position))
            else:  # Second half: new digit grows
                grow_height = int(digit_height * ((phase - duration / 2) / (duration / 2)))
                temp_digit = pygame.transform.scale(new_digit, (digit_width, grow_height))
                screen.blit(temp_digit, (x_position, y_position))

        pygame.display.flip()
        pygame.time.delay(20)

# Render function to display the time
def render_time(current_time):
    screen.fill((0, 0, 0))  # Clear the screen
    x_position = side_padding
    for index, digit in enumerate(current_time):
        if digit.isdigit():
            screen.blit(digit_images[digit], (x_position, top_bottom_padding))
        x_position += digit_width + (digit_spacing if index == 1 else 0)

# Main loop
running = True
last_time = "0000"  # Initialize to "0000"

while running:
    current_time = time.strftime("%I%M").rjust(4, '0')  # Get 12-hour format with leading zeros

    # Check if hours changed and animate the hour digits if needed
    if current_time[:2] != last_time[:2]:
        old_digits = [digit_images[last_time[0]], digit_images[last_time[1]]]
        new_digits = [digit_images[current_time[0]], digit_images[current_time[1]]]
        x_positions = [side_padding, side_padding + digit_width]
        flip_pair_animation(old_digits, new_digits, x_positions, top_bottom_padding)

    # Check if minutes changed and animate the minute digits if needed
    if current_time[2:] != last_time[2:]:
        old_digits = [digit_images[last_time[2]], digit_images[last_time[3]]]
        new_digits = [digit_images[current_time[2]], digit_images[current_time[3]]]
        x_positions = [
            side_padding + 2 * digit_width + digit_spacing,
            side_padding + 3 * digit_width + digit_spacing,
        ]
        flip_pair_animation(old_digits, new_digits, x_positions, top_bottom_padding)

    # Update the time
    last_time = current_time

    # Render the current time after flipping
    render_time(current_time)
    pygame.display.flip()
    pygame.time.delay(100)

    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
            running = False

pygame.quit()
