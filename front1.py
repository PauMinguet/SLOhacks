import pygame
import sys
import processes
import user

# Initialize Pygame
pygame.init()
# Define Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (128, 128, 128)
# Set the dimensions of the screen
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Hackathon app")
font = pygame.font.Font(None, 32)

stage = "intro"


# Set the font


if stage == "intro":
    # Set the text boxes
    username_box = pygame.Rect(250, 125, 300, 50)
    password_box = pygame.Rect(250, 250, 300, 50)
    # Set the buttons
    login_button = pygame.Rect(200, 375, 125, 50)
    signup_button = pygame.Rect(475, 375, 125, 50)
    # Set the button text
    login_text = font.render("Login", True, BLACK)
    signup_text = font.render("Sign Up", True, BLACK)
    # Set the default text
    username = ""
    password = ""

elif stage == ""




# Main loop
while True:
    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            
            
            # Handle button clicks
            if stage == "intro":
                if login_button.collidepoint(pygame.mouse.get_pos()):
                    processes.log_in(username, password)
                    stage = "processes"
                elif signup_button.collidepoint(pygame.mouse.get_pos()):
                    processes.sign_in(username, password)
                    stage = "processes"
            elif stage == "processes":


        # Handle key events
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:
                # Clear the text boxes on Enter
                username = ""
                password = ""
            else:
                # Add characters to the text boxes
                if stage == "intro":
                    if username_box.collidepoint(pygame.mouse.get_pos()):
                        if event.key == pygame.K_BACKSPACE:
                            username = username[:-1]
                        else:
                            username += event.unicode
                    elif password_box.collidepoint(pygame.mouse.get_pos()):
                        if event.key == pygame.K_BACKSPACE:
                            password = password[:-1]
                        else:
                            password += event.unicode

    # Fill the background
    screen.fill(WHITE)

    
    
    if stage == "intro":
        # Draw the text boxes
        pygame.draw.rect(screen, GRAY, username_box, 2)
        pygame.draw.rect(screen, GRAY, password_box, 2)

        # Draw the text in the text boxes
        username_text = font.render(username, True, BLACK)
        screen.blit(username_text, (username_box.x + 5, username_box.y + 5))
        password_text = font.render("*" * len(password), True, BLACK)
        screen.blit(password_text, (password_box.x + 5, password_box.y + 5))

        # Draw the buttons
        if username != "" and password != "":
            pygame.draw.rect(screen, GRAY, login_button, 2)
            pygame.draw.rect(screen, GRAY, signup_button, 2)

        # Draw the button text
        screen.blit(login_text, (login_button.x + 25, login_button.y + 15))
        screen.blit(signup_text, (signup_button.x + 10, signup_button.y + 15))

        pygame.draw.rect(screen, GRAY, login_button, 2)
        pygame.draw.rect(screen, GRAY, signup_button, 2)
    

    # Update the screen
    pygame.display.update()
