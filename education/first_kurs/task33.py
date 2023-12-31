import math

class Sphere:
    def __init__(self, radius, mass):
        self.radius = radius
        self.mass = mass

    def get_radius(self):
        return self.radius

    def get_mass(self):
        return self.mass

    def get_volume(self):
        return (4/3) * math.pi * self.radius**3

    def get_surface_area(self):
        return 4 * math.pi * self.radius**2

    def get_density(self):
        return self.mass / self.get_volume()

# Example usage:
ball = Sphere(2, 50)
print(ball.get_radius())        # Output: 2
print(ball.get_mass())          # Output: 50
print(ball.get_volume())        # Output: 33.510321638291124
print(ball.get_surface_area())  # Output: 50.26548245743669
print(ball.get_density())       # Output: 1.492079387834959

print("radius : {} , mass: {}".format(ball.radius,ball.mass))
