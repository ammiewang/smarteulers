import math
from math import *

#this function takes all initial parameters as inputs in the terminal
def initial_h():
    t0 = float(input("Input t0: "))
    y0 = float(input("Input y0: "))
    tf = float(input("Input tf: "))
    ss = float(input("Input your desired initial step size: "))
    e = float(input("Input the maximum error rate: "))
    f = input("Input dy/dt (please look in formatting.txt to see the proper input format): ")
    return t0, y0, tf, ss, e, f

#this function executes the EM calculation of y_k+1
def calc_eulers_h(t,y,ss,f):
    return y+ss*eval(f)

#this function executes half-step Euler's method
def better_em_h(t,y,tf,ss,e,f):
    points = [(t,y)]
    while (t < tf and ss > 0) or (t > tf and ss < 0):
        em1 = calc_eulers_h(t,y,ss,f) #single step
        em2 = calc_eulers_h(t,y,ss/2,f)
        em2 = calc_eulers_h(t+ss/2,em2,ss/2,f) #half step
        error = em1-em2 #signed error
        eer = abs(error/ss) #estimated error rate
        if eer < .0000000000000000001: #we use .0000000000000000001 instead of 0 due to Python arithmetic error
            ss += .000000001
            y = calc_eulers_h(t,y,ss,f)
            t += ss
            points.append((t,y),)
        else:
            if eer <= e: #error rate <= max
                t += ss
                y = em2-error
                ss = (e/eer)*ss #recalibrate step size
                points.append((t,y),) #accept estimate
            else: #error rate > max
                ss = (e/eer)*ss #recalibrate step size
    return points

#this function executes the original Euler's method
def em_h(t,y,tf,ss,f):
    points = [(t,y)]
    while (t < tf and ss > 0) or (t > tf and ss < 0):
        em = calc_eulers_h(t,y,ss,f)
        t += ss
        y = em
        points.append((t, em),)
    return points

#t0, y0, tf, ss, e, f = initial_h()
#print(better_em_h(t0, y0, tf, ss, e, f))
#print(len(better_em(t0, y0, tf, ss, e, f)))
#print(em_h(t0, y0, tf, ss, f))
