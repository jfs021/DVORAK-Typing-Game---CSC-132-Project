#####################################################################
# author: Taylor DeMent  
# date: 4/8/2024    
# description: A very rough version of the starting screen for the typing test
# featuring a nonfunctional start and settings buttons
#####################################################################

import pygame
pygame.init

# setting dimensions of starting window
start_screen_width = 800
start_screen_height = 600
start_screen = pygame.display.set_mode((start_screen_width, start_screen_height))

# displaying the window name 
pygame.display.set_caption("Main Menu")

# set text color
TEXT_COL = (200, 0, 10)

# pull images of buttons
start_img = pygame.image.load('Python Programs 2/Start_Button').convert_alpha
settings_img = pygame.image.load('Python Programs 2/Settings_Button').convert_alpha

# button class that is used to set up the position and images used for the buttons
class Button():
    def __init__(self, x, y, image):
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.topleft = (x,y)

# function called to display buttons
    def Draw(self):
        start_screen.blit(self.image, (self.rect.x, self.rect.y))

# creates start and setting buttons with their positions and images
start_button = Button(100, 200, start_img)
settings_button = Button(450, 200, settings_img)


# creates the window with the start and settings button on it
run = True
while run:
    start_screen.fill ((250, 250, 250))
    start_button.Draw()
    settings_button.Draw()
