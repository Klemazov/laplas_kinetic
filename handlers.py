import numpy as np
def change_to_linear(T,betta):
    y = np.log(betta/T**2)
    x = 1000/T
    return x,y


def open_DSC(name_of_file, encoding='utf-16', skip_header=49):
    """
    TODO description of function
    type of data: ndarray
    """
    data = np.genfromtxt(name_of_file, encoding=encoding, skip_header=skip_header).T
    time = data[0]
    temperature = data[1]+273.15
    heat_flow = data[2]
    return time, temperature, heat_flow

def mask(min_range, max_range, value):
    value_masked = None
    return value_masked

def area(massive_x, massive_y):
    area_massive = None
    return area_massive

def subtracted(DSC_curve):
    return subtracted_value

def kissinger(heating_rates, temperature_peaks):
    return Ea, Std, R2

def friedman(temperature, DSC_curve):
    y = np.log(subtracted(DSC_curve)/area())
    x = 1000/temperature[mask]
    return x,y
