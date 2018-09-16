from ogroot.shapes.shape import shape

class Circle(shape):
    def __init__(self, cx, cy, radius, fill='', opacity='0.4'):
        super().__init__(cx, cy)
        self.radius = radius
        self.args = (fill, opacity)

    def far_edges(self):
        return self.cx + self.radius, self.cy + self.radius

    def near_edges(self):
        return self.cx - self.radius, self.cy - self.radius

    def generate_tag(self, x_correct, y_correct):
        svg = '<circle cx="{}" cy="{}" r="{}" stroke="green" ' \
              'stroke-width="4" fill="{}" fill-opacity="{}"/>'.format(self.cx + x_correct, self.cy + y_correct, self.radius, *self.args)

        return svg