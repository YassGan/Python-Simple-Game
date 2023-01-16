import pygame
import random


pygame.init()
i = 0
testcoda = 0
teststart = 1
testloose = 0
clock = pygame.time.Clock()
jj = 0
b = 0
enmot = 3
testplayagain = 0
test2 = 0
testwin = 0
win = 0
winn = 2
testtextpause = 0
shootloop = 0
speed = 11
dspeed = 11
masse = 1
dmasse = 1
# Constant Variables
WIDTH = 1350
HEIGHT = 780
RUN = True
FPS = 23
DHARBA = 0
lagm = 3
numberofhseb = 7
kk = 0
secondpath = 400
# Initializing the display
DS = pygame.display.set_mode((WIDTH, HEIGHT))
bg = pygame.image.load(
    'C:/Users/yacin/OneDrive/Bureau/Player Charachter Frames/1bg2.jpg').convert()
hh = 75
ss = pygame.image.load(
    'C:/Users/yacin/OneDrive/Bureau/Player Charachter Frames/ss.png')

firewoosh = pygame.mixer.Sound(
    "C:/Users/yacin/OneDrive/Bureau/Player Charachter Frames/firewoosh1.wav")

hitt = pygame.mixer.Sound(
    "C:/Users/yacin/OneDrive/Bureau/Player Charachter Frames/hitt.wav")

KILL = pygame.mixer.Sound(
    "C:/Users/yacin/OneDrive/Bureau/Player Charachter Frames/killl.wav")
directed = pygame.mixer.music.load(
    "C:/Users/yacin/OneDrive/Bureau/Player Charachter Frames/directed.wav")
# event quiting action


def damagedcodat():
    if testcoda == 1:
        damagedcoda.play()
        testcoda = 0


def eventquiting():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            RUN = False
            pygame.quit()


