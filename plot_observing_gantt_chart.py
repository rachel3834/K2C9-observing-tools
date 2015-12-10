##################################################################################
#     	      	           PLOT OBSERVING GANTT CHART
#
# Code to display a Gantt chart of the ground-based observing programs supporting
# the K2/Campaign 9 Microlensing Program
##################################################################################

import project_configs
from os import path
from sys import exit, argv
import observers_class
from astropy.time import Time

def plot_gantt_chart(config_file):
    '''Function to plot a Gantt chart of the ground-based observing programs supporting
    the K2/Campaign 9 Microlensing Program.'''
    
    # Observing Project configuration contains the information to be plotted:
    observing_projects = project_configs.read_project_configs(config_file)
    
    fig = pyplot.figure(1)
    
    
    
    return True
    


##################################################################################

if __name__ == '__main__':
    
    if len(argv) > 1: config_file = argv[1]
    else: config_file = raw_input('Please enter the path to the observing projects configuration file: ')
    
    plot_gantt_chart(config_file)
