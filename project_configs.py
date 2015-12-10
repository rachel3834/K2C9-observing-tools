##################################################################################
#                   OBSERVING PROJECT CONFIGURATIONS
##################################################################################

from os import path
from sys import exit, argv
import observers_class
from astropy.time import Time

def read_project_configs(config_file):
    '''Function to read and parse the project configuration file.  
    File format is ASCII with the following columns separated by 
    a | character.  
    
    # ObservingProject    Location[Name, lat,long(deg),alt(m)]    Bandpass  Cadence[hrs]   ObservingPeriods   DataProduct
    
    ObservingPeriods are specified as date ranges in the format 
    yyyy-mm-dd_yyyy-mm-dd
    and multiple, comma-separated entries are supported. 
    
    Comment lines are prefixed by # and will be ignored. 
    '''
    
    # Halt here if no config is available, otherwise read the file:
    if path.isfile(config_file) == False:
        print 'ERROR: Cannot read configuration file '+config_file
	exit()
    
    file_lines = open(config_file,'r').readlines()
    
    observing_projects = {}
    
    for line in file_lines:
        if line[0:1] != '#':
	    line = clean_line(line)
	    if len(line) > 0:
	        entries = line.split('|')
	    
	        # A project may already have an entry in the dictionary, to handle projects with
	        # multiple sites.
	        if entries[0] in observing_projects.keys(): obs = observing_projects[entries[0]]
	        else:
	            obs = observers_class.ObserverProject()
	            obs.name = entries[0]
	        
	        site = observers_class.ObservingSite()
                site.name = entries[1]
                site.latitude = parse_float(entries[2])
                site.longitude = parse_float(entries[3])
                site.altitude = parse_float(entries[4])
	        obs.sites.append(site)
	    
	        obs.bandpass = entries[5]
                obs.cadence = parse_float(entries[6])
                obs.observingperiods = parse_period_list(entries[7])
	        obs.dataproduct = entries[8]
	    
	        observing_projects[obs.name] = obs
    
    return observing_projects

def clean_line(line):
    '''Function to remove whitespace characters from a line, including tabs and return characters 
    but not spaces'''
    return line.replace('\n','').replace('\t','')

def parse_period_list(entry):
    '''Function to parse a comma-separated list of observing period in the format 
    yyyy-mm-dd_yyyy-mm-dd
    '''
    periods = []
    for p in entry.split(','): 
        t_list = []
	for t in p.split('_'): t_list.append(t.lstrip().rstrip())
        t = Time(t_list, format='isot', scale='utc')
        periods.append(t)
    return periods

def parse_float(entry):
    '''Function to parse a string entry into a floating point value.  
    Returns the string if the string does not contain a valid floating point entry.'''
    
    try: value = float(entry)
    except ValueError: value = entry
    return value
    

#####################################################################
if __name__ == '__main__':
    
    if len(argv) > 1: config_file = argv[1]
    else: config_file = raw_input('Please enter the path to the observing projects configuration file: ')
    
    observing_projects = read_project_configs(config_file)
    
    for name, obs in observing_projects.items(): print obs.summary()
    
