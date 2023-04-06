import sympy as sym
import math as m
c1, s1, d1 = sym.symbols('c1, s1, d1')
theta1 = m.radians(0)
T1 = sym.Matrix([[round(m.cos(theta1)), -m.sin(theta1), 0, 0],
                 [m.sin(theta1), round(m.cos(theta1)), 0, 0],
                 [0, 0, 1, d1],
                 [0, 0, 0, 1]])
T1
d2 = sym.symbols('d2')
theta = m.radians(-180)
T2 = sym.Matrix([[1, 0, 0, 0],
                 [0, round(m.cos(theta)), -m.sin(theta), -m.sin(theta)*d2],
                 [0, m.sin(theta), round(m.cos(theta)), round(m.cos(theta))*d2],
                 [0, 0, 0, 1]])
T2
d3 = sym.symbols('d3')
T3 = sym.Matrix([[1, 0, 0, 0],
                 [0, 1, 0, 0],
                 [0, 0, 1, d3],
                 [0, 0, 0, 1]])
T3
Tn = T1*T2*T3

