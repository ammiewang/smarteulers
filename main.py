from diffeq import EM
import time

def main():
    new_eq = EM()
    print("Half Step Method: ")
    print(new_eq.better_em_half())
    print('\n')
    print("Derivative Method: ")
    print(new_eq.better_em_deriv())
    print('\n')
    print("Original Method: ")
    print(new_eq.em())
    print('\n')

    new_eq.to_graphs_and_csv({'Derivative': new_eq.em_deriv_points, 'Half-Step': new_eq.em_half_points, \
                             'Original': new_eq.em_points}, 'All Methods')
    new_eq.to_graphs_and_csv({'Derivative': new_eq.em_deriv_points}, 'Derivative Method')
    new_eq.to_graphs_and_csv({'Half-Step': new_eq.em_deriv_points}, 'Half-Step Method')
    new_eq.to_graphs_and_csv({'Original': new_eq.em_points}, 'Original Method')

def loop_through(num_times, func, method):
    start = time.time()
    for _ in range(num_times):
        func()
    end = time.time()
    print("Method: ", method)
    print("Total Time: ", end-start)
    print("Average Time per Execution: ", (end-start)/num_times)

def timing():
    em = EM()
    method = int(input("Which method would you like to run? Input 1 for Derivative, 2 for Half-Step, 3 for Original, 4 for All: "))
    num_times = int(input("How many times would you like to run each method?"))
    first_time = True
    while (method != 1 and method != 2 and method != 3 and method != 4) or first_time:
        if method == 1:
            loop_through(num_times, em.better_em_deriv, 'Derivative')
        elif method == 2:
            loop_through(num_times, em.better_em_half, 'Half-Step')
        elif method == 3:
            loop_through(num_times, em.em, 'Original')
        elif method == 4:
            loop_through(num_times, em.better_em_deriv, 'Derivative')
            loop_through(num_times, em.better_em_half, 'Half-Step')
            loop_through(num_times, em.em, 'Original')
        else:
            method = int(input('Please input 1 (Derivative), 2 (Half-Step), 3 (Original), or 4 (All): '))
        first_time = False

#main()
#timing()
