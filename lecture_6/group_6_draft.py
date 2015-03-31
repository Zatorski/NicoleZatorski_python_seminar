#################################
# Title: Lecture 6 Group Script #
# Lesson: Conductors/Capacitors #
# Filename: group_6.py	        #
# Original Author: Joe Griffin	#
# Most Recent Edit: 1/27/2014	#
# Last Editor: Joe Griffin	#
#################################

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
        self.ref[self] = self.q

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
    def __init__(self, ref, Rc, hc, lambda_c, Rs, sigma_c, distance_between):
        self.Rc = Rc
        self.hc = hc
        self.ref = ref
        self.lambda_c = lambda_c
        self.Rs = Rs
        self.sigma_c = sigma_c
        self.Qs = sigma_s/(4 * pi * (Rs**2))
        self.Qc = lambda_c/(2 * pi * Rc * hc)
        self.distance_between = distance_between
        ref[self] = self.Qs + self.Qc
        

    def capacitance(self):
        Vs = ((k * self.Qs)/ self.Rs) - ((k * self.Qs)/ (self.distance_between- self.Rs))
        Vc = -lambda_c * log((self.distance_between/self.Rc), 2.718281828) * k


class super_conductors(capacitor):
    def __inti__(self, cap1, cap2, type_of_connection):
        self.cap1 = cap1
        self.cap2 = cap2
        self.type_of_connection = type_of_connection
                 
                 
