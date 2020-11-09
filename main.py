from random import random
from pso import PSO

class Unbuffered(object):
   def __init__(self, stream):
       self.stream = stream
   def write(self, data):
       self.stream.write(data)
       self.stream.flush()
   def writelines(self, datas):
       self.stream.writelines(datas)
       self.stream.flush()
   def __getattr__(self, attr):
       return getattr(self.stream, attr)

import sys
sys.stdout = Unbuffered(sys.stdout)

# Parameters
v_max = 5
omega = 0.7
c_1 = 2
c_2 = 2
S = 30

print("8-QUEENS PROBLEM SOLUTION USING PSO")

pso = PSO(v_max, omega, c_1, c_2, S)
print("alou")
pso.search()
