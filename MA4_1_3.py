
"""
Solutions to module 4
Review date:
"""

student = "Nora Sundman"
reviewer = ""

import math as m
import random as r
from time import perf_counter
import functools

import concurrent.futures as future
import multiprocessing as multiprocess


def sphere_volume(n, d, processId = None, returnContainer = None):
    r.seed(244)
    # n is a list of set of coordinates
    # d is the number of dimensions of the sphere 
    radius = 1
    vc = 0
    for _ in range(int(n)):
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
    #print(f"Volume is estimated to {volume}")
    
    if processId != None:
        returnContainer[processId] = volume
    return volume

def hypersphere_exact(n,d):
    return m.pi**(d/2)/m.gamma(d/2+1) # Calculate with radius=1


# parallel code - parallelize for loop
def sphere_volume_parallel1(n,d,np):
    #using multiprocessor to perform 10 iterations of volume function
    manager = multiprocess.Manager()
    volumesDict = manager.dict()
    processes = []
    for i in range(np):
        p = multiprocess.Process(target=sphere_volume, args=[n,d, i, volumesDict])
        processes.append(p)
    
    for p in processes:
        p.start()
    
    for p in processes:
        p.join()
    
    #print(volumesDict.values())
    return functools.reduce(lambda a, b: a+b, volumesDict.values()) / float(np) # Return the avarage of the volumes


# parallel code - parallelize actual computations by splitting data
def sphere_volume_parallel2(n,d,np):
    with future.ProcessPoolExecutor() as ex:
        n_part = n/np
        volumes = ex.map(sphere_volume, [n_part for _ in range(np)], [d for _ in range(np)])
        avarageVolume = functools.reduce(lambda a, b: a+b, volumes) / float(np)
    return avarageVolume


def main():
    # PART 1 -- parallelization of a for loop among 10 processes 
    print(f"Part1, will compare running unparallel and parallel with the same number of simulated points")
    n = 100000
    d = 11
    start = perf_counter()
    for y in range (10):
        sphere_volume(n,d)
    end = perf_counter()
    print(f"Time for unparallel {round(end-start, 4)}s")

    n = 1000000
    d = 11
    np = 10
    start = perf_counter()
    res = sphere_volume_parallel2(n, d, np) # Using parallel2 as it divides up n by np, instead of just running the full n in np processes 
    end = perf_counter()
    print(f"Time for parallel {round(end-start, 4)}s")
    
    # PART 2
    print(f"\nPart2, will compare the two approaches with both simulating the same amount of points")
    np = 10
    start = perf_counter()
    res = sphere_volume_parallel1(100000, 11, np) # In this call n will be multiplied by np in regards to how many simulations are made
    end = perf_counter()
    print(f"Time for parallel1 {round(end-start, 4)}s with result {res} compared to exact {hypersphere_exact(1000, 11)}")
    
    start = perf_counter()
    res = sphere_volume_parallel2(1000000, 11, np) # n is 10 times larger, because problem will be split into 10, will simulate the same amount of points in the end
    end = perf_counter()
    print(f"Time for parallel2 {round(end-start, 4)}s with result {res} compared to exact {hypersphere_exact(1000, 11)}")
    

if __name__ == '__main__':
	main()
