# coding: utf-8
from __future__ import print_function
import matplotlib
matplotlib.use('agg')

import sys, math, numpy as N, matplotlib.pyplot as P
from context import libstempo as T


T.data = T.__path__[0] + '/data/' # example files


def _test_version():
    print("Python version   :",sys.version.split()[0])
    print("libstempo version:",T.__version__)
    print("Tempo2 version   :",T.libstempo.tempo2version())
    return True


def _test_load():
    psr = T.tempopulsar(parfile = T.data + '/J1909-3744_NANOGrav_dfg+12.par',
                        timfile = T.data + '/J1909-3744_NANOGrav_dfg+12.tim')
    return True


