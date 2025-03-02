import random

import pygame

import circleshape
from constants import *


class Asteroid(circleshape.CircleShape):
    containers = []

    def __init__(self, x: float, y: float, radius: float):
        super().__init__(x, y, radius)
        self.lifetime = 5

    def draw(self, screen):
        pygame.draw.circle(
            screen, PLAYER_COLOR, (self.position[0], self.position[1]), 2
        )

    def update(self, dt):
        self.position += dt * self.velocity

    def drain(self, dt):
        self.lifetime -= dt
        if self.lifetime <= 0:
            self.kill()

    def split(self):
        self.kill()
        if ASTEROID_MIN_RADIUS >= self.radius:
            return
        self.spawn()

    def spawn(self):
        angle = random.uniform(20, 50)
        cis_velocity = self.velocity.rotate(+angle)
        trans_velocity = self.velocity.rotate(-angle)
        new_radius = self.radius - ASTEROID_MIN_RADIUS
        cis_asteroid = Asteroid(self.position[0], self.position[1], new_radius)
        trans_asteroid = Asteroid(self.position[0], self.position[1], new_radius)
        cis_asteroid.velocity = cis_velocity * ASTEROID_SPLIT_ACCELERATION 
        trans_asteroid.velocity = trans_velocity * ASTEROID_SPLIT_ACCELERATION
