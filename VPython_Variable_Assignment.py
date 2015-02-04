#Video two chalenge
#Nicole Zatorski

from visual import *
sphere1 = sphere(pos = vector(2, 2, 0), radius = .5, color = color.green)
sphere2 = sphere(pos = vector(-2, 0, 0), radius = .5, color = color.green)
sphere3 = sphere(pos = vector(2, -2, 0), radius = .5, color = color.green)

arrow1 = arrow(pos = sphere1.pos, axis = sphere2.pos - sphere1.pos, color = color.red)
arrow2 = arrow(pos = sphere2.pos, axis = sphere3.pos - sphere2.pos, color = color.red)
arrow3 = arrow(pos = sphere3.pos, axis = sphere1.pos - sphere3.pos, color = color.red)
