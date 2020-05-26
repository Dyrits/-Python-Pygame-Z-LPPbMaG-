import pygame
import random
from classes.GameObject import GameObject, Hero, NPC

# Defining the class of the game:


class Game:

    # Setting the framerate:
    tick_rate = 60

    # Initializing the class:
    def __init__(self, title, width, height, background):
        self.title = title
        self.width = width
        self.height = height
        self.background = pygame.transform.scale(pygame.image.load(background), (width, height))

        # Displaying the window:
        self.game_screen = pygame.display.set_mode((width, height))
        self.game_screen.blit(self.background, (0, 0))
        pygame.display.set_caption(title)

    # Défining the main loop of the game:
    def run_game_loop(self, level):
        game_over = False
        win = False
        direction = 0

        # Creating the character at the bottom of the screen, calling the class :
        hero = Hero('hero.png', 375, 750, 50, 50)
        # Creating NPCs:
        npc_0 = NPC('npc.png', 50, 400, 50, 50)
        npc_1 = NPC('npc.png', 650, 200, 50, 50)
        npc_2 = NPC('npc.png', 250, 600, 50, 50)
        npc_3 = NPC('npc.png', 450, 500, 50, 50)
        npc_4 = NPC('npc.png', 550, 300, 50, 50)

        npc_0.speed += level
        # Decreasing randomly the speed of the first NPC after the level 10:
        if level > 10:
            npc_0.speed -= random.randrange(0, level // 2)
        if level > 20:
            npc_0.speed -= random.randrange(0, level // 2)

        npc_1.speed = level
        # Increasing randomly the speed of the second NPC after the level 10:
        if level > 10:
            npc_0.speed += random.randrange(0, level // 2)
        if level > 20:
            npc_0.speed += random.randrange(0, level)

        npc_2.speed += level // 5
        # Increasing the speed of the thrid NPC every 5 levels (for one level).
        if level % 5 == 0:
            npc_2.speed += (random.randrange(level // 5, level // 5 * 5))

        npc_3.speed += level // 2
        if level % 2 == 0:
            npc_3.speed += level // 2

        # Defining the speed of the fifth NPC randomly:
        npc_4.speed += random.randrange(0, level * 2)


        # Creating the portal:
        warp = GameObject('warp.png', 375, 0, 50, 50)

        # Running the loop as long as the game is not over:
        while not game_over:

            # Checking the player's input:
            for event in pygame.event.get():
                # Quitting:
                if event.type == pygame.QUIT:
                    game_over = True
                # Detecting when a key is pressed on:
                elif event.type == pygame.KEYDOWN:
                    # Moving up:
                    if event.key == pygame.K_UP:
                        direction = 1
                    # Moving down:
                    elif event.key == pygame.K_DOWN:
                        direction = -1
                # Detecting when a key is releaded:
                elif event.type == pygame.KEYUP:
                    # Not moving:
                    if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                        direction = 0
                # Following the input in the terminal:
                print(event)

            # Displaying the background over the character:
            self.game_screen.blit(self.background, (0, 0))

            # Displayind the portal over the background:
            warp.draw(self.game_screen)

            # Updating the character position:
            hero.move(direction, self.height)
            # Displaying the character over the background:
            hero.draw(self.game_screen)

            # Displaying the NPC over the background:
            npc_0.move(self.width)
            npc_0.draw(self.game_screen)
            if level > 5:
                npc_1.move(self.width)
                npc_1.draw(self.game_screen)
            if level > 10:
                npc_2.move(self.width)
                npc_2.draw(self.game_screen)
            if level > 15:
                npc_3.move(self.width)
                npc_3.draw(self.game_screen)
            if level > 20:
                npc_4.move(self.width)
                npc_4.draw(self.game_screen)

            level_display = pygame.font.SysFont('Bahnschrift', 20).render(f'Level {level}', True, (0, 0, 0))
            self.game_screen.blit(level_display, (220, 20))

            # Creating a list of NPCs:
            npcs = [npc_0]
            if level > 5:
                npcs.append(npc_1)
            if level > 10:
                npcs.append(npc_2)
            if level > 15:
                npcs.append(npc_3)
            if level > 20:
                npcs.append(npc_4)

            # Initializing font:
            pygame.font.init()

            # Ending the game if there is a collision:
            if hero.detect_collision(warp):
                game_over = True
                win = True
                text = pygame.font.SysFont('Bahnschrift', 50).render('Good job!', True, (0, 0, 0))
                self.game_screen.blit(text, (300, 300))
                pygame.display.update()
                pygame.time.Clock().tick(1)
                break
            else:
                for enemy in npcs:
                    if hero.detect_collision(enemy):
                        game_over = True
                        win = False
                        text = pygame.font.SysFont('Bahnschrift', 75).render('Loser!', True, (0, 0, 0))
                        self.game_screen.blit(text, (300, 300))
                        pygame.display.update()
                        pygame.time.Clock().tick(1)
                        break
                        

            # Updating the game for every tick of the clock.
            pygame.display.update()
            pygame.time.Clock().tick(self.tick_rate)

        if win:
            self.run_game_loop(level + 1)
        else:
            return