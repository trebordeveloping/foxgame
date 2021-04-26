#-------------------------------------------------------------------------------
# Name:        colours
# Purpose:     store colours for the game
#
# Author:      robert.cormack
#
# Created:     20/04/2021
# Copyright:   (c) robert.cormack 2021
# Licence:     <your licence>
#-------------------------------------------------------------------------------

class Colours():

    def __init__(self, black, white, green, red, yellow):

        self.black = black
        self.white = white
        self.green = green
        self.red = red
        self.yellow = yellow

clrs = Colours(

    (0, 0, 0),          # black
    (255, 255, 255),    # white
    (0, 255, 0),        # green
    (255, 0, 0),        # red
    (255, 255, 0)       # yellow

    )
