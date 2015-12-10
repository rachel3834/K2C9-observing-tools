##################################################################################
#                   CLASS DEFINITIONS OF GROUND-BASED OBSERVERS
##################################################################################


class ObserverProject:
    '''Class describing a ground-based observing facility and its capabilities.'''
    
    def __init__(self):
        self.name = None
	self.sites = []
	self.cadence = None
        self.bandpass = None
	self.dataproduct = None
	self.observingperiods = []

    def summary(self):
        times = self.list_periods()
	sites = self.list_sites()
	if str(self.cadence).isalpha() == False: cadence = str(self.cadence) + 'hrs '
	else: cadence = str(self.cadence) + ' '
        return str(self.name) + '  ' + sites + ' ' + cadence + str(self.dataproduct) + '  ' + times
    
    def list_periods(self):
        time_list = ''
        for t in self.observingperiods:
	    if len(time_list) > 0: time_list = time_list + ', '
	    time_list = time_list + t[0].iso.split()[0] + ' - ' + t[1].iso.split()[0]
        return time_list
    
    def list_sites(self):
        sites_list = ''
	for s in self.sites: sites_list = sites_list + ' ' + s.name
	return sites_list
    
class ObservingSite:
    '''Class describing a single location on Earth from which observations are 
    made.'''
    
    def __init__(self):
        self.name = None
	self.latitude = None
	self.longitude = None
	self.altitude = None
