from pygame import *
from random import sample
import sys


class Timer:
    def __init__(self, repeat=False, start=False):
        self.repeat = repeat
        self.active = False
        self.start_time = 0
        self.time = 0
        if start:
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
        return self.time / 1000

    def update(self):
        if self.active:
            self.time = time.get_ticks() - self.start_time


class Main:
    def __init__(self):
        init()
        self.record = 9999
        self.cast = ['', '', '']
        self.sr1, self.sr2, self.sr3, self.spell, self.last_spell, self.x = None, None, None, None, None, None
        self.window = display.set_mode((1000, 700))
        self.screen = Surface((1000, 700))
        self.cube = Surface((100, 100))
        self.repeat_spell = []
        self.timer = Timer(start=False)

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
        self.combo_to_spell = {
            ('exort', 'exort', 'exort'): self.sunstrike,
            ('wex', 'wex', 'wex'): self.emp,
            ('quas', 'quas', 'quas'): self.coldsnap,

            ('quas', 'quas', 'wex'): self.ghostwalk,
            ('exort', 'quas', 'quas'): self.icewall,
            ('quas', 'wex', 'wex'): self.tornado,

            ('exort', 'wex', 'wex'): self.alacrity,
            ('exort', 'exort', 'wex'): self.meteor,
            ('exort', 'exort', 'quas'): self.forge,

            ('exort', 'quas', 'wex'): self.blast,
        }

    def get_font(self, size):
        return font.SysFont("freesanbold.ttf", size)

    def rand_spell(self):
        spell_list = [self.sunstrike, self.emp, self.coldsnap, self.blast, self.forge, self.ghostwalk, self.icewall, self.meteor, self.tornado,
                      self.alacrity]
        self.repeat_spell.extend(sample(spell_list, 5))

    def spells(self):
        if '' in self.cast:
            return None
        key = tuple(sorted(self.cast))
        result = self.combo_to_spell.get(key)
        if result and result != self.spell:
            return result
        return None

    def start_game(self):
        self.timer.activate()
        self.rand_spell()

    def start_screen(self):
        while True:
            self.window.blit(self.screen, (0, 0))
            draw.rect(self.screen, (0, 0, 0), (0, 0, 1000, 700))
            text = self.get_font(50).render('Нажмите пробел, чтобы начать игру', 1, (0, 255, 0))
            text_rect = text.get_rect()
            text_rect.center = (500, 250)
            self.screen.blit(text, text_rect)
            display.update()
            for ev in event.get():
                if ev.type == QUIT:
                    quit()
                    sys.exit()
                if ev.type == KEYDOWN:
                    if ev.key == K_SPACE:
                        main.run()

    def end_screen(self):
        while True:
            self.window.blit(self.screen, (0, 0))
            draw.rect(self.screen, (0, 0, 0), (0, 0, 1000, 700))
            text = self.get_font(50).render('Нажмите любую клавишу, чтобы начать заново', 1, (0, 255, 0))
            text_rect = text.get_rect()
            text_rect.center = (500, 300)
            text2 = self.get_font(50).render(f'Ваш счёт: {self.timer.current_time()}', 1, (0, 255, 0))
            text2_rect = text2.get_rect()
            text2_rect.center = (500, 250)
            self.record = min(self.record, self.timer.current_time())
            text3 = self.get_font(50).render(f'Ваш рекорд: {self.record}', 1, (0, 255, 0))
            text3_rect = text3.get_rect()
            text3_rect.center = (475, 200)
            self.screen.blit(text, text_rect)
            self.screen.blit(text2, text2_rect)
            self.screen.blit(text3, text3_rect)
            display.update()
            for ev in event.get():
                if ev.type == QUIT:
                    quit()
                    sys.exit()
                if ev.type == KEYDOWN:
                    return
            display.update()

    def reset(self):
        self.cast = ['', '', '']
        self.sr1, self.sr2, self.sr3, self.spell, self.last_spell, self.x = None, None, None, None, None, None
        self.repeat_spell.clear()

    def run(self):
        while True:
            self.window.blit(self.screen, (0, 0))
            self.screen.blit(self.backgrounds, (0, 0))
            self.timer.update()
            self.timer_text = self.get_font(30).render(f'{self.timer.current_time()}', True, (0, 255, 0))
            self.screen.blit(self.timer_text, self.timer_text.get_rect())

            draw.circle(self.screen, (0, 0, 0), (400, 400), 35)  # right
            draw.circle(self.screen, (0, 0, 0), (500, 400), 35)  # mid
            draw.circle(self.screen, (0, 0, 0), (600, 400), 35)  # left

            self.screen.blit(self.quas, (100, 550))
            self.screen.blit(self.wex, (225, 550))
            self.screen.blit(self.exort, (350, 550))
            self.screen.blit(self.invok, (800, 550))

            self.screen.blit(self.cube, (300, 200))
            self.screen.blit(self.cube, (600, 200))
            if self.x:
                self.screen.blit(self.x, (300, 200))  # top left
            if self.repeat_spell:
                self.screen.blit(self.repeat_spell[0], (600, 200))  # top right

            self.screen.blit(self.cube, (500, 550))
            self.screen.blit(self.cube, (650, 550))
            if self.spell:
                self.screen.blit(self.spell, (500, 550))
            if self.last_spell:
                self.screen.blit(self.last_spell, (650, 550))

            if self.sr1:
                self.screen.blit(self.sr1, (360, 360))
            if self.sr2:
                self.screen.blit(self.sr2, (460, 360))
            if self.sr3:
                self.screen.blit(self.sr3, (560, 360))

            if len(self.repeat_spell) > 5:
                self.screen.blit(self.repeat_spell[5], (700, 50))
            if len(self.repeat_spell) > 4:
                self.screen.blit(self.repeat_spell[4], (575, 50))
            if len(self.repeat_spell) > 3:
                self.screen.blit(self.repeat_spell[3], (450, 50))
            if len(self.repeat_spell) > 2:
                self.screen.blit(self.repeat_spell[2], (325, 50))
            if len(self.repeat_spell) > 1:
                self.screen.blit(self.repeat_spell[1], (200, 50))

            display.update()

            for ev in event.get():
                if ev.type == QUIT:
                    quit()
                    sys.exit()
                if ev.type == KEYDOWN:
                    if ev.key == K_q:
                        self.cast[0] = self.cast[1]
                        self.cast[1] = self.cast[2]
                        self.cast[2] = 'quas'
                        self.sr1 = self.sr2
                        self.sr2 = self.sr3
                        self.sr3 = self.quas_r
                        if not self.timer.active:
                            self.start_game()

                    if ev.key == K_w:
                        self.cast[0] = self.cast[1]
                        self.cast[1] = self.cast[2]
                        self.cast[2] = 'wex'
                        self.sr1 = self.sr2
                        self.sr2 = self.sr3
                        self.sr3 = self.wex_r
                        if not self.timer.active:
                            self.start_game()

                    if ev.key == K_e:
                        self.cast[0] = self.cast[1]
                        self.cast[1] = self.cast[2]
                        self.cast[2] = 'exort'
                        self.sr1 = self.sr2
                        self.sr2 = self.sr3
                        self.sr3 = self.exort_r
                        if not self.timer.active:
                            self.start_game()

                    if ev.key == K_r:
                        sp = self.spells()
                        if sp:
                            self.last_spell, self.spell = self.spell, sp

                    if ev.key == K_d:
                        self.x = self.spell
                        if len(self.repeat_spell) > 0:
                            if self.x == self.repeat_spell[0]:
                                self.repeat_spell.remove(self.repeat_spell[0])
                            if len(self.repeat_spell) == 0:
                                self.timer.deactivate()
                                self.reset()
                                main.end_screen()
                                return

                    if ev.key == K_f:
                        self.x = self.last_spell
                        if len(self.repeat_spell) > 0:
                            if self.x == self.repeat_spell[0]:
                                self.repeat_spell.remove(self.repeat_spell[0])
                            if len(self.repeat_spell) == 0:
                                self.timer.deactivate()
                                self.reset()
                                main.end_screen()
                                return


if __name__ == '__main__':
    main = Main()
    main.start_screen()
