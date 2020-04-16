import timeit

setup = """
from se_derivative import initial, better_em, em

t0, y0, tf, ss, e, f, dy, dt = initial()

def main_better(t0, y0, tf, ss, e, f, dy, dt):
    better_em(t0, y0, tf, ss, e, f, dy, dt)

"""


t1 = timeit.Timer(stmt="main_better(t0, y0, tf, ss, e, f, dy, dt)", setup=setup)
print("Derivative Method: ", t1.timeit(10)/10)


setup2 = """
from se_half import initial_h, better_em_h, em_h

t0, y0, tf, ss, e, f = initial_h()

def main_better(t0, y0, tf, ss, e, f):
    better_em_h(t0, y0, tf, ss, e, f)

def main_em(t0, y0, tf, ss, f):
    em_h(t0, y0, tf, ss, f)


"""

t2 = timeit.Timer(stmt="main_em(t0, y0, tf, ss, f)", setup=setup2)
t3 = timeit.Timer(stmt="main_better(t0, y0, tf, ss, e, f)", setup=setup2)
print("Original Method: ", t2.timeit(10)/10)
print("Half-Step Method: ", t3.timeit(10)/10)

#Each method is currently being run 10 times and the average runtime across all 10 trials is taken.
#If you would like to increase the mount of trials, simply the t.timeit() command to t.timeit([desired number])/[desired number]
