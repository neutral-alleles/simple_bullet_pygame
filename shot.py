import pygame

import circleshape
from constants import *


class Shot(circleshape.CircleShape):
    containers = []

    def __init__(self, x: float, y: float):
        super().__init__(x, y, SHOT_RADIUS)
        self.lifetime = SHOT_LIFETIME

    def draw(self, screen):
        pygame.draw.circle(
            screen, SHOT_COLOR, (self.position[0], self.position[1]), 2
        )

    def update(self, dt):
        self.position += dt * self.velocity
        self.lifetime -= dt
        if self.lifetime < 0:
            self.kill()
