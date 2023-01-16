import pygame
pygame.init()
FPS = 25
win = pygame.display.set_mode((1350, 780))
pygame.display.set_caption("First Game")


gaming = True

"""
walkRight = [pygame.image.load('C:/Users/yacin/OneDrive/Bureau/Player Charachter Frames/R1.png'), pygame.image.load('C:/Users/yacin/OneDrive/Bureau/Player Charachter Frames/R2.png'), pygame.image.load('C:/Users/yacin/OneDrive/Bureau/Player Charachter Frames/R3.png'), pygame.image.load('C:/Users/yacin/OneDrive/Bureau/Player Charachter Frames/R4.png'), pygame.image.load(
    'C:/Users/yacin/OneDrive/Bureau/Player Charachter Frames/R5.png'), pygame.image.load('C:/Users/yacin/OneDrive/Bureau/Player Charachter Frames/R6.png'), pygame.image.load('C:/Users/yacin/OneDrive/Bureau/Player Charachter Frames/R7.png'), pygame.image.load('C:/Users/yacin/OneDrive/Bureau/Player Charachter Frames/R8.png'), pygame.image.load('C:/Users/yacin/OneDrive/Bureau/Player Charachter Frames/R9.png')]
walkLeft = [pygame.image.load('C:/Users/yacin/OneDrive/Bureau/Player Charachter Frames/L1.png'), pygame.image.load('C:/Users/yacin/OneDrive/Bureau/Player Charachter Frames/L2.png'), pygame.image.load('C:/Users/yacin/OneDrive/Bureau/Player Charachter Frames/L3.png'), pygame.image.load('C:/Users/yacin/OneDrive/Bureau/Player Charachter Frames/L4.png'), pygame.image.load(
    'C:/Users/yacin/OneDrive/Bureau/Player Charachter Frames/L5.png'), pygame.image.load('C:/Users/yacin/OneDrive/Bureau/Player Charachter Frames/L6.png'), pygame.image.load('C:/Users/yacin/OneDrive/Bureau/Player Charachter Frames/L7.png'), pygame.image.load('C:/Users/yacin/OneDrive/Bureau/Player Charachter Frames/L8.png'), pygame.image.load('C:/Users/yacin/OneDrive/Bureau/Player Charachter Frames/L9.png')]


"""


wwalkRight = [pygame.image.load('C:/Users/yacin/OneDrive/Bureau/Player Charachter Frames/R1E.png'), pygame.image.load('C:/Users/yacin/OneDrive/Bureau/Player Charachter Frames/R2E.png'), pygame.image.load('C:/Users/yacin/OneDrive/Bureau/Player Charachter Frames/R3E.png'), pygame.image.load('C:/Users/yacin/OneDrive/Bureau/Player Charachter Frames/R4E.png'), pygame.image.load('C:/Users/yacin/OneDrive/Bureau/Player Charachter Frames/R5E.png'), pygame.image.load(
    'C:/Users/yacin/OneDrive/Bureau/Player Charachter Frames/R6E.png'), pygame.image.load('C:/Users/yacin/OneDrive/Bureau/Player Charachter Frames/R7E.png')]
wwalkLeft = [pygame.image.load('C:/Users/yacin/OneDrive/Bureau/Player Charachter Frames/L1E.png'), pygame.image.load('C:/Users/yacin/OneDrive/Bureau/Player Charachter Frames/L2E.png'), pygame.image.load('C:/Users/yacin/OneDrive/Bureau/Player Charachter Frames/L3E.png'), pygame.image.load('C:/Users/yacin/OneDrive/Bureau/Player Charachter Frames/L4E.png'), pygame.image.load('C:/Users/yacin/OneDrive/Bureau/Player Charachter Frames/L5E.png'), pygame.image.load(
    'C:/Users/yacin/OneDrive/Bureau/Player Charachter Frames/L6E.png'), pygame.image.load('C:/Users/yacin/OneDrive/Bureau/Player Charachter Frames/L7E.png')]


