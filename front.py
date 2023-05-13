import pygame

# initialize Pygame
pygame.init()

# set up the window
window_size = (800, 600)
screen = pygame.display.set_mode(window_size)
pygame.display.set_caption("Login Screen")

# set up fonts
font = pygame.font.SysFont("Arial", 24)
button_font = pygame.font.SysFont("Arial", 18)

# set up colors
background_color = (255, 255, 255)
sign_in_button_color = (0, 200, 0)
log_in_button_color = (200, 0, 0)
text_color = (255, 255, 255)

# set up button sizes and positions
button_width = 300
button_height = 150
button_spacing = 40
button_top_margin = 120
sign_in_button_left = (window_size[0] - button_width - button_spacing) // 2
log_in_button_left = sign_in_button_left + button_width + button_spacing

# main loop
while True:
    # event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = pygame.mouse.get_pos()
            if sign_in_button_rect.collidepoint(mouse_pos):
                print("Sign in button pressed")
            elif log_in_button_rect.collidepoint(mouse_pos):
                print("Log in button pressed")

    # fill the background
    screen.fill(background_color)

    # render the buttons
    sign_in_button = button_font.render("Sign In", True, text_color)
    sign_in_button_rect = sign_in_button.get_rect()
    sign_in_button_rect.left = sign_in_button_left
    sign_in_button_rect.top = button_top_margin
    pygame.draw.rect(screen, sign_in_button_color, sign_in_button_rect)
    pygame.draw.rect(screen, text_color, sign_in_button_rect, 2)
    sign_in_button_rect.inflate_ip(-10, -10)
    screen.blit(sign_in_button, sign_in_button_rect)

    log_in_button = button_font.render("Log In", True, text_color)
    log_in_button_rect = log_in_button.get_rect()
    log_in_button_rect.left = log_in_button_left
    log_in_button_rect.top = button_top_margin
    pygame.draw.rect(screen, log_in_button_color, log_in_button_rect)
    pygame.draw.rect(screen, text_color, log_in_button_rect, 2)
    log_in_button_rect.inflate_ip(-10, -10)
    screen.blit(log_in_button, log_in_button_rect)

    # check if the mouse is over a button
    mouse_pos = pygame.mouse.get_pos()
    if sign_in_button_rect.collidepoint(mouse_pos):
        pygame.draw.rect(screen, (100, 255, 100), sign_in_button_rect, 3)
    elif log_in_button_rect.collidepoint(mouse_pos):
        pygame.draw.rect(screen, (255, 100, 100), log_in_button_rect, 3)

    # update the display
    pygame.display.update()
