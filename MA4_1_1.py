
"""
Solutions to module 4
Review date:
"""

student = "Nora Sundman"
reviewer = ""

import math
import random as r
import matplotlib.pyplot as plt 

def approximate_pi(n):
    r.seed(244)
    radius = 1
    nc = 0
    for _ in range(n):
        pointX = r.uniform(-radius, radius)
        pointY = r.uniform(-radius, radius)
        color = "blue"
        if pointX*pointX + pointY*pointY <= 1: # Is inside
            nc += 1
            color = "red"
        plt.scatter(pointX, pointY, c=color, s=4)
    pi = 4*nc/n
    print(f"Number of points inside the circle are {nc}, the approximation of pi is {pi}, while the built in pi constant is {math.pi}")
    #plt.show()
    ax = plt.gca()
    ax.set_aspect('equal', adjustable='box')
    plt.savefig(f"approximate_pi_n{n}.png")
    return pi
    
def main():
    dots = [1000, 10000, 100000]
    for n in dots:
        approximate_pi(n)

if __name__ == '__main__':
	main()
