#!/usr/bin/python2.5

import pyglet
from pyglet.window import mouse

import particle

window = pyglet.window.Window(resizable=True)

p = particle.Particle([64,64], [50,200])

@window.event
def on_draw():
    window.clear()
    p.draw()

def update(dt):
    p.update(dt)
    p.check_bounds(window.width, window.height)
pyglet.clock.schedule(update)

@window.event
def on_mouse_press(x, y, button, modifiers):
    if button == mouse.LEFT:
        p.pos[0] = x
        p.pos[1] = y
    if button == mouse.RIGHT:
        p.vel[0] = x - p.pos[0]
        p.vel[1] = y - p.pos[1]

pyglet.app.run()