walkRight = [pygame.image.load('C:/Users/yacin/OneDrive/Bureau/Player Charachter Frames/R1.png'), pygame.image.load('C:/Users/yacin/OneDrive/Bureau/Player Charachter Frames/R2.png'), pygame.image.load('C:/Users/yacin/OneDrive/Bureau/Player Charachter Frames/R3.png'), pygame.image.load('C:/Users/yacin/OneDrive/Bureau/Player Charachter Frames/R4.png'), pygame.image.load(
    'C:/Users/yacin/OneDrive/Bureau/Player Charachter Frames/R5.png'), pygame.image.load('C:/Users/yacin/OneDrive/Bureau/Player Charachter Frames/R6.png')]
walkLeft = [pygame.image.load('C:/Users/yacin/OneDrive/Bureau/Player Charachter Frames/L1.png'), pygame.image.load('C:/Users/yacin/OneDrive/Bureau/Player Charachter Frames/L2.png'), pygame.image.load('C:/Users/yacin/OneDrive/Bureau/Player Charachter Frames/L3.png'), pygame.image.load('C:/Users/yacin/OneDrive/Bureau/Player Charachter Frames/L4.png'), pygame.image.load(
    'C:/Users/yacin/OneDrive/Bureau/Player Charachter Frames/L5.png'), pygame.image.load('C:/Users/yacin/OneDrive/Bureau/Player Charachter Frames/L6.png')]


"""
walkRight = [pygame.image.load('C:/Users/yacin/OneDrive/Bureau/Player Charachter Frames/R1.png'), pygame.image.load('C:/Users/yacin/OneDrive/Bureau/Player Charachter Frames/R2.png'), pygame.image.load('C:/Users/yacin/OneDrive/Bureau/Player Charachter Frames/R3.png'), pygame.image.load('C:/Users/yacin/OneDrive/Bureau/Player Charachter Frames/R4.png'), pygame.image.load(
    'C:/Users/yacin/OneDrive/Bureau/Player Charachter Frames/R5.png'), pygame.image.load('C:/Users/yacin/OneDrive/Bureau/Player Charachter Frames/R6.png')]
walkLeft = [pygame.image.load('C:/Users/yacin/OneDrive/Bureau/Player Charachter Frames/L1.png'), pygame.image.load('C:/Users/yacin/OneDrive/Bureau/Player Charachter Frames/L2.png'), pygame.image.load('C:/Users/yacin/OneDrive/Bureau/Player Charachter Frames/L3.png'), pygame.image.load('C:/Users/yacin/OneDrive/Bureau/Player Charachter Frames/L4.png'), pygame.image.load(
    'C:/Users/yacin/OneDrive/Bureau/Player Charachter Frames/L5.png'), pygame.image.load('C:/Users/yacin/OneDrive/Bureau/Player Charachter Frames/L6.png')]
"""


bg = pygame.image.load(
    'C:/Users/yacin/OneDrive/Bureau/Player Charachter Frames/1bg2.jpg').convert()
# bg = pygame.transform.scale(bg, (1400, 820))
char = pygame.image.load(
    'C:/Users/yacin/OneDrive/Bureau/Player Charachter Frames/jumping.png')

clock = pygame.time.Clock()

sio = pygame.image.load(
    'C:/Users/yacin/OneDrive/Bureau/Player Charachter Frames/flamme.png').convert()


