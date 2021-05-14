import pygame as pg

class graphic():
    def __init__(self):
        pg.init()
        self.screen_size = [800, 800]
        self.screen = pg.display.set_mode(self.screen_size)
        pg.display.set_caption("TANK GAME")
        self.playing = False

    class tank():
        def __init__(self):
            self.UP = 8
            self.DOWN = 2
            self.RIGHT = 6
            self.LEFT = 4
            self.TANK_LENGTH = 40
            self.TANK_WIDTH = 26
            self.TANK_COLOR_UNDER = [0, 102, 0]
            self.TANK_COLOR_UP = [0, 153, 0]
            self.tank_direction = self.UP
            self.tank_location = [40, 40]
            self.TANK_R = 10
            self.TANK_CANNON_WIDTH = 2
            self.set_color_player()
        
        def set_screen(self, screen):
            self.screen = screen

        def set_color_player(self):
            self.tank_color_under = self.TANK_COLOR_UNDER
            self.tank_color_up = self.TANK_COLOR_UP

        def draw_tank(self):
            if (self.tank_direction  == self.UP) or (self.tank_direction == self.DOWN):
                pg.draw.rect(self.screen, self.tank_color_under, self.tank_location + [self.TANK_WIDTH] + [self.TANK_LENGTH])
                pg.draw.circle(self.screen, self.tank_color_up, [self.tank_location[0]+self.TANK_WIDTH/2] + [self.tank_location[1]+self.TANK_LENGTH/2], self.TANK_R)
            else:
                pg.draw.rect(self.screen, self.tank_color_under, self.tank_location + [self.TANK_LENGTH] + [self.TANK_WIDTH])
                pg.draw.circle(self.screen, self.tank_color_up, [self.tank_location[0]+self.TANK_LENGTH/2] + [self.tank_location[1]+self.TANK_WIDTH/2], self.TANK_R)
            if (self.tank_direction  == self.UP):
                pg.draw.rect(self.screen, self.tank_color_up,[self.tank_location[0]+self.TANK_WIDTH/2-1] + [self.tank_location[1]] + [2] + [self.TANK_LENGTH/2])
            elif (self.tank_direction  == self.DOWN):
                pg.draw.rect(self.screen, self.tank_color_up, [self.tank_location[0]+self.TANK_WIDTH/2-1] + [self.tank_location[1]+self.TANK_LENGTH/2] + [2] + [self.TANK_LENGTH/2])
            elif (self.tank_direction  == self.LEFT):
                pg.draw.rect(self.screen, self.tank_color_up, [self.tank_location[0]] + [self.tank_location[1]+self.TANK_WIDTH/2-1] + [self.TANK_LENGTH/2] + [2])
            elif (self.tank_direction  == self.RIGHT):
                pg.draw.rect(self.screen, self.tank_color_up, [self.tank_location[0]+self.TANK_LENGTH/2] + [self.tank_location[1]+self.TANK_WIDTH/2-1] + [self.TANK_LENGTH/2] + [2])

        def set_direction(self, direction):
            self.tank_direction = direction

    class background():
        def __init__(self):
            self.WHITE = [255, 255, 255]
            self.BLACK = [0, 0, 0]
            self.BACKGROUND_1 = [89, 89, 89]

        def set_screen(self, screen):
            self.screen = screen

        def draw_background(self):
            pg.draw.rect(self.screen, self.BACKGROUND_1, [0, 0, 800, 800])

    def test(self):
        self.playing = True
        clock = pg.time.Clock()
        clock.tick(10)
        background = self.background()
        tank = self.tank()
        background.set_screen(self.screen)
        tank.set_screen(self.screen)
        while self.playing:
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    self.playing = False
            background.draw_background()
            tank.tank_direction
            tank.draw_tank()
            pg.display.flip()
        pg.quit()

if __name__ == '__main__':
    T = graphic()
    T.test()
    