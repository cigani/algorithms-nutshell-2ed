"""
    Demonstrate probabilistic method of counting a set by sampling.
"""

import random
import math
import numpy

def computeK(generator):
    """
    Compute estimate of using probabilistic counting algorithm.
    Doesn't know value of n, the size of the population
    """
    seen = set()

    while True:
        item = generator()
        if item in seen:
            k = len(seen)
            return 2.0*k*k/math.pi
        else:
            seen.add(item)

if __name__ == '__main__':
    n = 1024
    while n <= 1048576:
        sample = lambda : random.randint(1,n)
        row = []
        for t in [32, 64, 128, 256, 512]:
            estimates = []
            for _ in range(t):
                estimates.append (computeK(sample))
    
            estimates.remove(min(estimates))
            estimates.remove(max(estimates))
            
            row.append(int(numpy.average(estimates)))
        
        print (n, row[0], row[1], row[2], row[3], row[4])
        n = n * 2
        