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
from const import E0
k = 1 / (4 * pi * E0)

class capacitor:
    def __init__(self, capacitance, ref):
        self.capacitance = float(capacitance)               # This will be in Farads
        self.q = 0.0

    def charge(self, voltage):
        self.q = self.capacitance * voltage                 # This will be in Coulombs
        self.ref[self] = self.q

class ll_plate_cap(capacitor):
    def __init__(self, area, sep, ref):                     # ref is not necessarily a
        self.area = float(area)                             #   named dict, just a dict
        self.sep = float(sep)
        self.ref = ref                                      # We can refer to ref as an
        self.capacitance = E0 * area / sep                  #   attribute of self
        self.q = 0.0
