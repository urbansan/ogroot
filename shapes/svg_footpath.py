import os
from ogroot import ROOT_DIR

class SvgFootpach:
    def __init__(self):
        self.shapes = []

    def _get_svg_sizes(self):
        cx_length = 0
        cy_length = 0
        for shape in self.shapes:
            cx, cy = shape.far_edges()
            cx_length = max(cx, cx_length)
            cy_length = max(cy, cy_length)

        cx_cutoff = cx_length
        cy_cutoff = cy_length
        for shape in self.shapes:
            cx, cy = shape.near_edges()
            cx_cutoff = min(cx, cx_cutoff)
            cy_cutoff = min(cy, cy_cutoff)

        return cx_length - cx_cutoff, cy_length - cy_cutoff, -cx_cutoff, -cy_cutoff

    def generate(self, filename='test.svg'):

        w, h, x_correct, y_correct = self._get_svg_sizes()
        svg = '\n' + '\n'.join(shape.generate_tag(x_correct, y_correct) for shape in self.shapes)
        svg = '<svg width="%s" height="%s">' % (w, h) + svg + '\n</svg>'

        with open(os.path.join(ROOT_DIR, 'svg_output/%s' % filename), 'w') as f:
            f.writelines(svg)

    def add_shape(self, shape):
        self.shapes.append(shape)
