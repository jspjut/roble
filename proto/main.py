#!/usr/bin/python2.5

import random

import pyglet
from pyglet.window import mouse
from pyglet.gl import *

import particle

window = pyglet.window.Window(resizable=True)

center = [window.width/2, window.height/2]
ps = []
for i in xrange(int(window.height/10)):
    ps.append(particle.Particle(center, [random.randrange(-200, 200),random.randrange(-200,200)]))

wrap = False

@window.event
def on_draw():
    window.clear()
    for p in ps:
        p.draw()

def update(dt):
    for p in ps:
        p.update(dt)
        if wrap:
            p.wrap_around(window.width, window.height)
        else:
            p.bounce_around(window.width, window.height)
pyglet.clock.schedule(update)

@window.event
def on_mouse_press(x, y, button, modifiers):
    if button == mouse.LEFT:
        for p in ps:
            p.pos[0] = x
            p.pos[1] = y
    if button == mouse.RIGHT:
        for p in ps:
            p.vel[0] = x - p.pos[0]
            p.vel[1] = y - p.pos[1]

pyglet.app.run()
