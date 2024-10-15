
"""
Solutions to module 4
Review date:
"""

student = "Nora Sundman"
reviewer = ""

import math as m
import random as r
import functools

def sphere_volume(n, d):
    r.seed(244)
    # n is a list of set of coordinates
    # d is the number of dimensions of the sphere 
    radius = 1
    vc = 0
    for _ in range(n):
        x = [r.uniform(-radius, radius) for _ in range(d)] # Create d amount coordinates

        terms = list(map(lambda a: a**2, x))
        
        term_sum = functools.reduce(lambda a, b: a+b, terms)
        
        if term_sum <= 1: # Is inside
            vc += 1
    
    ## Volume calculation
    # V_i / V_t = points_i / points_t => V_i = (points_i / points_t) * V_t 
    # | in which V_t is the length of the side (random function boundrary => axis length=2 in this case) raised to the power of how many dimensions d.
    # It's calculating the square area, box volume and the like for higher dimensions.
    volume = 2**d * vc/n 
    return volume

def hypersphere_exact(n,d):
    return m.pi**(d/2)/m.gamma(d/2+1) # Calculate with radius=1
    #return (r**d)*(m.pi**(d/2) )/(m.gamma(d/2+1))
     
def main():
    n = 100000
    d = 2
    sphere_volume(n,d)


if __name__ == '__main__':
	main()

