import matplotlib.pyplot as plt
from se_derivative import *
from se_half import *
import csv

#initializes, runs, and outputs the results from all three methods to the terminal
t0, y0, tf, ss, e, f, dy, dt = initial()
deriv = better_em(t0, y0, tf, ss, e, f, dy, dt)
regular = em_h(t0, y0, tf, ss, f)
half = better_em_h(t0, y0, tf, ss, e, f)
print("\n")
print("Smart EM - Derivative Method: ", deriv)
print("\n")
print("Smart EM - Half Step Method: ", half)
print("\n")
print("Original EM: ", regular)

#separates the t and y coordinates of the derivative method
xs_d, ys_d = [], []
d_dict = []
for x,y in deriv:
    xs_d.append(x)
    ys_d.append(y)
    d_dict.append({'t': x, 'y': y})

#separates the t and y coordinates of the half-step method
xs_h, ys_h = [], []
h_dict = []
for x,y in half:
    xs_h.append(x)
    ys_h.append(y)
    h_dict.append({'t': x, 'y': y})

#separates the t and y coordinates of the original Euler's method
xs_r, ys_r = [], []
r_dict = []
for x,y in regular:
    xs_r.append(x)
    ys_r.append(y)
    r_dict.append({'t': x, 'y': y})

#plots the results of the derivative method
plt.plot(xs_d, ys_d, 'o', alpha=0.5, label='Smart EM - Derivative Method')
plt.legend(loc='best')
plt.title('Predicted Solution - Smart EM - Derivative Method')
plt.xlabel('t')
plt.ylabel('y')
plt.yscale('linear')
plt.savefig('smart_derivative.png')
plt.clf()

#plots the results of the half-step method
plt.plot(xs_h, ys_h, 'o', alpha=0.5, label='Smart EM - Half Step Method')
plt.legend(loc='best')
plt.title('Predicted Solution - Smart EM - Half Step Method')
plt.xlabel('t')
plt.ylabel('y')
plt.yscale('linear')
plt.savefig('smart_half_step.png')
plt.clf()

#plots the results of the original Euler's method
plt.plot(xs_r, ys_r, 'o', alpha=0.5, label='Original EM')
plt.legend(loc='best')
plt.title('Predicted Solution - Original EM')
plt.xlabel('t')
plt.ylabel('y')
plt.yscale('linear')
plt.savefig('original.png')
plt.clf()

#plots the results of all three methods together
plt.plot(xs_r, ys_r, 'o', alpha=0.5, label='Original EM')
plt.plot(xs_d, ys_d, 'o', alpha=0.5, label='Smart EM - Derivative Method')
plt.plot(xs_h, ys_h, 'o', alpha=0.5, label='Smart EM - Half Step Method')
plt.legend(loc='best')
plt.title('Predicted Solution')
plt.xlabel('t')
plt.ylabel('y')
plt.yscale('linear')
plt.savefig('all_three_solutions.png')
plt.clf()

#writes the estimates of all three methods into tables of (t,y) coordinates
def csvv(dicts, fieldnames, solution_type):
    with open(solution_type + ".csv", 'w', newline='') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames = fieldnames)
        writer.writeheader()
        for a in dicts:
            writer.writerow(a)

names = ('t','y')
deriv_table = csvv(d_dict, names, 'smart_deriv')
half_table = csvv(h_dict, names, 'smart_half_step')
regular_table = csvv(r_dict, names, 'original_EM')