class Player(object):
    walkRight = [pygame.image.load('C:/Users/yacin/OneDrive/Bureau/Player Charachter Frames/R1.png'), pygame.image.load('C:/Users/yacin/OneDrive/Bureau/Player Charachter Frames/R2.png'), pygame.image.load('C:/Users/yacin/OneDrive/Bureau/Player Charachter Frames/R3.png'), pygame.image.load('C:/Users/yacin/OneDrive/Bureau/Player Charachter Frames/R4.png'), pygame.image.load(
        'C:/Users/yacin/OneDrive/Bureau/Player Charachter Frames/R5.png'), pygame.image.load('C:/Users/yacin/OneDrive/Bureau/Player Charachter Frames/R6.png')]
    walkLeft = [pygame.image.load('C:/Users/yacin/OneDrive/Bureau/Player Charachter Frames/L1.png'), pygame.image.load('C:/Users/yacin/OneDrive/Bureau/Player Charachter Frames/L2.png'), pygame.image.load('C:/Users/yacin/OneDrive/Bureau/Player Charachter Frames/L3.png'), pygame.image.load('C:/Users/yacin/OneDrive/Bureau/Player Charachter Frames/L4.png'), pygame.image.load(
        'C:/Users/yacin/OneDrive/Bureau/Player Charachter Frames/L5.png'), pygame.image.load('C:/Users/yacin/OneDrive/Bureau/Player Charachter Frames/L6.png')]

    def __init__(self, x, y, vel):
        self.x = x
        self.y = y
        self.vel = vel
        self.walkcount = 0
        self.Left = False
        self.Right = False
        self.press = 1
        self.hitbox = (self.x, self.y, self.x+45, self.y+50)
        self.visible = True
        self.moving = True
        self.sens = 1
        self.aller = 0
        self.jump = False
        self.j = 7

    def move(self):
        if self.visible:
            if self.moving:
                if self.walkcount >= 11:
                    self.walkcount = 0
                if self.Right and self.x < WIDTH-50:
                    self.walkcount += 1
                    self.x += self.vel
                if self.Left and self.x > 0:
                    self.walkcount += 1
                    self.x -= self.vel

    def draw(self, DS):
        global kk, hh
        if self.visible:
            if self.Right:
                DS.blit(self.walkRight[self.walkcount//2], (self.x, self.y))
            if self.Left:
                DS.blit(self.walkLeft[self.walkcount//2], (self.x, self.y))
            if self.press == 1 and self.Right == False and self.Left == False:
                DS.blit(self.walkRight[0], (self.x, self.y))
            if self.press == 0 and self.Right == False and self.Left == False:
                DS.blit(self.walkLeft[0], (self.x, self.y))

            self.hitbox = (self.x, self.y+25, 45, 95)

            pygame.draw.rect(DS, (255, 0, 50), (self.x-12, self.y, 75, 15))
            pygame.draw.rect(DS, (0, 255, 0),
                             (self.x-12, self.y, hh, 15))
            #pygame.draw.rect(DS, (25, 5, 7), self.hitbox, 2)


def keyboard_presses(Player):
    global shootloop
    global lagm
    shootloop += 1
    if shootloop >= 3:
        shootloop = 0
    keys = pygame.key.get_pressed()

    if keys[pygame.K_RIGHT]:
        Player.Left = False
        Player.Right = True
        Player.press = 1
        Player.sens = 1
    if keys[pygame.K_LEFT]:
        Player.Left = True
        Player.Right = False
        Player.press = 0
        Player.sens = -1
    if keys[pygame.K_SPACE]:
        if shootloop == 0 and len(cratache) < lagm and test == 0:
            firewoosh.play()
            Player.aller = 1
            flamme = pygame.image.load(
                'C:/Users/yacin/OneDrive/Bureau/Player Charachter Frames/s1.png')
            if Player.Left:
                projectile.sense = -1
            if Player.Right:
                projectile.sense = 1
            if Player.sens == 1:
                cratache.append(projectile(
                    yassine.x, yassine.y+40, 6, yassine.sens))
            if Player.sens == -1:
                cratache.append(projectile(
                    yassine.x-30, yassine.y+40, 6, yassine.sens))
    if keys[pygame.K_s]:
        Player.jump = True


def do_jump(Player):
    global masse
    global dmasse
    global speed
    global dspeed
    if Player.jump:
        f = 0.5*masse*(speed**2)
        Player.y -= f
        speed = speed-1
        if speed < 0:
            masse = -dmasse
        if speed == -(dspeed+1):
            Player.jump = False
            speed = dspeed
            masse = dmasse


def keyboard_ini(Player):
    keys = pygame.key.get_pressed()
    if keys[pygame.K_RIGHT]:
        Player.Left = False
        Player.Right = False
    if keys[pygame.K_LEFT]:
        Player.Left = False
        Player.Right = False
    if keys[pygame.K_UP]:
        Player.y -= 5
    if keys[pygame.K_DOWN]:
        Player.y += 5


class flamme():
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.hitbox = (self.x+15, self.y, 38, 70)
        self.flamme = pygame.image.load(
            'C:/Users/yacin/OneDrive/Bureau/Player Charachter Frames/s1.png')
        self.flammemoving = [pygame.image.load('C:/Users/yacin/OneDrive/Bureau/Fire moving/1.png'), pygame.image.load('C:/Users/yacin/OneDrive/Bureau/Fire moving/2.png'), pygame.image.load(
            'C:/Users/yacin/OneDrive/Bureau/Fire moving/3.png'), pygame.image.load('C:/Users/yacin/OneDrive/Bureau/Fire moving/4.png'), pygame.image.load('C:/Users/yacin/OneDrive/Bureau/Fire moving/5.png'), pygame.image.load('C:/Users/yacin/OneDrive/Bureau/Fire moving/6.png'), pygame.image.load('C:/Users/yacin/OneDrive/Bureau/Fire moving/7.png'), pygame.image.load(
            'C:/Users/yacin/OneDrive/Bureau/Fire moving/8.png'), pygame.image.load('C:/Users/yacin/OneDrive/Bureau/Fire moving/9.png'), pygame.image.load('C:/Users/yacin/OneDrive/Bureau/Fire moving/10.png')]
        self.flammeb = pygame.image.load(
            'C:/Users/yacin/OneDrive/Bureau/Player Charachter Frames/blue.png')

    def draw(self, DS):
       # DS.blit(self.flamme, (yassine.x+59, yassine.y+25))
        # DS.blit(self.flammeb, (yassine.x+259, yassine.y+25))

        DS.blit(self.flammemoving[i], (self.x, self.y))
        #pygame.draw.rect(DS, (55, 2, 44), self.hitbox, 2)


def firehit():
    if (yassine.x+31 > fl.x and yassine.x+45 < fl.x+45 and yassine.y+130 >= fl.y) or (yassine.y+115 >= fl.y and yassine.x > fl.x and yassine.x-5 < fl.x+45):
        print("hhjhjhjhhj")
        print(j)
        if yassine.Right:
            right = 1
        if yassine.Left:
            right = 0
        yassine.visible = False
        frappe = pygame.image.load(
            'C:/Users/yacin/OneDrive/Bureau/Player Charachter Frames/frappe.png')
        frappeg = pygame.image.load(
            'C:/Users/yacin/OneDrive/Bureau/Player Charachter Frames/frappeg.png')
        hit = pygame.image.load(
            'C:/Users/yacin/OneDrive/Bureau/Player Charachter Frames/hit.png')
        if yassine.sens == 1:
            DS.blit(frappe, (yassine.x+19, yassine.y))
        if yassine.sens == -1:
            DS.blit(frappeg, (yassine.x-19, yassine.y))


class projectile(Player):
    def __init__(self, x, y, vel, sense):
        self.x = x
        self.y = y
        self.vel = vel
        self.hitbox = (self.x+10, self.y+20, 50, 30)
        self.sense = sense

    def move(self):
        self.x += (self.vel*self.sense)

    def draw(self, DS):
        if self.sense == 1:
            flamme = pygame.image.load(
                'C:/Users/yacin/OneDrive/Bureau/Player Charachter Frames/s1.png')
            self.hitbox = (self.x+10, self.y+20, 50, 30)
            #pygame.draw.rect(DS, (2, 6, 4), self.hitbox, 1)
            DS.blit(flamme, (self.x, self.y))
        if self.sense == -1:
            flammeL = pygame.image.load(
                'C:/Users/yacin/OneDrive/Bureau/Player Charachter Frames/s1L.png')
            self.hitbox = (self.x+10, self.y+20, 50, 30)
            #pygame.draw.rect(DS, (2, 6, 4), self.hitbox, 1)
            DS.blit(flammeL, (self.x, self.y))


class blueprojectile():
    def __init__(self, x, y, vel, sense):
        self.x = x
        self.y = y
        self.vel = vel
        self.hitbox = (self.x+10, self.y+20, 50, 30)
        self.sense = sense

    def move(self):
        self.x += (self.vel*self.sense)

    def draw(self, DS):
        if self.sense == 1:
            flammeblue = pygame.image.load(
                'C:/Users/yacin/OneDrive/Bureau/Player Charachter Frames/blue.png')
            self.hitbox = (self.x+10, self.y+20, 50, 30)
            #pygame.draw.rect(DS, (2, 6, 4), self.hitbox, 1)
            DS.blit(flammeblue, (self.x, self.y))
        if self.sense == -1:
            flammeblueg = pygame.image.load(
                'C:/Users/yacin/OneDrive/Bureau/Player Charachter Frames/blueg.png')
            self.hitbox = (self.x+10, self.y+20, 50, 30)
            #pygame.draw.rect(DS, (2, 6, 4), self.hitbox, 1)
            DS.blit(flammeblueg, (self.x, self.y))


class enemy():
    global secondpath
    wwalkRight = [pygame.image.load('C:/Users/yacin/OneDrive/Bureau/Player Charachter Frames/R1E.png'), pygame.image.load('C:/Users/yacin/OneDrive/Bureau/Player Charachter Frames/R2E.png'), pygame.image.load('C:/Users/yacin/OneDrive/Bureau/Player Charachter Frames/R3E.png'), pygame.image.load('C:/Users/yacin/OneDrive/Bureau/Player Charachter Frames/R4E.png'), pygame.image.load('C:/Users/yacin/OneDrive/Bureau/Player Charachter Frames/R5E.png'), pygame.image.load(
        'C:/Users/yacin/OneDrive/Bureau/Player Charachter Frames/R6E.png'), pygame.image.load('C:/Users/yacin/OneDrive/Bureau/Player Charachter Frames/R7E.png')]
    wwalkLeft = [pygame.image.load('C:/Users/yacin/OneDrive/Bureau/Player Charachter Frames/L1E.png'), pygame.image.load('C:/Users/yacin/OneDrive/Bureau/Player Charachter Frames/L2E.png'), pygame.image.load('C:/Users/yacin/OneDrive/Bureau/Player Charachter Frames/L3E.png'), pygame.image.load('C:/Users/yacin/OneDrive/Bureau/Player Charachter Frames/L4E.png'), pygame.image.load('C:/Users/yacin/OneDrive/Bureau/Player Charachter Frames/L5E.png'), pygame.image.load(
        'C:/Users/yacin/OneDrive/Bureau/Player Charachter Frames/L6E.png'), pygame.image.load('C:/Users/yacin/OneDrive/Bureau/Player Charachter Frames/L7E.png')]

    def __init__(self, x, y, vel):
        self.x = x
        self.y = y
        self.vel = vel
        self.walkcount = 0
        self.trajet = [x, x+secondpath]
        self.aller = False
        self.retour = False
        self.hitbox = (self.x, self.y, 44, 85)
        self.fire = False
        self.sens = 0
        self.hseb = 0
        self.visible = True
        self.j = 10
        self.kk = 0
        self.hh = 75
        self.n = 0

    def move(self):
        global numberofhseb
        if self.visible:
            if self.walkcount >= 11:
                self.walkcount = 0
                self.hseb += 1
                if self.hseb == numberofhseb:
                    self.fire = True
                    self.hseb = 0

            if self.x <= self.trajet[0]:
                self.aller = True
                self.retour = False
            if self.x >= self.trajet[1]:
                self.aller = False
                self.retour = True
            if self.aller:
                self.x += self.vel
            if self.retour:
                self.x -= self.vel

    def firing(self):
        if self.visible:
            if self.fire and len(cratacheblue) < 2:
                flamme = pygame.image.load(
                    'C:/Users/yacin/OneDrive/Bureau/Player Charachter Frames/s1.png')
                if self.retour:
                    self.sens = -1
                    cratacheblue.append(blueprojectile(
                        self.x, self.y+40, 6, self.sens))
                if self.aller:
                    self.sens = 1
                    cratacheblue.append(blueprojectile(
                        self.x-30, self.y+40, 6, self.sens))
                self.fire = False

    def draw(self, DS):
        if self.visible:
            if self.aller:
                DS.blit(self.wwalkRight[self.walkcount//2], (self.x, self.y))
                self.walkcount += 1
            if self.retour:
                DS.blit(self.wwalkLeft[self.walkcount//2], (self.x, self.y))
                self.walkcount += 1
            self.hitbox = (self.x+20, self.y+25, 40, 95)
            pygame.draw.rect(DS, (255, 0, 50), (self.x, self.y, 75, 15))
            pygame.draw.rect(DS, (0, 255, 0), (self.x, self.y, self.hh, 15))
            #pygame.draw.rect(DS, (25, 5, 7), self.hitbox, 2)
            #pygame.draw.rect(DS, (45, 55, 5), self.hitbox, 2)


"""
def playagain():
    global testplayagain
    if testplayagain==1:
        testplayagain=0
"""


# MAIN LOOP
# Declaring the diffrent varibles

enemies = []
thief = enemy(400, 600, 5)
thief2 = enemy(160, 600, 8)

enemies.append(thief)
enemies.append(thief2)
yassine = Player(2, 600, 8)
# fl = flamme(250, 640)
i = 0
j = False
shootloop = 0
score = 0
flammes = []
# fl1 = flamme(50, 640)
fl2 = flamme(250, 640)
flammes.append(flamme(850, 640))
flammes.append(fl2)
flammes.append(flamme(500, 640))
cratache = []
cratacheblue = []

font = pygame.font.SysFont("comicsacans", 40)
fontt = pygame.font.SysFont("comicsacans", 40)
fonttt = pygame.font.SysFont("comicsacans", 110)
textwin = fonttt.render("You Win ", 1, (0, 67, 22))
textloose2 = fonttt.render("GAME  OVER", 1, (50, 0, 0))
textloose = fonttt.render("  You Loose ", 1, (0, 67, 22))


test = 0
testtextpause = 0
pygame.mixer.music.play(-1)
while RUN:
    j = 0
    keys = pygame.key.get_pressed()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            RUN = False
            pygame.quit()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_g:
                test = 1
                testtextpause = 1
            if event.key == pygame.K_h:
                test = 0
                testtextpause = 0
            if event.key == pygame.K_e:
                teststart = 0
                test = 0

    if test == 1:
        i = 0
        for en in enemies:
            en.walkcount = 0
            if en.retour:
                en.x = en.x+en.vel
            if en.aller:
                en.x = en.x-en.vel
        for c in cratacheblue:
            c.x -= (c.vel*c.sense)
        for cc in cratache:
            cc.x -= (cc.vel*cc.sense)
        yassine.moving = False

    if test2 == 1:
        i = 0
        for en in enemies:
            en.walkcount = 0
            if en.retour:
                en.x = en.x+en.vel
            if en.aller:
                en.x = en.x-en.vel
        for c in cratacheblue:
            c.x -= (c.vel*c.sense)
        for cc in cratache:
            cc.x -= (cc.vel*cc.sense)
        yassine.moving = False

        # pygame.time.delay(100)
    print(j)
    if keys[pygame.K_h]:
        test = 0
        print("ggggggggggggggggggggggggggggggggggggggggggggggggggggg")
        print(test)

    if len(enemies) <= winn and win <= winn:
        enemies.append(enemy(random.randint(0, yassine.x+50),
                             600, random.randint(4, 13)))

    text = font.render("Score : "+str(score), 1, (0, 67, 22))
    kk = 0
    thiefhitg = pygame.image.load(
        "C:/Users/yacin/OneDrive/Bureau/Player Charachter Frames/thiefhitg.png")
    thiefhit = pygame.image.load(
        "C:/Users/yacin/OneDrive/Bureau/Player Charachter Frames/thiefhit.png")
    frappe = pygame.image.load(
        'C:/Users/yacin/OneDrive/Bureau/Player Charachter Frames/frappe.png')
    frappeg = pygame.image.load(
        'C:/Users/yacin/OneDrive/Bureau/Player Charachter Frames/frappeg.png')
    hit = pygame.image.load(
        'C:/Users/yacin/OneDrive/Bureau/Player Charachter Frames/hit.png')

    if test == 0:
        i += 1
        if i > 9:
            i = 0
    DS.blit(bg, (0, 0))
    # fl.draw(DS)

    for nar in flammes:
        nar.draw(DS)
        if (yassine.x+31 > nar.x and yassine.x+45 < nar.x+45 and yassine.y+130 >= nar.y) or (yassine.y+115 >= nar.y and yassine.x > nar.x and yassine.x-5 < nar.x+45):
            print("hhjhjhjhhj")
            print(j)
            if yassine.Right:
                right = 1
            if yassine.Left:
                right = 0
            yassine.visible = False
            if yassine.sens == 1:
                DS.blit(frappe, (yassine.x, yassine.y))
            if yassine.sens == -1:
                DS.blit(frappeg, (yassine.x, yassine.y))
            testloose = 1
            yassine.j = 0

    print(yassine.j)

    do_jump(yassine)
    # firehit()

    for hahi in cratache:
        hahi.move()
        hahi.draw(DS)
        if hahi.x > WIDTH or hahi.x < 0:
            cratache.pop(cratache.index(hahi))
    for bb in cratacheblue:
        bb.move()
        bb.draw(DS)
        if bb.x > WIDTH or bb.x < 0:
            cratacheblue.pop(cratacheblue.index(bb))
    if len(enemies) == 0:
        testwin = 1

    for en in enemies:
        en.move()
        en.draw(DS)
        en.firing()

    for hahi in cratache:
        for en in enemies:
            print(en.x)
            if (hahi.hitbox[0]+31 > en.x and hahi.hitbox[0]+45 < en.hitbox[0]+45) or (hahi.hitbox[0] > en.hitbox[0] and hahi.hitbox[0]-5 < en.hitbox[0]+45) and (en.n == 0):
                print("jhskjhfkjfh")
                try:
                    cratache.pop(cratache.index(hahi))
                except ValueError:
                    print("value error")
                if en.aller:
                    DS.blit(thiefhitg, (en.x, en.y))
                if en.retour:
                    DS.blit(thiefhit, (en.x, en.y))
                if en.j > 1:
                    en.j -= 1
                en.kk = 75//en.j
                en.hh = en.hh-en.kk
                if en.hh <= 0:
                    en.hh = 2
                if en.hh <= 2:
                    en.visible = False
                    en.n = 1
                print(en.visible)
                score += 1
                if en.j == enmot:
                    try:
                        enemies.pop(enemies.index(en))
                        KILL.play()
                        win += 1
                    except ValueError:
                        pass

            for bb in cratacheblue:
                if (hahi.hitbox[0]+31 > bb.x and hahi.hitbox[0]+45 < bb.hitbox[0]+45) or (hahi.hitbox[0] > bb.hitbox[0] and hahi.hitbox[0]-5 < bb.hitbox[0]+45):
                    try:
                        cratacheblue.pop(cratacheblue.index(bb))
                        cratache.pop(cratache.index(hahi))
                    except ValueError:
                        print("value error")

    for bb in cratacheblue:
        if (bb.hitbox[0]+31 > yassine.x and bb.hitbox[0]+31 < yassine.hitbox[0]+45 and yassine.hitbox[1]+130 >= bb.hitbox[1]) or (bb.hitbox[0] > yassine.hitbox[0] and bb.hitbox[0]-5 < yassine.hitbox[0]+45 and yassine.hitbox[1]+130 >= bb.hitbox[1]):
            print("ljklkj")
            hitt.play()
            cratacheblue.pop(cratacheblue.index(bb))
            DHARBA = yassine.sens
            if yassine.j > 1:
                yassine.j -= 1
            if yassine.j == 1:
                yassine.j = 1
            kk = 75//yassine.j
            hh = hh-kk
            if hh <= 0:
                hh = 2
            if hh == 2:
                testloose = 1
        # if fl.hitbox[0] < yassine.hitbox[0]+45 and fl.hitbox[0]+38 < yassine.hitbox[0]+45 and fl.hitbox[1] <= yassine.hitbox[1]+95:

    keyboard_presses(yassine)

    yassine.move()
    yassine.draw(DS)

    keyboard_ini(yassine)

    if DHARBA == 1:
        DS.blit(frappe, (yassine.x, yassine.y))
        print("hhhhhhhhhhhhhhhh")
        DHARBA = 0
    if DHARBA == -1:
        DS.blit(frappeg, (yassine.x, yassine.y))
        DHARBA = 0
    yassine.moving = True
    DS.blit(text, (1190, 20))
    if testtextpause == 1:
        pause = pygame.image.load(
            "C:/Users/yacin/OneDrive/Bureau/Player Charachter Frames/pause.png")
        DS.blit(pause, (0, 20))

    if testwin == 1:
        print("you win ")
        test2 = 1
        pygame.time.delay(100)
        DS.blit(textwin, (WIDTH/2-150, 300))
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                pygame.quit()
            if event.type == pygame.QUIT:
                pygame.quit()

    if testloose == 1:
        if yassine.sens == 1:
            DS.blit(frappe, (yassine.x, yassine.y))
            yassine.visible = False
        if yassine.sens == -1:
            DS.blit(frappeg, (yassine.x, yassine.y))
            yassine.visible = False
        print("you loose ")
        testcoda = 1
        test2 = 1
        pygame.time.delay(100)
        DS.blit(textloose2, (WIDTH/2-190, 250))
        DS.blit(textloose, (WIDTH/2-190, 350))
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                pygame.quit()
            if event.type == pygame.QUIT:
                pygame.quit()

    if teststart == 1:
        test = 1
        DS.blit(ss, (300, 50))

    print(testwin)
    print(teststart)
    # eventquiting()
    pygame.display.update()
    pygame.time.delay(FPS)
