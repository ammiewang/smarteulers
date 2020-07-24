from math import *
import sympy as sym
from sympy import sympify, symbols, diff
import matplotlib.pyplot as plt
import csv

class EM:
    def __init__(self):
        t, y = sym.symbols('t y')
        self.t0 = float(input("Input t0: "))
        self.y0 = float(input("Input y0: "))
        self.tf = float(input("Input tf: "))
        self.ss = float(input("Input your desired initial step size: "))
        self.err = float(input("Input the maximum error rate: "))
        self.dydt = input("Input dy/dt (please look in formatting.txt to see the proper input format): ")
        self.dy = str(diff(sympify(self.dydt), y))
        self.dt = str(diff(sympify(self.dydt), t))
        self.existing_csvs = set({})
        self.existing_images = set({})

    def calc_eulers(self, t, y, ss):
        return y+ss*eval(self.dydt)

    #this function returns M = max(f_y, f_t)
    def estimate_error(self, t, y):
        dy_at_pt = eval(self.dy)
        dt_at_pt = eval(self.dt)
        if abs(dt_at_pt) > abs(dy_at_pt):
            return dt_at_pt
        else:
            return dy_at_pt

    def better_em_deriv(self):
        t, y, ss, e = self.t0, self.y0, self.ss, self.err
        points = [(t, y)]
        while (t < self.tf and ss > 0) or (t > self.tf and ss < 0):
            ee = abs(self.estimate_error(t,y))
            if ee < .0000000000000000001: #we use .0000000000000000001 instead of 0 due to Python arithmetic error
                ss += .000000001
                y = self.calc_eulers(t,y,ss)
                t += ss
                points.append((t,y),)
            else:
                estimate = abs(ee*ss)
                if .999999*estimate <= e: #error rate <= max, we use .999999 instead of 1 due to Python arithmetic error
                    y = self.calc_eulers(t,y,ss)
                    t += ss
                    ss = (e/estimate)*ss #recalibrate step size
                    points.append((t,y),) #accept estimate
                else: #error rate > max
                    ss = (e/estimate)*ss #recalibrate step size
        self.em_deriv_points = points
        return points

    def better_em_half(self):
        t, y, ss, e = self.t0, self.y0, self.ss, self.err
        points = [(t, y)]
        while (t < self.tf and ss > 0) or (t > self.tf and ss < 0):
            em1 = self.calc_eulers(t,y,ss) #single step
            em2 = self.calc_eulers(t,y,ss/2)
            em2 = self.calc_eulers(t+ss/2,em2,ss/2) #half step
            error = em1-em2 #signed error
            eer = abs(error/ss) #estimated error rate
            if eer < .0000000000000000001: #we use .0000000000000000001 instead of 0 due to Python arithmetic error
                ss += .000000001
                y = self.calc_eulers(t,y,ss)
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
        self.em_half_points = points
        return points

    #this function executes the original Euler's method
    def em(self):
        t, y = self.t0, self.y0
        points = [(t,y)]
        while (t < self.tf and self.ss > 0) or (t > self.tf and self.ss < 0):
            em = self.calc_eulers(t,y,self.ss)
            t += self.ss
            y = em
            points.append((t, em),)
        self.em_points = points
        return points

    def parse_points(self, points):
        xs, ys = [], []
        dict = []
        for x,y in points:
            xs.append(x)
            ys.append(y)
            dict.append({'t': x, 'y': y})
        return xs, ys, dict

    def to_graphs_and_csv(self, points_dict, title):
        for label, points in points_dict.items():
            xs, ys, dict = self.parse_points(points)
            plt.plot(xs, ys, 'o', alpha=0.5, label=label)
            if label not in self.existing_csvs:
                with open(label + ".csv", 'w', newline='') as csvfile:
                    writer = csv.DictWriter(csvfile, fieldnames = ('t','y'))
                    writer.writeheader()
                    for a in dict:
                        writer.writerow(a)
                self.existing_csvs.add(label)
            else:
                print("A .csv file for this diffeq already exists with that name.")

        if title in self.existing_images:
            print("A .png for this diffeq already exists with that name.")
            return

        plt.legend(loc='best')
        plt.title(title)
        plt.xlabel('t')
        plt.ylabel('y')
        plt.yscale('linear')
        plt.savefig(title + '.png')
        plt.clf()

        self.existing_images.add(title)
