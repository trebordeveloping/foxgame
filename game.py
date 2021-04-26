#-------------------------------------------------------------------------------
# Name:        game
# Purpose:
#
# Author:      robert.cormack
#
# Created:     24/03/2021
# Copyright:   (c) robert.cormack 2021
# Licence:     <your licence>
#-------------------------------------------------------------------------------

def main():

    from colours import clrs
    from components import Player, Obstacle, Floor, Screen

    import pygame

    

    # Start
    pygame.init()

    # Making screen

    scr = Screen(
                700,    # width
                500,    # height
                pygame.image.load("background.jpg")
                )
    
    screen = pygame.display.set_mode(scr.dimensions)
    pygame.display.set_caption("My Game")

    # Loop until exit
    done = False

    # To set screen refresh rate
    clock = pygame.time.Clock()

    # Hide cursor
    pygame.mouse.set_visible(0)

    # ----- ALL GAME VARIABLES GO BELOW THIS COMMENT -----

    # Player
    player = Player(
                100,    # x-coordinate
                360,    # y-coordinate
                25,     # jump height
                False,  # jump variable
                3,      # health points
                0,      # immunity
                0,      # score
                [pygame.image.load("fox_sprite1.png"),
                 pygame.image.load("fox_sprite2.png"),
                 pygame.image.load("fox_sprite3.png")]
                )

    # Obstacle
    ob = Obstacle(
                700,    # x-coordinate
                350,    # y-coordinate
                pygame.image.load("fridge.png"), # sprite
                5,      # speed
                1      # count
                )

    floor = Floor(
                pygame.image.load("floor.png") # sprite
                )

    spriteCount = 0

    # Game over screen
    gameOverScreen = True

    def drawScreen(spriteCount):

        # draw background
        screen.blit(scr.sprite, (0, 0))
        
        # draw floor
        screen.blit(floor.sprite, (0, scr.sprH-20))

        # put obstacle on screen
        screen.blit(ob.sprite, (ob.x, ob.y))

        # put player on screen
        if player.jumpVar:
            screen.blit(player.sprites[2], (player.x, player.y))
        else:
            screen.blit(player.sprites[spriteCount], (player.x, player.y))

        

    # ----- ALL GAME VARIABLES GO ABOVE THIS COMMENT -----

    # -------- MAIN LOOP -----------
    while not done:

        # ----- EVENT PROCESSING GOES BELOW THIS COMMENT -----

        for event in pygame.event.get():  # Player did something
            if event.type == pygame.QUIT: # Player exits
                done = True               # End loop
                gameOverScreen = False

            # Player pressed a key

            elif event.type == pygame.KEYDOWN:

                # Player pressed the spacebar
                if event.key == pygame.K_SPACE and player.jumpVar == False:
                    player.jumpVar = True

        # ---- EVENT PROCESSING GOES ABOVE THIS COMMENT -----

        # ---- GAME LOGISTICS GO BELOW THIS COMMENT -----

        # Check if player is hit
        player.checkHit(ob.x, ob.y, ob.width, ob.height)

        # Game over if player has no more health points
        if player.hp == 0:
            done = True

        # Player jump
        if player.jumpVar:

            player.jump()

        # Increase score
        if ob.x < player.x:
            player.score = ob.count

        # Obstacle movement
        if ob.x > -120:
            ob.x -= ob.speed

        # New obstacle
        else:
            ob.x = scr.width
            ob.speed += 1
            ob.count += 1

        # ----- GAME LOGISTICS GO ABOVE THIS COMMENT -----

        # ----- GAME DRAWINGS GO BELOW THIS COMMENT -----

        # Clear screen
        screen.fill(clrs.white)

        if spriteCount >= 27:
            spriteCount = 1
            

        drawScreen(spriteCount // 9)

        spriteCount += 1

        

        # Display health
        font = pygame.font.Font(None, 30)
        text = font.render("Health: " + str(player.hp), 1, clrs.black)
        screen.blit(text, (550,10))

        # Display score
        text = font.render("Score: " + str(player.score), 1, clrs.black)
        screen.blit(text, (50, 10))

        # ----- GAME DRAWINGS GO ABOVE THIS COMMENT -----

        # Update screen
        pygame.display.flip()

        # 60 FPS
        clock.tick(60)

    # PÃƒÂ³rtate bien con el IDLE.
    # Si nos olvidamos de ÃƒÂ©sta lÃƒÂ­nea, el programa se 'colgarÃƒÂ¡'
    # en la salida.

    # ----- GAME OVER SCREEN GOES BELOW THIS COMMENT ----

    if gameOverScreen:

        # Print game over
        font = pygame.font.Font(None, 50)
        text = font.render("GAME OVER", 1, clrs.black)
        screen.blit(text, (250, 225))

        # Update screen
        pygame.display.flip()

        done = False

        while not done:
            for event in pygame.event.get():  # Player did something
                if event.type == pygame.QUIT: # Player exits
                    done = True

    # ----- GAME OVER SCREEN GOES ABOVE THIS COMMENT ----

    pygame.quit()

if __name__ == '__main__':
    main()
