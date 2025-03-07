#!/usr/bin/env python3
# Created by: Gustav Ihlenfeld
# Created on: March 5, 2025
# This program calculates the circumference and area of a circle

import math


def main():
    # Input (radius, fixed)
    radius = 12
    # Process the area and circumference of a circle
    area = math.pi * (radius**2)
    circumference = 2 * math.pi * radius

    # Output the results (area and circumference)
    print("\nThe area of the circle is {:.2f} square units.".format(area))
    print("The circumference of the circle is {:.2f} units.".format(circumference))

    # Call function


if __name__ == "__main__":
    main()
