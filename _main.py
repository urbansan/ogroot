import random
import os
from ogroot import ROOT_DIR
from ogroot.shapes import SvgFootpach, Circle, Ellipse

from ogroot.coordinates import footpath_data

fp = SvgFootpach()
W=500
H=500
coordinates = [
    (W/3, H/3, 40),
    (W/2, H/2, 40),
    (W/3*2, H/3*2, 40)
]

rand_color = lambda: '#' + hex(random.randint(0, 0xffffff)).split('x')[1].upper()

path_length = 1200
path_width = 100

for rx, ry in footpath_data:
    shape = Ellipse(
        rx + random.random() * (path_width - rx),
        ry + random.random() * (path_length - ry),
        rx, ry, fill=rand_color(), opacity='0.4'
    )
    fp.add_shape(shape)


# print(hex(randint(0, 0xffffff)))
fp.generate()