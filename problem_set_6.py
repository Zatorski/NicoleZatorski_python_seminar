#########################################
# Title: ModifiedLecture 6 Group Script #
# Lesson: Conductors/Capacitors         #
# Filename: problem_set_6.py            #
# Original Author: Joe Griffin	        #
# Last Editor: Nicole Zatorski  	#
#########################################

# This script is meant to define capacitor classes for a number of different capacitors so
#   they can be used to calculate total circuit capacitance.
from math import pi
from math import log
from const import E0
k = 1 / (4 * pi * E0)

class capacitor:
    def __init__(self, capacitance, ref):
        self.capacitance = float(capacitance)               # This will be in Farads
        self.q = 0.0
        self.ref = ref
        ref[self] = self.q

    def charge(self, voltage):
        self.q = self.capacitance * voltage                 # This will be in Coulombs
        self.ref[self] = (self.q, self.capacitance)

class ll_plate_cap(capacitor):
    def __init__(self, area, sep, ref):
        self.area = float(area)
        self.sep = float(sep)
        self.ref = ref
        self.capacitance = E0 * area / sep
        self.q = 0.0
        
class sphere_cap(capacitor):
    def __init__(self, r_inner, r_outer, ref):
        self.r_inner = float(r_inner)
        self.r_outer = float(r_outer)
        self.ref = ref
        self.capacitance = (self.r_inner * self.r_outer) / ( k * (self.r_outer - self.r_inner))
        self.q = 0.0

class asymmetric_cap(capacitor):
    def __init__(self, ref, distance_between,
                 Rc, hc, lambda_c,
                 Rs, sigma_s):
        self.Rc = Rc                                        # Raduis of cylinder                                                   
        self.hc = hc                                        # Height of cylinder
        self.ref = ref                                      # Refference dictionary to store charge
        self.lambda_c = lambda_c                            # Cylinder surface charge
        self.Rs = Rs                                        # Radius of sphere
        self.sigma_c = sigma_c                              # Sphere surface charge
        self.Qs = sigma_s/(4 * pi * (Rs**2))                # Charge of sphere ####### CHECK THE UNITS!!!!!
        self.Qc = lambda_c/(2 * pi * Rc * hc)               # Charge of cylinder ###### CHECK THE UNITS!!!!!
        self.distance_between = distance_between            # S
        self.q = self.Qs + self.Qc                          # Total charge is the summ of the charges on s and c
        ref[self] = self.q
        

    def capacitance(self):
        Vs = ((k * self.Qs)/ self.Rs) - ((k * self.Qs)/ (self.distance_between- self.Rs)) #### You did these calculations
        Vc = -lambda_c * log((self.distance_between/self.Rc), 2.718281828) * k  ### analytically, could you have done them
                                                                            #### numerically instead?
                                                                            ### Double check Vc and  do not confuse R_c and R_S!
        Vtot = Vs + Vc                                      # Total voltage is the sum of the voltages
        self.capacitance = self.q/Vtot


class super_conductors(capacitor):
    def __inti__(self, cap1, cap2, type_of_connection):  ###### This supercapacitor works, although type_of_connection
                                                            #### is not a boolean but a string (check the sol)
        self.cap1 = cap1
        self.cap2 = cap2
        self.type_of_connection = str.lower(type_of_connection)     # This prevents an issue from arising if the user inputs a string with uppercase letters 

    def capacitance_calc(self):
        if self.type_of_connection == 'parallel':
            self.capacitance = self.cap1.capacitance + self.cap2.capacitance
        else:
            self.capacitance = (1/self.cap1.capacitance) + (1/self.cap2.capacitance) # Capacitors in series


            ######## how about the charge method for super_conductors?
