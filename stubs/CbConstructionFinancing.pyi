class SystemCosts(object):
	def assign(self): 
		pass

	def export(self) -> Dict[Dict]
		pass

	def __init__(self, *args, **kwargs): 
		pass


	total_installed_cost = float


class FinancialParameters(object):
	def assign(self): 
		pass

	def export(self) -> Dict[Dict]
		pass

	def __init__(self, *args, **kwargs): 
		pass


	const_per_interest_rate1 = float
	const_per_interest_rate2 = float
	const_per_interest_rate3 = float
	const_per_interest_rate4 = float
	const_per_interest_rate5 = float
	const_per_months1 = float
	const_per_months2 = float
	const_per_months3 = float
	const_per_months4 = float
	const_per_months5 = float
	const_per_percent1 = float
	const_per_percent2 = float
	const_per_percent3 = float
	const_per_percent4 = float
	const_per_percent5 = float
	const_per_upfront_rate1 = float
	const_per_upfront_rate2 = float
	const_per_upfront_rate3 = float
	const_per_upfront_rate4 = float
	const_per_upfront_rate5 = float


class Outputs(object):
	def assign(self): 
		pass

	def export(self) -> Dict[Dict]
		pass

	def __init__(self, *args, **kwargs): 
		pass


	const_per_interest1 = float
	const_per_interest2 = float
	const_per_interest3 = float
	const_per_interest4 = float
	const_per_interest5 = float
	const_per_interest_total = float
	const_per_percent_total = float
	const_per_principal1 = float
	const_per_principal2 = float
	const_per_principal3 = float
	const_per_principal4 = float
	const_per_principal5 = float
	const_per_principal_total = float
	const_per_total1 = float
	const_per_total2 = float
	const_per_total3 = float
	const_per_total4 = float
	const_per_total5 = float
	construction_financing_cost = float


class CbConstructionFinancing(object):
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

	SystemCosts = SystemCosts
	FinancialParameters = FinancialParameters
	Outputs = Outputs


def default(config) -> CbConstructionFinancing
	pass

def new() -> CbConstructionFinancing
	pass

def wrap(ssc_data_t) -> CbConstructionFinancing
	pass

__loader__ = None 

__spec__ = None