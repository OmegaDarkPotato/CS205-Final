import constants as c
import pygame
from pygame.locals import *
import os

class Menu():

    # initialize the menu with buttons
    def __init__(self, MENUSTAT, screen, clock, background1):
        self.playButton = pygame.image.load(c.imagePath + c.playButton)
        self.helpButton = pygame.image.load(c.imagePath + c.helpButton)
        self.exitButton = pygame.image.load(c.imagePath + c.exitButton)
        self.MENUSTAT = MENUSTAT
        self.screen = screen
        self.clock = clock
        self.background1 = background1
        self.fpsClock = pygame.time.Clock()


    def formatButtons(self, menu, animateMenuX):
        formattedPlayButton = pygame.transform.scale(self.playButton, (100, 50))  # size change
        formattedHelpButton = pygame.transform.scale(self.helpButton, (100, 50))  # size change
        formattedExitButton = pygame.transform.scale(self.exitButton, (100, 50))  # size change

        self.screen.blit(menu, (animateMenuX, 0))  # add to layer starting left top corner position
        self.screen.blit(formattedPlayButton,
                         (c.windowLength - int(c.windowLength / 2) - 250, c.windowWidth - int(c.windowWidth / 5)))
        self.screen.blit(formattedHelpButton,
                         (c.windowLength - int(c.windowLength / 2), c.windowWidth - int(c.windowWidth / 5)))  # middle
        self.screen.blit(formattedExitButton,
                         (c.windowLength - int(c.windowLength / 2) + 250, c.windowWidth - int(c.windowWidth / 5)))

        return formattedPlayButton, formattedHelpButton, formattedExitButton


    def placeButtons(self, currentMouseX, currentMouseY, formattedPlayButton, formattedHelpButton, formattedExitButton):
        # if lowerbound < mousepos < higher bound and for y.. do button
        # difference is button size formatted
        if ((c.windowLength - int(c.windowLength / 2) - 250) < currentMouseX < (
                c.windowLength - int(c.windowLength / 2) - 150)) and (
                (c.windowWidth - int(c.windowWidth / 5)) < currentMouseY < (
                c.windowWidth - int(c.windowWidth / 5) + 50)):
            self.screen.blit(formattedPlayButton,
                             (c.windowLength - int(c.windowLength / 2) - 250, c.windowWidth - int(c.windowWidth / 5)),
                             special_flags=pygame.BLEND_RGBA_MULT)
        elif ((c.windowLength - int(c.windowLength / 2)) < currentMouseX < (
                c.windowLength - int(c.windowLength / 2) + 100)) and (
                (c.windowWidth - int(c.windowWidth / 5)) < currentMouseY < (
                c.windowWidth - int(c.windowWidth / 5) + 50)):
            self.screen.blit(formattedHelpButton,
                             (c.windowLength - int(c.windowLength / 2), c.windowWidth - int(c.windowWidth / 5)),
                             special_flags=pygame.BLEND_RGBA_MULT)  # middle
        elif ((c.windowLength - int(c.windowLength / 2) + 250) < currentMouseX < (
                c.windowLength - int(c.windowLength / 2) + 350)) and (
                (c.windowWidth - int(c.windowWidth / 5)) < currentMouseY < (
                c.windowWidth - int(c.windowWidth / 5) + 50)):
            self.screen.blit(formattedExitButton,
                             (c.windowLength - int(c.windowLength / 2) + 250, c.windowWidth - int(c.windowWidth / 5)),
                             special_flags=pygame.BLEND_RGBA_MULT)

    def startMenu(self):
        animateMenuX = 0
        print(self.MENUSTAT)
        while self.MENUSTAT == True:
            mouse = pygame.mouse.get_pos()
            # check mouse pos and highlight button when mouse hovers above
            currentMouseX = mouse[0]
            currentMouseY = mouse[1]

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    quit()
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    # on right click on play
                    if (event.button == 1) and ((c.windowLength - int(c.windowLength / 2) - 250) < currentMouseX < (
                            c.windowLength - int(c.windowLength / 2) - 150)) and (
                            (c.windowWidth - int(c.windowWidth / 5)) < currentMouseY < (
                            c.windowWidth - int(c.windowWidth / 5) + 50)):
                        print("Starting game ...")
                        menu = False
                        running = True

                        # prep load screen while game inits
                        loadScreen = pygame.image.load(c.imagePath + c.loadingImage)
                        formattedLoadScreen = pygame.transform.scale(loadScreen, (c.windowLength, c.windowWidth))
                        self.screen.blit(formattedLoadScreen, (0, 0))
                        pygame.display.update()  # update visuals
                        # TODO run the game
                        #game(running, screen, background1, clock)

                    # on right click on help (OPTIONS should rename latre)
                    elif (event.button == 1) and ((c.windowLength - int(c.windowLength / 2)) < currentMouseX < (
                            c.windowLength - int(c.windowLength / 2) + 100)) and (
                            (c.windowWidth - int(c.windowWidth / 5)) < currentMouseY < (
                            c.windowWidth - int(c.windowWidth / 5) + 50)):
                        print("opening options ...")
                        # menu = False
                        # running = True

                        # show help/setuup screen ? then go back to menu screen

                    # on right click on exit
                    elif (event.button == 1) and ((c.windowLength - int(c.windowLength / 2) + 250) < currentMouseX < (
                            c.windowLength - int(c.windowLength / 2) + 350)) and (
                            (c.windowWidth - int(c.windowWidth / 5)) < currentMouseY < (
                            c.windowWidth - int(c.windowWidth / 5) + 50)):
                        print("Shutting down ...")
                        os._exit(0)  # clean exit

            self.screen.fill((0, 0, 0))
            self.clock.tick(30)

            # menu animation
            menu = pygame.transform.scale(self.background1, (int(c.windowLength * 1.3), c.windowWidth))  # zoom in on bg

            formattedPlayButton, formattedHelpButton, formattedExitButton = self.formatButtons(menu, animateMenuX)

            ##        message_to_screen("Players: ", red, screen)



            # # check mouse pos and highlight button when mouse hovers above
            currentMouseX = mouse[0]
            currentMouseY = mouse[1]

            self.placeButtons(currentMouseX, currentMouseY, formattedPlayButton, formattedHelpButton, formattedExitButton)

            pygame.display.update()  # update visuals
            self.fpsClock.tick(30)

            animateMenuX -= 0.5
            if animateMenuX <= -400:
                animateMenuX = 0