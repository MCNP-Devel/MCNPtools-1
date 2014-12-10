#! /usr/bin/env python
# Script to generate a general cylinder with GQ cards for MCNP
# Ryan M. Bergmann, Dec 9, 2014.  ryan.bergmann@psi.ch, ryanmbergmann@gmail.com

import pylab as pl
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import axes3d, Axes3D
from matplotlib.colors import LogNorm, PowerNorm, Normalize
from matplotlib import cm
import sys
import numpy
import re

### print misc
print "GQ card form:  Ax^2 + By^2 + Cz^2 + Dxy + Eyz + Fxz + Gx + Hy + Jz + K = 0"

### cyclinder radius, translation
rad = 320
trans_x = 0.0
trans_y = 0.0
trans_z = 0.0
print "radius = ", rad
print "translation (x,y,z) = ", trans_x, ", ",trans_y, ", ",trans_z

### define cylinder axis (x,y,z)
axis_vec=numpy.array([0.0000001,-15.65,540.0])

### normalize
axis_vec      = numpy.divide(axis_vec,numpy.sqrt(numpy.sum(numpy.multiply(axis_vec,axis_vec))))
print "normed axis vector = ", axis_vec

### get spherical coordinates
phi   = numpy.arctan(axis_vec[1]/axis_vec[0])
theta = numpy.arccos(axis_vec[2])
print "theta = ",theta," phi = ",phi

### variablize trigs
st = numpy.sin(theta)
ct = numpy.cos(theta)
sp = numpy.sin(phi)
cp = numpy.cos(phi)

### calculate coeffs
A = ct*ct*cp*cp + sp*sp
B = ct*ct*sp*sp + cp*cp
C = st*st
D = -2.0*sp*cp*st*st
E = -2.0*st*ct*sp
F = -2.0*st*ct*cp
G = 0.0
H = 0.0
J = 0.0
K =  -rad*rad


### do linear translation
K = K + A*trans_x*trans_x + B*trans_y*trans_y + C*trans_z*trans_z + D*trans_x*trans_y + E*trans_y*trans_z + F*trans_x*trans_z - G*trans_x - H*trans_y - J*trans_z
G = G - 2.0*A*trans_x - D*trans_y - F*trans_z
H = H - 2.0*B*trans_y - D*trans_x - E*trans_z
J = J - 2.0*C*trans_z - E*trans_y - F*trans_x

### print
print 'A = ', A      # x^2
print 'B = ', B      # y^2
print 'C = ', C      # z^2
print 'D = ', D     # xy
print 'E = ', E      # yz
print 'F = ', F      # xz
print 'G = ', G      # x
print 'H = ', H      # y
print 'J = ', J      # z
print 'K = ', K      # const

print "MCNP CARD:"

print "XX  gq  ",A,B,C,D
print "      ",E,F,G
print "      ",H,J,K