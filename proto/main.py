#!/usr/bin/python2.5

import random

import pyglet
from pyglet.window import mouse
from pyglet.gl import *

import particle
import box

window = pyglet.window.Window(resizable=True)

center = [window.width/2, window.height/2]
ps = []
bs = [box.Box((0,0),(32,32),(127,127,127)),
      box.Box((0,32),(32,64),(0,127,127)),
      box.Box((0,64),(32,96),(127,0,127))]

def fireworks(pos, num, accel):
    for i in xrange(num):
        color = (random.randrange(255), random.randrange(255), random.randrange(255))
        ps.append(particle.Particle(pos, [random.randrange(-200, 200),random.randrange(-200,200)], color, accel))

# for i in xrange(int(window.height/10)):
#     ps.append(particle.Particle(center, [random.randrange(-200, 200),random.randrange(-200,200)]))

settings = {'wrap':False, 'kill':True, 'gravity':False}

@window.event
def on_draw():
    window.clear()
    for p in ps:
        vlist = p.get_vertex_list()
        vlist.draw(p.get_vertex_type())
    for b in bs:
        blist = b.get_vertex_list()
        blist.draw(b.get_vertex_type())

def update(dt):
    for p in ps:
        p.update(dt)
        if settings['kill'] and p.is_dead(window.width, window.height):
            ps.remove(p)
        if settings['wrap']:
            p.wrap_around(window.width, window.height)
        else:
            p.bounce_around(window.width, window.height)
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
        if x < 32 and y < 32:
            settings['wrap'] = not settings['wrap']
        elif x < 32 and y >32 and y < 64:
            settings['kill'] = not settings['kill']
        elif x < 32 and y >64 and y < 96:
            settings['gravity'] = not settings['gravity']
            if settings['gravity']:
                accel = (0,-180)
            else:
                accel = (0,0)
            for p in ps:
                p.accel = accel
        else:
            # Fireworks!
            center = [x,y]
            if settings['gravity']:
                accel = (0,-180)
            else:
                accel = (0,0)
            fireworks(center, 17, accel)

if __name__=="__main__":
    if settings['gravity']:
        accel = (0,-180)
    else:
        accel = (0,0)
    fireworks(center, int(window.height/10), accel)
    pyglet.app.run()