class player(object):
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.vel = 10
        self.isJump = False
        self.left = False
        self.right = False
        self.walkCount = 0
        self.jumpCount = 10
        self.standing = True

    def draw(self, win):
        if self.walkCount + 1 >= 12:
            self.walkCount = 0

        if not(self.standing):
            if self.left:
                win.blit(walkLeft[self.walkCount//2], (self.x, self.y))
                self.walkCount += 1
            elif self.right:
                win.blit(walkRight[self.walkCount//2], (self.x, self.y))
                self.walkCount += 1
        else:
            if self.right:
                win.blit(walkRight[0], (self.x, self.y))
            else:
                win.blit(walkLeft[0], (self.x, self.y))


class projectile(object):
    def __init__(self, x, y, radius, color, facing):
        self.x = x
        self.y = y
        self.radius = radius
        self.color = color
        self.facing = facing
        self.vel = 8 * facing

    def draw(self, win):
        pygame.draw.circle(win, self.color, (self.x, self.y), self.radius)


"""
    walkRight = [pygame.image.load('C:/Users/yacin/OneDrive/Bureau/Player Charachter Frames/R1E.png'), pygame.image.load('C:/Users/yacin/OneDrive/Bureau/Player Charachter Frames/R2E.png'), pygame.image.load('C:/Users/yacin/OneDrive/Bureau/Player Charachter Frames/R3E.png'), pygame.image.load('C:/Users/yacin/OneDrive/Bureau/Player Charachter Frames/R4E.png'), pygame.image.load('C:/Users/yacin/OneDrive/Bureau/Player Charachter Frames/R5E.png'), pygame.image.load(
        'C:/Users/yacin/OneDrive/Bureau/Player Charachter Frames/R6E.png'), pygame.image.load('C:/Users/yacin/OneDrive/Bureau/Player Charachter Frames/R7E.png'), pygame.image.load('C:/Users/yacin/OneDrive/Bureau/Player Charachter Frames/R8E.png'), pygame.image.load('C:/Users/yacin/OneDrive/Bureau/Player Charachter Frames/R9E.png'), pygame.image.load('C:/Users/yacin/OneDrive/Bureau/Player Charachter Frames/R10E.png'), pygame.image.load('C:/Users/yacin/OneDrive/Bureau/Player Charachter Frames/R11E.png')]
    walkLeft = [pygame.image.load('C:/Users/yacin/OneDrive/Bureau/Player Charachter Frames/L1E.png'), pygame.image.load('C:/Users/yacin/OneDrive/Bureau/Player Charachter Frames/L2E.png'), pygame.image.load('C:/Users/yacin/OneDrive/Bureau/Player Charachter Frames/L3E.png'), pygame.image.load('C:/Users/yacin/OneDrive/Bureau/Player Charachter Frames/L4E.png'), pygame.image.load('C:/Users/yacin/OneDrive/Bureau/Player Charachter Frames/L5E.png'), pygame.image.load(
        'C:/Users/yacin/OneDrive/Bureau/Player Charachter Frames/L6E.png'), pygame.image.load('C:/Users/yacin/OneDrive/Bureau/Player Charachter Frames/L7E.png'), pygame.image.load('C:/Users/yacin/OneDrive/Bureau/Player Charachter Frames/L8E.png'), pygame.image.load('C:/Users/yacin/OneDrive/Bureau/Player Charachter Frames/L9E.png'), pygame.image.load('C:/Users/yacin/OneDrive/Bureau/Player Charachter Frames/L10E.png'), pygame.image.load('C:/Users/yacin/OneDrive/Bureau/Player Charachter Frames/L11E.png')]


"""


class enemy(object):
    walkRight = [pygame.image.load('C:/Users/yacin/OneDrive/Bureau/Player Charachter Frames/R1E.png'), pygame.image.load('C:/Users/yacin/OneDrive/Bureau/Player Charachter Frames/R2E.png'), pygame.image.load('C:/Users/yacin/OneDrive/Bureau/Player Charachter Frames/R3E.png'), pygame.image.load('C:/Users/yacin/OneDrive/Bureau/Player Charachter Frames/R4E.png'), pygame.image.load('C:/Users/yacin/OneDrive/Bureau/Player Charachter Frames/R5E.png'), pygame.image.load(
        'C:/Users/yacin/OneDrive/Bureau/Player Charachter Frames/R6E.png'), pygame.image.load('C:/Users/yacin/OneDrive/Bureau/Player Charachter Frames/R7E.png')]
    walkLeft = [pygame.image.load('C:/Users/yacin/OneDrive/Bureau/Player Charachter Frames/L1E.png'), pygame.image.load('C:/Users/yacin/OneDrive/Bureau/Player Charachter Frames/L2E.png'), pygame.image.load('C:/Users/yacin/OneDrive/Bureau/Player Charachter Frames/L3E.png'), pygame.image.load('C:/Users/yacin/OneDrive/Bureau/Player Charachter Frames/L4E.png'), pygame.image.load('C:/Users/yacin/OneDrive/Bureau/Player Charachter Frames/L5E.png'), pygame.image.load(
        'C:/Users/yacin/OneDrive/Bureau/Player Charachter Frames/L6E.png'), pygame.image.load('C:/Users/yacin/OneDrive/Bureau/Player Charachter Frames/L7E.png')]

    def __init__(self, x, y, width, height, end):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.path = [x, end]
        self.walkCount = 0
        self.vel = 6

    def draw(self, win):
        self.move()
        if self.walkCount + 1 >= 12:
            self.walkCount = 0

        if self.vel > 0:
            win.blit(self.walkRight[self.walkCount//3], (self.x, self.y))
            self.walkCount += 1
        else:
            win.blit(self.walkLeft[self.walkCount//3], (self.x, self.y))
            self.walkCount += 1

        win.blit(sio, (355, 332))

    def move(self):
        if self.vel > 0:
            if self.x < self.path[1] + self.vel:
                self.x += self.vel
            else:
                self.vel = self.vel * -1
                self.x += self.vel
                self.walkCount = 0
        else:
            if self.x > self.path[0] - self.vel:
                self.x += self.vel
            else:
                self.vel = self.vel * -1
                self.x += self.vel
                self.walkCount = 0


class flamme():

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def draw(self, win):
        win.blit(flame, (self.x, self.y))


def redrawGameWindow():
    win.blit(bg, (0, 0))

    man.draw(win)
    goblin.draw(win)
    global gaming
    if gaming == True:
        bg3 = pygame.image.load(
            'C:/Users/yacin/OneDrive/Bureau/Player Charachter Frames/ss.png')
        bg4 = pygame.image.load(
            'C:/Users/yacin/OneDrive/Bureau/Player Charachter Frames/aqq.png')
        win.blit(bg3, (280, 1))
        win.blit(bg4, (560, 500))

    for bullet in bullets:
        bullet.draw(win)
    for h in enemies:
        h.draw(win)
    for t in flammet:
        t.draw(win)

    pygame.display.update()


# mainloop
man = player(200, 570, 64, 64)
goblin = enemy(100, 570, 64, 64, 900)
bullets = []
enemies = []
flammet = []
run = True
s = pygame.draw.rect(win, (45, 54, 7), (560, 502, 200, 73), 2)
playsound = pygame.mixer.Sound(
    'C:/Users/yacin/OneDrive/Bureau/Player Charachter Frames/play.wav')


while run:

    clock.tick(FPS)

    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
            if s.collidepoint(event.pos):
                print("ffeeeffe")
                playsound.play()
                gaming = False

        if event.type == pygame.QUIT:
            run = False

    for bullet in bullets:
        if bullet.x < 500 and bullet.x > 0:
            bullet.x += bullet.vel
        else:
            bullets.pop(bullets.index(bullet))

    keys = pygame.key.get_pressed()

    if keys[pygame.K_SPACE]:
        if man.left:
            facing = -1
        else:
            facing = 1

        if len(bullets) < 5:
            bullets.append(projectile(round(man.x + man.width // 2),
                                      round(man.y + man.height//2), 6, (0, 0, 0), facing))
        if len(flammet) < 5:
            flammet.append(flamme(round(man.x + man.width // 2), man.y))
            enemies.append(enemy(100, 410, 64, 64, 300))

    if keys[pygame.K_LEFT] and man.x > man.vel:
        man.x -= man.vel
        man.left = True
        man.right = False
        man.standing = False
    elif keys[pygame.K_RIGHT] and man.x < 1000:
        man.x += man.vel
        man.right = True
        man.left = False
        man.standing = False
    else:
        man.standing = True
        man.walkCount = 0

    if not(man.isJump):
        if keys[pygame.K_UP]:
            man.isJump = True
            man.right = False
            man.left = False
            man.walkCount = 0
    else:
        if man.jumpCount >= -10:
            neg = 1
            if man.jumpCount < 0:
                neg = -1
            man.y -= (man.jumpCount ** 2) * 0.5 * neg
            man.jumpCount -= 1
        else:
            man.isJump = False
            man.jumpCount = 10

    redrawGameWindow()

pygame.quit()
