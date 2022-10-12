#!/usr/bin/env python3

# Created by: maliksalem1
# Created on: Oct 2022
# This program shows volume and area of a sphere

import math

#user input
radius = float(input("Enter the radius of a sphere: "))

#process 1

s_area = 4*math.pi*pow(radius,2)

#process 2

volume = (4/3)*math.pi*pow(radius,3)

#output 
print("surface area of the sphere wll be %.2f" %s_area)
print("volume of the sphere will be  %.2f" %volume)

print("\nDone.\n")
