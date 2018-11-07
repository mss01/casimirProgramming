import numpy as np

rad = 1

def circumFer(rad):
    circ = 2*np.pi*rad
    return circ

def surfaceArea(rad):
    "This is a different change"
    "..."
    '''Calculates the surface area of a circle'''
    surfA = np.pi*rad**2
    return surfA


print('Circumference of circle with radius', rad, 'is', circumFer(rad))
print('Surface area of circle with radius', rad, 'is', surfaceArea(rad))

def VolumeSphere(rad):
    vol=4/3*np.pi*rad**3
    return vol

