print('hello world')

import numpy as np

rad = 1

def circumFer(rad):
    circ = 2*np.pi*rad
    return circ

print('Circumference of circle with radius', rad, 'is', circumFer(rad))

