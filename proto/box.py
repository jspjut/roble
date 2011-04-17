import pyglet

class Box:
    def __init__(self, botleft, topright, color = (127,127,127)):
        self.botleft = botleft
        self.topright = topright
        self.color = color

    def get_vertex_list(self):
        return pyglet.graphics.vertex_list(4,
                                           ('v2f', (self.botleft[0], self.botleft[1],
                                                    self.botleft[0], self.topright[1],
                                                    self.topright[0], self.topright[1],
                                                    self.topright[0], self.botleft[1]
                                                    )),
                                           ('c3B', (self.color[0], self.color[1], self.color[2],
                                                    self.color[0], self.color[1], self.color[2],
                                                    self.color[0], self.color[1], self.color[2],
                                                    self.color[0], self.color[1], self.color[2]))
                                           )

    def get_vertex_type(self):
        return pyglet.graphics.GL_QUADS
