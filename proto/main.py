#!/usr/bin/python2.5

import random

import pyglet
from pyglet.window import mouse
from pyglet.gl import *

import particle

window = pyglet.window.Window(resizable=True)

center = [window.width/2, window.height/2]
ps = []

def fireworks(pos, num):
    for i in xrange(num):
        color = (random.randrange(255), random.randrange(255), random.randrange(255))
        ps.append(particle.Particle(pos, [random.randrange(-200, 200),random.randrange(-200,200)], color))

fireworks(center, int(window.height/10))
# for i in xrange(int(window.height/10)):
#     ps.append(particle.Particle(center, [random.randrange(-200, 200),random.randrange(-200,200)]))

wrap = False

@window.event
def on_draw():
    window.clear()
    for p in ps:
        vlist = p.get_vertex_list()
        vlist.draw(p.get_vertex_type())

def update(dt):
    for p in ps:
        p.update(dt)
        if p.is_dead(window.width, window.height):
            ps.remove(p)
#         if wrap:
#             p.wrap_around(window.width, window.height)
#         else:
#             p.bounce_around(window.width, window.height)
pyglet.clock.schedule(update)


@window.event
def on_mouse_press(x, y, button, modifiers):
    if button == mouse.MIDDLE:
        for p in ps:
            p.pos[0] = x
            p.pos[1] = y
    if button == mouse.RIGHT:
        for p in ps:
            p.vel[0] = x - p.pos[0]
            p.vel[1] = y - p.pos[1]
    if button == mouse.LEFT:
        # Fireworks!
        center = [x,y]
        fireworks(center, 17)

pyglet.app.run()
