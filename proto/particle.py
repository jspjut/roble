import pyglet

class Particle:
    def __init__(self, pos, vel):
        self.pos = [pos[0], pos[1]]
        self.vel = vel
        self.color = (0,0,255)

    def draw(self):
        size = 5
        pyglet.graphics.draw(6, pyglet.gl.GL_TRIANGLE_FAN,
                             ('v2f', (self.pos[0], self.pos[1],
                                      self.pos[0] + size, self.pos[1] + 0,
                                      self.pos[0] + 0, self.pos[1] + size,
                                      self.pos[0] + -size, self.pos[1] + 0,
                                      self.pos[0] + 0, self.pos[1] + -size,
                                      self.pos[0] + size, self.pos[1] + 0
                                      )),
                             ('c3B', (255, 255, 255,
                                      0, 0, 255,
                                      0, 0, 255,
                                      0, 0, 255,
                                      0, 0, 255,
                                      0, 0, 255))
                             )
        pass

    def update(self, dt):
        self.pos[0] = self.pos[0] + self.vel[0] * dt
        self.pos[1] = self.pos[1] + self.vel[1] * dt

    def wrap_around(self, width, height):
        if self.pos[0] > width:
            self.pos[0] -= width
        if self.pos[0] < 0:
            self.pos[0] += width
        if self.pos[1] > height:
            self.pos[1] -= height
        if self.pos[1] < 0:
            self.pos[1] += height

    def bounce_around(self, width, height):
        if (self.pos[0] > width and self.vel[0] > 0) or (self.pos[0] < 0 and self.vel[0] < 0):
            self.vel[0] = -self.vel[0]
        if (self.pos[1] > height and self.vel[1] > 0) or (self.pos[1] < 0 and self.vel[1] < 0):
            self.vel[1] = -self.vel[1]
