#!/usr/bin/env python3

# Created by: maliksalem1
# Created on: Oct 2022
# This program shows volume and area of a sphere

import math


def main():
    # user input

    radius = float(input("Enter the radius of a sphere: "))

    s_area = 4 * math.pi * pow(radius, 2)
    volume = (4 / 3) * math.pi * pow(radius, 3)

    # output
    print("surface area of the sphere will be %.2f" % s_area)

    print("volume of the sphere will be %.2f" % volume)

    print("\nDone.\n")


if __name__ == "__main__":
    main()
