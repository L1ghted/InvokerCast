from pygame import *


class Timer:
    def __init__(self, duration, repeat=False, autostart=False, end_func=None, on_update=None):
        self.duration = duration
        self.repeat = repeat
        self.autostart = autostart
        self.active = False
        self.start_time = 0
        self.end_func = end_func
        self.on_update = on_update
        self.time = 0
        if autostart:
            self.activate()

    def activate(self):
        self.active = True
        self.start_time = time.get_ticks()

    def deactivate(self):
        self.active = False
        self.start_time = 0
        if self.repeat:
            self.activate()

    def current_time(self):
        self.time = time.get_ticks() // 1000
        return self.time

    def update(self):
        if self.active:
            if self.on_update:
                self.on_update()
            self.time = time.get_ticks()
            if self.time - self.start_time >= self.duration:
                if self.end_func:
                    self.end_func()
                self.deactivate()


class Main:
    def __init__(self):
        init()
        self.cast = ['', '', '']
        self.sr1, self.sr2, self.sr3, self.spell, self.last_spell, self.x = None, None, None, None, None, None
        self.window = display.set_mode((1280, 719))
        self.screen = Surface((1280, 719))
        self.cube = Surface((100, 100))


        self.backgrounds = image.load('data/bg1.jpg')
        self.invok = image.load('data/invok.png')
        self.quas = image.load('data/quas.png')
        self.quas_r = image.load('data/quas_r.png')
        self.wex = image.load('data/wex.png')
        self.wex_r = image.load('data/wex_r.png')
        self.exort = image.load('data/exort.png')
        self.exort_r = image.load('data/exort_r.png')
        # Скиллы
        self.sunstrike = image.load('data/sunstrike.png')
        self.emp = image.load('data/emp.png')
        self.coldsnap = image.load('data/coldsnap.png')
        self.blast = image.load('data/blast.png')
        self.forge = image.load('data/forge.png')
        self.ghostwalk = image.load('data/ghostwalk.png')
        self.icewall = image.load('data/icewall.png')
        self.meteor = image.load('data/meteor.png')
        self.tornado = image.load('data/tornado.png')
        self.alacrity = image.load('data/alacrity.png')

    def get_font(self, size):
        return font.SysFont("freesanbold.ttf", size)

    def set_timer(self):
        self.timer.activate()

    def sec(self):
        return self.timer.cu

    def spells(self):
        if self.cast[0] == 'exort' and self.cast[1] == 'exort' and self.cast[
            2] == 'exort' and self.spell != self.sunstrike:
            return self.sunstrike
        elif self.cast[0] == 'wex' and self.cast[1] == 'wex' and self.cast[2] == 'wex' and self.spell != self.emp:
            return self.emp
        elif self.cast[0] == 'quas' and self.cast[1] == 'quas' and self.cast[
            2] == 'quas' and self.spell != self.coldsnap:
            return self.coldsnap

        elif self.cast[0] == 'quas' and self.cast[1] == 'quas' and self.cast[
            2] == 'wex' and self.spell != self.ghostwalk:
            return self.ghostwalk
        elif self.cast[0] == 'wex' and self.cast[1] == 'quas' and self.cast[
            2] == 'quas' and self.spell != self.ghostwalk:
            return self.ghostwalk
        elif self.cast[0] == 'quas' and self.cast[1] == 'wex' and self.cast[
            2] == 'quas' and self.spell != self.ghostwalk:
            return self.ghostwalk

        elif self.cast[0] == 'quas' and self.cast[1] == 'quas' and self.cast[
            2] == 'exort' and self.spell != self.icewall:
            return self.icewall
        elif self.cast[0] == 'exort' and self.cast[1] == 'quas' and self.cast[
            2] == 'quas' and self.spell != self.icewall:
            return self.icewall
        elif self.cast[0] == 'quas' and self.cast[1] == 'exort' and self.cast[
            2] == 'quas' and self.spell != self.icewall:
            return self.icewall
        elif self.cast[0] == 'wex' and self.cast[1] == 'wex' and self.cast[2] == 'quas' and self.spell != self.tornado:
            return self.tornado
        elif self.cast[0] == 'wex' and self.cast[1] == 'quas' and self.cast[2] == 'wex' and self.spell != self.tornado:
            return self.tornado
        elif self.cast[0] == 'quas' and self.cast[1] == 'wex' and self.cast[2] == 'wex' and self.spell != self.tornado:
            return self.tornado

        elif self.cast[0] == 'wex' and self.cast[1] == 'wex' and self.cast[
            2] == 'exort' and self.spell != self.alacrity:
            return self.alacrity
        elif self.cast[0] == 'wex' and self.cast[1] == 'exort' and self.cast[
            2] == 'wex' and self.spell != self.alacrity:
            return self.alacrity
        elif self.cast[0] == 'exort' and self.cast[1] == 'wex' and self.cast[
            2] == 'wex' and self.spell != self.alacrity:
            return self.alacrity

        elif self.cast[0] == 'exort' and self.cast[1] == 'exort' and self.cast[
            2] == 'wex' and self.spell != self.meteor:
            return self.meteor
        elif self.cast[0] == 'wex' and self.cast[1] == 'exort' and self.cast[
            2] == 'exort' and self.spell != self.meteor:
            return self.meteor
        elif self.cast[0] == 'exort' and self.cast[1] == 'wex' and self.cast[
            2] == 'exort' and self.spell != self.meteor:
            return self.meteor

        elif self.cast[0] == 'exort' and self.cast[1] == 'exort' and self.cast[
            2] == 'quas' and self.spell != self.forge:
            return self.forge
        elif self.cast[0] == 'quas' and self.cast[1] == 'exort' and self.cast[
            2] == 'exort' and self.spell != self.forge:
            return self.forge
        elif self.cast[0] == 'exort' and self.cast[1] == 'quas' and self.cast[
            2] == 'exort' and self.spell != self.forge:
            return self.forge

        elif self.cast[0] == 'quas' and self.cast[1] == 'wex' and self.cast[2] == 'exort' and self.spell != self.blast:
            return self.blast
        elif self.cast[0] == 'quas' and self.cast[1] == 'exort' and self.cast[2] == 'wex' and self.spell != self.blast:
            return self.blast
        elif self.cast[0] == 'exort' and self.cast[1] == 'quas' and self.cast[2] == 'wex' and self.spell != self.blast:
            return self.blast
        elif self.cast[0] == 'exort' and self.cast[1] == 'wex' and self.cast[2] == 'quas' and self.spell != self.blast:
            return self.blast
        elif self.cast[0] == 'wex' and self.cast[1] == 'quas' and self.cast[2] == 'exort' and self.spell != self.blast:
            return self.blast
        elif self.cast[0] == 'wex' and self.cast[1] == 'exort' and self.cast[2] == 'quas' and self.spell != self.blast:
            return self.blast

    def run(self):
        while True:
            self.timer = Timer(duration=1000, repeat=True, on_update=None)
            self.timer.activate()
            self.timer_text = self.get_font(30).render(f'{self.timer.current_time()}', True, (0, 255, 0))
            self.window.blit(self.screen, (0, 0))
            self.screen.blit(self.backgrounds, (0, 0))
            self.window.blit(self.timer_text, self.timer_text.get_rect())
            draw.circle(self.screen, (0, 0, 0), (500, 400), 35)  # right
            draw.circle(self.screen, (0, 0, 0), (600, 400), 35)  # mid
            draw.circle(self.screen, (0, 0, 0), (700, 400), 35)  # left

            self.screen.blit(self.quas, (355, 455))
            self.screen.blit(self.wex, (455, 455))
            self.screen.blit(self.exort, (555, 455))
            self.screen.blit(self.invok, (939, 455))

            if self.x:
                self.screen.blit(self.x, (450, 200))  # top
            else:
                self.screen.blit(self.cube, (450, 200))
                self.screen.blit(self.cube, (650, 200))
            self.screen.blit(self.cube, (670, 450))
            self.screen.blit(self.cube, (800, 450))
            if self.spell:
                self.screen.blit(self.spell, (670, 450))
            if self.last_spell:
                self.screen.blit(self.last_spell, (800, 450))

            if self.sr1:
                self.screen.blit(self.sr1, (460, 360))
            if self.sr2:
                self.screen.blit(self.sr2, (560, 360))
            if self.sr3:
                self.screen.blit(self.sr3, (660, 360))

            display.update()

            for ev in event.get():
                if ev.type == QUIT:
                    exit()
                if ev.type == KEYDOWN:
                    if ev.key == K_q:
                        self.cast[0] = self.cast[1]
                        self.cast[1] = self.cast[2]
                        self.cast[2] = 'quas'
                        self.sr1 = self.sr2
                        self.sr2 = self.sr3
                        self.sr3 = self.quas_r

                    if ev.key == K_w:
                        self.cast[0] = self.cast[1]
                        self.cast[1] = self.cast[2]
                        self.cast[2] = 'wex'
                        self.sr1 = self.sr2
                        self.sr2 = self.sr3
                        self.sr3 = self.wex_r

                    if ev.key == K_e:
                        self.cast[0] = self.cast[1]
                        self.cast[1] = self.cast[2]
                        self.cast[2] = 'exort'
                        self.sr1 = self.sr2
                        self.sr2 = self.sr3
                        self.sr3 = self.exort_r

                    if ev.key == K_r:
                        sp = self.spells()
                        if sp:
                            self.last_spell, self.spell = self.spell, sp

                    if ev.key == K_d:
                        self.x = self.spell

                    if ev.key == K_f:
                        self.x = self.last_spell


if __name__ == '__main__':
    main = Main()
    main.run()
