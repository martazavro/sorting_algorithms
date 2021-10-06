import matplotlib.pyplot as plt

def generate_graphics(data):
    '''
    The function generate 8 graphics of comperison time and
    the amount of operations of sorting algoritms.
    '''
    create_graphic1_time(data)
    create_graphic1_comparisons(data)
    create_graphic2_time(data)
    create_graphic2_comparisons(data)
    create_graphic3_time(data)
    create_graphic3_comparisons(data)
    create_graphic4_time(data)
    create_graphic4_comparisons(data)


def create_graphic1_time(data):

    insertion_y = []
    merge_y = []
    selection_y = []
    shell_y = []

    x = ["2^7", "2^8", "2^9", "2^10", "2^11", "2^12", "2^13", "2^14", "2^15"]
 
    for run in data:
        if run[0] == 1 and run[1] == 'Insertion':
            insertion_y.append(run[3])
        
        elif run[0] == 1 and run[1] == 'Merge':
            merge_y.append(run[3])

        elif run[0] == 1 and run[1] == 'Selection':
            selection_y.append(run[3])

        elif run[0] == 1 and run[1] == 'Shell':
            shell_y.append(run[3])

    fig, ax = plt.subplots()
    ax.set_yscale('log')

    plt.plot(x, insertion_y, label='Insertion', color='red',
         marker='o', markerfacecolor='red')

    plt.plot(x, merge_y, label='Merge', color='blue',
         marker='o', markerfacecolor='blue')

    plt.plot(x, selection_y, label='Selection', color='green',
         marker='o', markerfacecolor='green')

    plt.plot(x, shell_y, label='Shell', color='yellow',
         marker='o', markerfacecolor='yellow')

    plt.xlabel('array size')
    plt.ylabel('time')
    
    plt.title('Experiment 1 (random array): time')
    plt.legend()
    plt.show()


def create_graphic1_comparisons(data):


    insertion_y = []
    merge_y = []
    selection_y = []
    shell_y = []

    x = ["2^7", "2^8", "2^9", "2^10", "2^11", "2^12", "2^13", "2^14", "2^15"]
 
    for run in data:
        if run[0] == 1 and run[1] == 'Insertion':
            insertion_y.append(run[4])
        
        elif run[0] == 1 and run[1] == 'Merge':
            merge_y.append(run[4])

        elif run[0] == 1 and run[1] == 'Selection':
            selection_y.append(run[4])

        elif run[0] == 1 and run[1] == 'Shell':
            shell_y.append(run[4])

    fig, ax = plt.subplots()
    ax.set_yscale('log')

    plt.plot(x, insertion_y, label='Insertion', color='red',
         marker='o', markerfacecolor='red')

    plt.plot(x, merge_y, label='Merge', color='blue',
         marker='o', markerfacecolor='blue')

    plt.plot(x, selection_y, label='Selection', color='green',
         marker='o', markerfacecolor='green')

    plt.plot(x, shell_y, label='Shell', color='yellow',
         marker='o', markerfacecolor='yellow')

    plt.xlabel('array size')
    plt.ylabel('number of comparisons')
    
    plt.title('Experiment 1 (random array): comparisons')
    plt.legend()
    plt.show()


def create_graphic2_time(data):

    insertion_y = []
    merge_y = []
    selection_y = []
    shell_y = []

    x = ["2^7", "2^8", "2^9", "2^10", "2^11", "2^12", "2^13", "2^14", "2^15"]
 
    for run in data:
        if run[0] == 2 and run[1] == 'Insertion':
            insertion_y.append(run[3])
        
        elif run[0] == 2 and run[1] == 'Merge':
            merge_y.append(run[3])

        elif run[0] == 2 and run[1] == 'Selection':
            selection_y.append(run[3])

        elif run[0] == 2 and run[1] == 'Shell':
            shell_y.append(run[3])

    fig, ax = plt.subplots()
    ax.set_yscale('log')

    plt.plot(x, insertion_y, label='Insertion', color='red',
         marker='o', markerfacecolor='red')

    plt.plot(x, merge_y, label='Merge', color='blue',
         marker='o', markerfacecolor='blue')

    plt.plot(x, selection_y, label='Selection', color='green',
         marker='o', markerfacecolor='green')

    plt.plot(x, shell_y, label='Shell', color='yellow',
         marker='o', markerfacecolor='yellow')

    plt.xlabel('array size')
    plt.ylabel('time')
    
    plt.title('Experiment 2 (sorted in increasing order array): time')
    plt.legend()
    plt.show()


def create_graphic2_comparisons(data):

    insertion_y = []
    merge_y = []
    selection_y = []
    shell_y = []

    x = ["2^7", "2^8", "2^9", "2^10", "2^11", "2^12", "2^13", "2^14", "2^15"]
 
    for run in data:
        if run[0] == 2 and run[1] == 'Insertion':
            insertion_y.append(run[4])
        
        elif run[0] == 2 and run[1] == 'Merge':
            merge_y.append(run[4])

        elif run[0] == 2 and run[1] == 'Selection':
            selection_y.append(run[4])

        elif run[0] == 2 and run[1] == 'Shell':
            shell_y.append(run[4])

    fig, ax = plt.subplots()
    ax.set_yscale('log')

    plt.plot(x, insertion_y, label='Insertion', color='red',
         marker='o', markerfacecolor='red')

    plt.plot(x, merge_y, label='Merge', color='blue',
         marker='o', markerfacecolor='blue')

    plt.plot(x, selection_y, label='Selection', color='green',
         marker='o', markerfacecolor='green')

    plt.plot(x, shell_y, label='Shell', color='yellow',
         marker='o', markerfacecolor='yellow')

    plt.xlabel('array size')
    plt.ylabel('number of comparisons')
    
    plt.title('Experiment 2 (sorted in increasing order array): comparisons')
    plt.legend()
    plt.show()




