 # commonImports.py:
from __future__ import print_function
import numpy as np # for numerical computation
import sympy as sp # sympy module for computation
import numpy.linalg as lg # numpy linear algebra module
import scipy.linalg as sg # scipy linear algebra module
import scipy.integrate as si
from scipy.stats import ortho_group
import importlib
import itertools
import inspect
import csv
import pandas as pd
import random
from IPython.display import display, Math

import autograd.numpy as anp # Thinly−wrapped numpy
from autograd import grad

from grcodes import drawArrow, plotfig, printM, printx # frequently used

import math as ma
from sympy import sin, cos, exp, symbols, lambdify, init_printing, latex
from sympy import pi, Matrix, sqrt, oo, integrate, diff, Derivative
from sympy import MatrixSymbol, simplify, nsimplify, Function
from sympy import factor, expand, nsimplify, Matrix, ordered, hessian
from sympy.plotting import plot as splt
init_printing(use_unicode=True) # for latex-like qualityprinting formate

from matplotlib.ticker import MultipleLocator
import matplotlib.pyplot as plt # for plotting figures
import matplotlib as mpl 
