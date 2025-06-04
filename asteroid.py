import pygame
from circleshape import CircleShape
from constants import ASTEROID_MIN_RADIUS
import random

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, 2)

    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return

        random_angle = random.uniform(20, 50)
        new_vector_one = self.velocity.rotate(random_angle)
        new_vector_two = self.velocity.rotate(-random_angle)
        x, y = self.position
        new_radius = self.radius - ASTEROID_MIN_RADIUS
        asteroid_one = Asteroid(x, y, new_radius)
        asteroid_two = Asteroid(x, y, new_radius)

        asteroid_one.velocity = new_vector_one * 1.2
        asteroid_two.velocity = new_vector_two * 1.2





