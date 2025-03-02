# this allows us to use code from
# the open-source pygame library
# throughout this file
import sys

import pygame

from asteroid import Asteroid
from asteroidfield import AsteroidField
from constants import *
from player import Player
from shot import Shot


def main():
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt: float = 0

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    Player.containers = [updatable, drawable]
    player: Player = Player(x=SCREEN_WIDTH / 2, y=SCREEN_HEIGHT / 2)
    Asteroid.containers = [asteroids, updatable, drawable]

    AsteroidField.containers = [updatable]
    asteroid_field = AsteroidField()

    Shot.containers = [updatable, drawable, shots]

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        pygame.Surface.fill(screen, SCREEN_COLOR)

        updatable.update(dt)

        for draw_obj in drawable:
            draw_obj.draw(screen)

        for asteroid in asteroids:
            if player.collides(asteroid):
                player.health -= 1
                asteroid.kill()
            if player.health <= 0:
                print("Game over!")
                sys.exit(0)

        print(len(asteroids))

        for asteroid in asteroids:
            for shot in shots:
                if asteroid.collides(shot):
                    asteroid.split()
                    shot.kill()

        for asteroid in asteroids:
            this_screen = asteroid.check_in_area(0, 0, SCREEN_WIDTH, SCREEN_HEIGHT)
            if not this_screen:
                asteroid.drain(dt)

        for this_asteroid in asteroids:
            this_screen = this_asteroid.check_in_area(0, 0, SCREEN_WIDTH, SCREEN_HEIGHT)
            if not this_screen:
                break
            for that_asteroid in asteroids:
                not_equal = this_asteroid != that_asteroid
                collides = this_asteroid.collides(that_asteroid)
                that_screen = that_asteroid.check_in_area(
                    0, 0, SCREEN_WIDTH, SCREEN_HEIGHT
                )

                if not_equal and collides and this_screen and that_screen:
                    this_asteroid.split()
                    that_asteroid.split()

        pygame.display.flip()
        dt = clock.tick(60) / 1000


if __name__ == "__main__":
    main()
