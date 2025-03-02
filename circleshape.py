import pygame


# Base class for game objects
class CircleShape(pygame.sprite.Sprite):
    def __init__(self, x, y, radius):
        # we will be using this later
        if hasattr(self, "containers"):
            super().__init__(self.containers)
        else:
            super().__init__()

        self.position = pygame.Vector2(x, y)
        self.velocity = pygame.Vector2(0, 0)
        self.radius = radius

    def collides(self, other):
        return self.radius > pygame.math.Vector2.distance_to(
            self.position, other.position
        )

    def draw(self, screen):
        # sub-classes must override
        pass

    def check_in_area(self, x1, y1, x2, y2):
        return (self.position[0] >= x1 and self.position[0] <= x2) and (
            self.position[1] >= y1 and self.position[1] <= y2
        )

    def update(self, dt):
        # sub-classes must override
        pass
