import pygame as pg

class Graphic():
    def __init__(self):
        pg.init()
        self.screen_size = [800, 800]
        self.screen = pg.display.set_mode(self.screen_size)
        pg.display.set_caption("TANK GAME")
        self.UP = 8
        self.DOWN = 2
        self.RIGHT = 6
        self.LEFT = 4
        self.TANK_LENGTH = 40
        self.TANK_WIDTH = 26
        self.tank_direction = self.UP
        self.tank_location = [40, 40]
        self.TANK_COLOR_UNDER = [0, 102, 0]
        self.TANK_COLOR_UP = [0, 153, 0]
        self.BLACK = [255, 255, 255]
        self.BACKGROUND_1 = [89, 89, 89]
        self.TANK_R = 10
        self.TANK_CANNON_WIDTH = 2
        self.playing = False

    def draw_tank(self):
        if (self.tank_direction  == self.UP) or (self.tank_direction == self.DOWN):
            pg.draw.rect(self.screen, self.TANK_COLOR_UNDER, self.tank_location + str(self.TANK_WIDTH)+str(self.TANK_LENGTH))
        else:
            pg.draw.rect(self.screen, self.TANK_COLOR_UNDER, self.tank_location + str(self.TANK_LENGTH)+str(self.TANK_WIDTH))
        pg.draw.circle(self.screen, self.TANK_COLOR_UP, str(self.tank_location[0]+13) + str(self.tank_location[1]+20), self.TANK_R)
        if (self.tank_direction  == self.UP):
            pg.draw.rect(self.screen, self.TANK_COLOR_UNDER,str(self.tank_location[0]+self.TANK_WIDTH/2) + str(self.tank_location[1]) + [2] + str(self.TANK_LENGTH/2))
        elif (self.TankDirection  == self.DOWN):
            pg.draw.rect(self.screen, self.TANK_COLOR_UNDER, str(self.tank_location[0]+self.TANK_WIDTH/2) + str(self.tank_location[1]+self.TANK_LENGTH/2) + [2] + str(self.TANK_LENGTH/2))
        elif (self.tank_direction  == self.LEFT):
            pg.draw.rect(self.screen, self.TANK_COLOR_UNDER, str(self.tank_location[0]) + str(self.tank_location[1]+self.TANK_WIDTH/2) + str(self.TANK_LENGTH/2) + [2])
        elif (self.tank_direction  == self.RIGHT):
            pg.draw.rect(self.screen, self.TANK_COLOR_UNDER, str(self.tank_location[0]+self.TANK_LENGTH/2) + str(self.tank_location[1]+self.TANK_WIDTH/2) + str(self.TANK_LENGTH/2) + [2])
        
    def draw_background(self):
        pg.draw.rect(self.screen, self.BACKGROUND_1, [0, 0, 800, 800])

    def test(self):
        print(self.tank_location + str(self.TANK_WIDTH)+str(self.TANK_LENGTH))
    """
        self.playing = True
        clock = pg.time.Clock()
        clock.tick(10)
        while self.playing:
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    self.playing = False
            self.draw_background()
            self.draw_tank()
            pg.display.flip()
        pg.quit()
    """

if __name__ == '__main__':
    T = Graphic()
    T.test()
    