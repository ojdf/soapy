import numpy
import numpy.random

import pyfftw

import aotools
from aotools.image_processing import centroiders

from .. import LGS, logger, lineofsight, AOFFT, interp
from . import wfs
from .. import numbalib

# xrange now just "range" in python3.
# Following code means fastest implementation used in 2 and 3
try:
    xrange
except NameError:
    xrange = range

# The data type of data arrays (complex and real respectively)
CDTYPE = numpy.complex64
DTYPE = numpy.float32

class Perfect(wfs.WFS):

    def calcInitParams(self):
        """
        Calculate some parameters to be used during initialisation
        """
        super(Perfect, self).calcInitParams()
        self.n_measurements = self.mask.shape[0] * self.mask.shape[1]
            

    def calculateSlopes(self):

        self.slopes = (self.los.phase * self.mask).flatten() / self.los.phs2Rad
        return self.slopes

    def calcFocalPlane(self):
        self.wfsDetectorPlane = self.los.phase * self.mask
        return self.wfsDetectorPlane
