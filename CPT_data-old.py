import os
from math import sqrt

def standard_deviation(lst, population=True):
    """Calculates the standard deviation for a list of numbers."""
    num_items = len(lst)
    mean = sum(lst) / num_items
    differences = [x - mean for x in lst]
    sq_differences = [d ** 2 for d in differences]
    ssd = sum(sq_differences)
 
    # Note: it would be better to return a value and then print it outside
    # the function, but this is just a quick way to print out the values along
    # the way.
    if population is True:
        variance = ssd / num_items
    else:
        variance = ssd / (num_items - 1)
    sd = sqrt(variance)
    return sd

def create_data_file(
        experiment_info,
        task_name,
        header='Participant number, Trial number, Task, Letter, Correct Response, Response, Correct, Accuracy,'
               'Response Time, Trial time, Trial Type'):
    file_name = experiment_info['Participant'] + '-' + experiment_info['date'] + '-' + task_name + '.csv'
    folder_name = os.path.join('Data', experiment_info['Participant'], '')
    if not os.path.exists(folder_name):
        os.makedirs(folder_name)
    file_path = '%s%s' % (folder_name, file_name)
    with open(file_path, 'w') as f:
        f.write(header)
        f.write('\n')
    return file_path


def write_data(filename, data):
    with open(filename, 'a') as f:
        row_string = ",".join(map(str, data))
        f.write(row_string + '\n')

