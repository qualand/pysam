class PVWatts(object):
	def assign(self): 
		pass

	def export(self) -> Dict[Dict]
		pass

	def __init__(self, *args, **kwargs): 
		pass


	alb = float
	beam = float
	day = float
	diffuse = float
	hour = float
	lat = float
	lon = float
	minute = float
	month = float
	poa = float
	tamb = float
	tcell = float
	time_step = float
	tz = float
	wspd = float
	year = float


class SystemDesign(object):
	def assign(self): 
		pass

	def export(self) -> Dict[Dict]
		pass

	def __init__(self, *args, **kwargs): 
		pass


	array_type = float
	azimuth = float
	dc_ac_ratio = float
	gcr = float
	inv_eff = float
	losses = float
	module_type = float
	system_capacity = float
	tilt = float


class Outputs(object):
	def assign(self): 
		pass

	def export(self) -> Dict[Dict]
		pass

	def __init__(self, *args, **kwargs): 
		pass


	ac = float
	dc = float


class Pvwattsv51ts(object):
	def assign(self, dict):
		pass

	def execute(self, int_verbosity):
		pass

	def export(self):
		pass

	def __getattribute__(self, *args, **kwargs):
		pass

	def __init__(self, *args, **kwargs):
		pass

	PVWatts = PVWatts
	SystemDesign = SystemDesign
	Outputs = Outputs


def default(config) -> Pvwattsv51ts
	pass

def new() -> Pvwattsv51ts
	pass

def wrap(ssc_data_t) -> Pvwattsv51ts
	pass

__loader__ = None 

__spec__ = None