def create_graphic3_time(data):

    insertion_y = []
    merge_y = []
    selection_y = []
    shell_y = []

    x = ["2^7", "2^8", "2^9", "2^10", "2^11", "2^12", "2^13", "2^14", "2^15"]
 
    for run in data:
        if run[0] == 3 and run[1] == 'Insertion':
            insertion_y.append(run[3])
        
        elif run[0] == 3 and run[1] == 'Merge':
            merge_y.append(run[3])

        elif run[0] == 3 and run[1] == 'Selection':
            selection_y.append(run[3])

        elif run[0] == 3 and run[1] == 'Shell':
            shell_y.append(run[3])

    fig, ax = plt.subplots()
    ax.set_yscale('log')

    plt.plot(x, insertion_y, label='Insertion', color='red',
         marker='o', markerfacecolor='red')

    plt.plot(x, merge_y, label='Merge', color='blue',
         marker='o', markerfacecolor='blue')

    plt.plot(x, selection_y, label='Selection', color='green',
         marker='o', markerfacecolor='green')

    plt.plot(x, shell_y, label='Shell', color='yellow',
         marker='o', markerfacecolor='yellow')

    plt.xlabel('array size')
    plt.ylabel('time')
    
    plt.title('Experiment 3 (sorted in decsential order array): time')
    plt.legend()
    plt.show()

def create_graphic3_comparisons(data):

    insertion_y = []
    merge_y = []
    selection_y = []
    shell_y = []

    x = ["2^7", "2^8", "2^9", "2^10", "2^11", "2^12", "2^13", "2^14", "2^15"]
 
    for run in data:
        if run[0] == 3 and run[1] == 'Insertion':
            insertion_y.append(run[4])
        
        elif run[0] == 3 and run[1] == 'Merge':
            merge_y.append(run[4])

        elif run[0] == 3 and run[1] == 'Selection':
            selection_y.append(run[4])

        elif run[0] == 3 and run[1] == 'Shell':
            shell_y.append(run[4])

    fig, ax = plt.subplots()
    ax.set_yscale('log')

    plt.plot(x, insertion_y, label='Insertion', color='red',
         marker='o', markerfacecolor='red')

    plt.plot(x, merge_y, label='Merge', color='blue',
         marker='o', markerfacecolor='blue')

    plt.plot(x, selection_y, label='Selection', color='green',
         marker='o', markerfacecolor='green')

    plt.plot(x, shell_y, label='Shell', color='yellow',
         marker='o', markerfacecolor='yellow')

    plt.xlabel('array size')
    plt.ylabel('number of comparisons')
    
    plt.title('Experiment 3 (sorted in decsential order array): comparisons')

    plt.legend()
    plt.show()



def create_graphic4_time(data):

    insertion_y = []
    merge_y = []
    selection_y = []
    shell_y = []

    x = ["2^7", "2^8", "2^9", "2^10", "2^11", "2^12", "2^13", "2^14", "2^15"]
 
    for run in data:
        if run[0] == 4 and run[1] == 'Insertion':
            insertion_y.append(run[3])
        
        elif run[0] == 4 and run[1] == 'Merge':
            merge_y.append(run[3])

        elif run[0] == 4 and run[1] == 'Selection':
            selection_y.append(run[3])

        elif run[0] == 4 and run[1] == 'Shell':
            shell_y.append(run[3])

    fig, ax = plt.subplots()
    ax.set_yscale('log')

    plt.plot(x, insertion_y, label='Insertion', color='red',
         marker='o', markerfacecolor='red')

    plt.plot(x, merge_y, label='Merge', color='blue',
         marker='o', markerfacecolor='blue')

    plt.plot(x, selection_y, label='Selection', color='green',
         marker='o', markerfacecolor='green')

    plt.plot(x, shell_y, label='Shell', color='yellow',
         marker='o', markerfacecolor='yellow')

    plt.xlabel('array size')
    plt.ylabel('time')
    
    plt.title('Experiment 4 (array of {1, 2, 3}): time')
    plt.legend()
    plt.show()


def create_graphic4_comparisons(data):

    insertion_y = []
    merge_y = []
    selection_y = []
    shell_y = []

    x = ["2^7", "2^8", "2^9", "2^10", "2^11", "2^12", "2^13", "2^14", "2^15"]
 
    for run in data:
        if run[0] == 4 and run[1] == 'Insertion':
            insertion_y.append(run[4])
        
        elif run[0] == 4 and run[1] == 'Merge':
            merge_y.append(run[4])

        elif run[0] == 4 and run[1] == 'Selection':
            selection_y.append(run[4])

        elif run[0] == 4 and run[1] == 'Shell':
            shell_y.append(run[4])

    fig, ax = plt.subplots()
    ax.set_yscale('log')

    plt.plot(x, insertion_y, label='Insertion', color='red',
         marker='o', markerfacecolor='red')

    plt.plot(x, merge_y, label='Merge', color='blue',
         marker='o', markerfacecolor='blue')

    plt.plot(x, selection_y, label='Selection', color='green',
         marker='o', markerfacecolor='green')

    plt.plot(x, shell_y, label='Shell', color='yellow',
         marker='o', markerfacecolor='yellow')

    plt.xlabel('array size')
    plt.ylabel('number of comparisons')
    
    plt.title('Experiment 4 (array of {1, 2, 3}): comparisons')
    plt.legend()
    plt.show()
