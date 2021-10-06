from sorts import insertion_sort, selection_sort, merge_sort, shell_sort
from graphics import generate_graphics
import statistics as s
import random
import time


def main():
    array_sizes = [2**i for i in range(7, 16)]
    data = []

    for size in array_sizes:
        # first_experiment
        data += first_experiment(size, 1)
        #second_experiment
        data += sort([i for i in range(size)], 2)
        #third_experiment
        data += sort(([i for i in range(size)][::-1]), 3)
        #fourth_experiment
        data += sort([random.randint(1, 3) for _ in range(size)], 4)

    generate_graphics(data)


    return "Analized!"


def first_experiment(size, experiment):

    insertion_results = []
    insertion_compar = []
    merge_results = []
    merge_compar = []
    selection_results = []
    selection_compar = []
    shell_results = []
    shell_compar = []

    for _ in range(5):
        array = [random.randint(1, size) for i in range(size)]

        start_time = time.time()
        insertion_compar.append(insertion_sort(array))
        run_time = time.time()-start_time
        insertion_results.append(run_time)

        start_time = time.time()
        merge_compar.append(merge_sort(array))
        run_time = time.time()-start_time
        merge_results.append(run_time)

        start_time = time.time()
        selection_compar.append(selection_sort(array))
        run_time = time.time()-start_time
        selection_results.append(run_time)

        start_time = time.time()
        shell_compar.append(shell_sort(array))
        run_time = time.time()-start_time
        shell_results.append(run_time)

    return [[experiment, 'Insertion', len(array), s.mean(insertion_results), s.mean(insertion_compar)], [experiment, 'Merge', len(array), s.mean(merge_results), s.mean(merge_compar)], [experiment, 'Selection', len(array), s.mean(selection_results), s.mean(selection_compar)], [experiment, 'Shell', len(array), s.mean(shell_results), s.mean(shell_compar)]]


def sort(array, experiment):

    start_time = time.time()
    insertion_compar = insertion_sort(array)
    insertion_run_time = time.time()-start_time

    start_time = time.time()
    merge_compar = merge_sort(array)
    merge_run_time = time.time()-start_time

    start_time = time.time()
    selection_compar = selection_sort(array)
    selection_run_time = time.time()-start_time

    start_time = time.time()
    shell_compar = shell_sort(array)
    shell_run_time = time.time()-start_time

    return [[experiment, 'Insertion', len(array), insertion_run_time, insertion_compar], [experiment, 'Merge', len(array), merge_run_time, merge_compar], [experiment, 'Selection', len(array), selection_run_time, selection_compar], [experiment, 'Shell', len(array), shell_run_time, shell_compar]]
    