from ogroot.shapes.shape import shape

class Ellipse(shape):
    def __init__(self, cx, cy, rx, ry, fill='', opacity='0.4'):
        super().__init__(cx, cy)
        self.rx = rx
        self.ry = ry
        self.args = (fill, opacity)

    def far_edges(self):
        return self.cx + self.rx, self.cy + self.ry

    def near_edges(self):
        return self.cx - self.rx, self.cy - self.ry

    def generate_tag(self, x_correct, y_correct):
        svg = '<ellipse cx="{}" cy="{}" rx="{}" ry="{}" stroke="black" ' \
              'stroke-width="2" fill="{}" fill-opacity="{}"/>'.format(self.cx + x_correct, self.cy + y_correct, self.rx, self.ry, *self.args)

        return svg