from math import sqrt, pi
from const import E0
k = 1.0 / (4 * pi * E0)

q = [None, None, None, None]
charge = [1, 0, 1, 2]                                   # Charges are represented as [x, y, z, q]
q[0] = charge
q[1] = [-1, 0, 1, -1]
q[2] = [0, 1, -1, 1]
q[3] = [0, -1, -1, -2]

E_0 = [None, None, None]                                # Calculate contribution to net electric field
mag=sqrt((q[0][0]**2) + (q[0][1]**2) + (q[0][2]**2))    #   of a single charge.
    
E_0[0] = k * (q[0][3] / (mag**2)) * (-q[0][0] / mag)    # Electric field is [E_x, E_y, E_z]
E_0[1] = k * (q[0][3] / (mag**2)) * (-q[0][1] / mag)    # E[0] represents electric field
E_0[2] = k * (q[0][3] / (mag**2)) * (-q[0][2] / mag)    #   contribution from q[0]

E_1 = [None, None, None]
mag=sqrt((q[1][0]**2) + (q[1][1]**2) + (q[1][2]**2))

E_1[0] = k * (q[1][3] / (mag**2)) * (-q[1][0] / mag)
E_1[1] = k * (q[1][3] / (mag**2)) * (-q[1][1] / mag)
E_1[2] = k * (q[1][3] / (mag**2)) * (-q[1][2] / mag)

E_2 = [None, None, None]
mag=sqrt((q[2][0]**2) + (q[2][1]**2) + (q[2][2]**2))

E_2[0] = k * (q[2][3] / (mag**2)) * (-q[2][0] / mag)
E_2[1] = k * (q[2][3] / (mag**2)) * (-q[2][1] / mag)
E_2[2] = k * (q[2][3] / (mag**2)) * (-q[2][2] / mag)

E_3 = [None, None, None]
mag=sqrt((q[3][0]**2) + (q[3][1]**2) + (q[3][2]**2))

E_3[0] = k * (q[3][3] / (mag**2)) * (-q[3][0] / mag)
E_3[1] = k * (q[3][3] / (mag**2)) * (-q[3][1] / mag)
E_3[2] = k * (q[3][3] / (mag**2)) * (-q[3][2] / mag)

E = [E_0, E_1, E_2, E_3]

E_tot = [None, None, None]                              # Once we have individual fields, we
E_tot[0] = E[0][0] + E[1][0] + E[2][0] + E[3][0]        #   can add together the components to
E_tot[1] = E[0][1] + E[1][1] + E[2][1] + E[3][1]        #   create the total field at the origin
E_tot[2] = E[0][2] + E[1][2] + E[2][2] + E[3][2]        # E_tot will be enormous because a
print 'E =', E_tot, 'N/C'                               #   Coulomb is a huge measurement.
