import math
from math import *
import sympy as sym
from sympy import sympify, symbols, diff

#this function takes all initial parameters as inputs in the terminal
def initial():
    t, y = sym.symbols('t y')
    t0 = float(input("Input t0: "))
    y0 = float(input("Input y0: "))
    tf = float(input("Input tf: "))
    ss = float(input("Input your desired initial step size: "))
    e = float(input("Input the maximum error rate: "))
    f = input("Input dy/dt (please look in formatting.txt to see the proper input format): ")
    dy = str(diff(sympify(f), y))
    dt = str(diff(sympify(f), t))
    return t0, y0, tf, ss, e, f, dy, dt

#this function executes the EM calculation of y_k+1
def calc_eulers(t,y,ss,f):
    return y+ss*eval(f)

#this function returns M = max(f_y, f_t)
def estimate_error(f, t, y, dy, dt):
    dy_at_pt = eval(dy)
    dt_at_pt = eval(dt)
    if abs(dt_at_pt) > abs(dy_at_pt):
        return dt_at_pt
    else:
        return dy_at_pt

#this function executes derivative Euler's method
def better_em(t,y,tf,ss,e,f,dy,dt):
    points = [(t,y)]
    while (t < tf and ss > 0) or (t > tf and ss < 0):
        ee = abs(estimate_error(f,t,y,dy,dt))
        if ee < .0000000000000000001: #we use .0000000000000000001 instead of 0 due to Python arithmetic error
            ss += .000000001
            y = calc_eulers(t,y,ss,f)
            t += ss
            points.append((t,y),)
        else:
            estimate = abs(ee*ss)
            if .999999*estimate <= e: #error rate <= max, we use .999999 instead of 1 due to Python arithmetic error
                y = calc_eulers(t,y,ss,f)
                t += ss
                ss = (e/estimate)*ss #recalibrate step size
                points.append((t,y),) #accept estimate
            else: #error rate > max
                ss = (e/estimate)*ss #recalibrate step size
    return points

def em(t,y,tf,ss,f):
    points = [(t,y)]
    while (t < tf and ss > 0) or (t > tf and ss < 0):
        em = calc_eulers(t,y,ss,f)
        t += ss
        y = em
        points.append((t, y),)
    return points

#t0, y0, tf, ss, e, f, dy, dt = initial()
#print(better_em(t0, y0, tf, ss, e, f, dy, dt))
#print(len(better_em(t0, y0, tf, ss, e, f)))
#print(em(t0, y0, tf, ss, f))"""
