#########################
# Title: Problem Set 4  #
# Nicole Zatorski       #
#########################

# We will calculate the flux due to a charged sphere in space through a plane.

from math import sqrt, pi, sin, atan2
E0 = 8.854187817e-12 
k = 1.0 / (4 * pi * E0)

pos_sphere = [0, 0, 0]
q_sphere = 10e-6


# the dE_list is the jhat-component of the electric field because the other
# components don't contribute to flux


def F():
    plane = ((2.0, 2.0, 1.0), (-2.0, -2.0, 1.0), (2.0, -2.0, 1.0), (-2.0, 2.0, 1.0))        # Position of the verticies of the square
    Lx = (plane[1][0] - plane[0][0])**2                                                     # Length of the sides of the square
    Ly = (plane[1][1] - plane[0][1])**2
    area = (plane[0][0] - plane[1][0]) * (plane[0][1] - plane[1][1])                        # Area of the square
    distance = sqrt(Lx + Ly)
    dx = 1.0e-3                                                                             # Integral increment length
    dy = 1.0e-3 
    dEx_list = []                                                                           # Differential contributions
    dEy_list = [] 
##    for i in xrange(int(sqrt(Lx) / dx)):                                                  # Create our integration iterable
##        theta = atan2(1, i)
##        E_sphere = ((k * q_sphere) / (distance ** 2)) * sin (theta)
##        dEx_list.append(E_sphere)
##    for elt in dEx_list:
    for i in xrange(int(sqrt(Lx) / dx)):                                                    # Taking all of the partitions of x
        for j in xrange(int(sqrt(Ly) / dy)):                                                #   and calculating the electric field for 
            theta = atan2(1, i*distance)                                                             #   the corresponding line of y values
            E_sphere = ((k * q_sphere) / (distance ** 2)) * sin (theta)                     # The j hat component of the electric field
            dEy_list.append(E_sphere)
    E = sum(dEy_list)
    F = E * area
    return F                                                                                # Total Flux

def vector(F):
    plane = ((2.0, 2.0, 1.0), (-2.0, -2.0, 1.0), (2.0, -2.0, 1.0), (-2.0, 2.0, 1.0))
    area = (plane[0][0] - plane[1][0]) * (plane[0][1] - plane[1][1])
    Eforce = F *(10.0e-3)                                                                   # E (which is flux divided by area) multiplied
    g = 9.80665                                                                             #   by charge (which is sigma times area is force
    mass = Eforce/g                                                                         # Sum of forces is 0, so electric field force equals 
    return mass                                                                             #   gravitational force
