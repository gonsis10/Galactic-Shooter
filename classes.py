import pygame
import math
from config import WIDTH, HEIGHT


class Crosshair(pygame.sprite.Sprite):
    def __init__(self):
        super(Crosshair, self).__init__()
        self.image = pygame.transform.scale(pygame.image.load("images/crosshair.png").convert_alpha(), (30, 30))
        self.rect = self.image.get_rect()

    def update(self):
        self.rect.center = pygame.mouse.get_pos()


class Player(pygame.sprite.Sprite):
    def __init__(self, pos):
        super(Player, self).__init__()
        self.org_image = pygame.transform.scale(pygame.image.load("images/ship.png").convert_alpha(), (50, 50))
        self.image = self.org_image
        self.rect = self.image.get_rect()
        self.rect.center = pos

        self.rads = 0
        self.angle = 0
        self.flt_x = pos[0]
        self.flt_y = pos[1]
        self.change_x = 0
        self.change_y = 0

        # self.accel_x = 0
        # self.accel_y = 0
        # self.max_accel = 0.2
        self.vel_x = 0
        self.vel_y = 0
        self.max_vel = 5

    def keys_pressed(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_a]:
            self.rect.centerx -= self.max_vel
        elif keys[pygame.K_d]:
            self.rect.centerx += self.max_vel
        if keys[pygame.K_w]:
            self.rect.centery -= self.max_vel
        elif keys[pygame.K_s]:
            self.rect.centery += self.max_vel

    def rotate(self):
        # ROTATION
        mouse_x, mouse_y = pygame.mouse.get_pos()
        rel_x, rel_y = mouse_x - self.rect.centerx, mouse_y - self.rect.centery
        self.rads = math.atan2(rel_y, rel_x)
        self.angle = (180 / math.pi) * -self.rads - 90
        self.image = pygame.transform.rotate(self.org_image, int(self.angle))
        self.rect = self.image.get_rect(center=self.rect.center)

    def update(self):
        self.keys_pressed()
        self.rotate()

    def shoot(self):
        return Bullet(self.rect.center, self.angle + 90, self.rads)


class Bullet(pygame.sprite.Sprite):
    def __init__(self, pos, angle, rads):
        super(Bullet, self).__init__()
        self.image = pygame.image.load("images/bullet.png").convert_alpha()
        self.image = pygame.transform.rotate(self.image, int(angle))
        self.rect = self.image.get_rect(center=pos)

        self.vel = 10
        self.flt_x, self.flt_y = pos
        self.change_x = math.cos(rads) * self.vel
        self.change_y = math.sin(rads) * self.vel

    def update(self):
        self.flt_x += self.change_x
        self.flt_y += self.change_y
        self.rect.center = (int(self.flt_x),
                            int(self.flt_y))
        if self.rect.right < 0 or self.rect.left > WIDTH or self.rect.bottom < 0 or self.rect.top > HEIGHT:
            self.kill()
