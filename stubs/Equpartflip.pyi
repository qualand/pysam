class FinancialParameters(object):
	def assign(self): 
		pass

	def export(self) -> Dict[Dict]
		pass

	def __init__(self, *args, **kwargs): 
		pass

	analysis_period = float
	federal_tax_rate = tuple
	inflation_rate = float
	insurance_rate = float
	prop_tax_assessed_decline = float
	prop_tax_cost_assessed_percent = float
	property_tax_rate = float
	real_discount_rate = float
	state_tax_rate = tuple
	system_capacity = float
	system_heat_rate = float


class SystemCosts(object):
	def assign(self): 
		pass

	def export(self) -> Dict[Dict]
		pass

	def __init__(self, *args, **kwargs): 
		pass

	add_om_num_types = float
	annual_fuel_usage = float
	om_capacity = tuple
	om_capacity1 = tuple
	om_capacity1_nameplate = float
	om_capacity2 = tuple
	om_capacity2_nameplate = float
	om_capacity_escal = float
	om_fixed = tuple
	om_fixed1 = tuple
	om_fixed2 = tuple
	om_fixed_escal = float
	om_fuel_cost = tuple
	om_fuel_cost_escal = float
	om_opt_fuel_1_cost = tuple
	om_opt_fuel_1_cost_escal = float
	om_opt_fuel_1_usage = float
	om_opt_fuel_2_cost = tuple
	om_opt_fuel_2_cost_escal = float
	om_opt_fuel_2_usage = float
	om_production = tuple
	om_production1 = tuple
	om_production1_values = tuple
	om_production2 = tuple
	om_production2_values = tuple
	om_production_escal = float
	om_replacement_cost1 = tuple
	om_replacement_cost2 = tuple
	om_replacement_cost_escal = float
	total_installed_cost = float


class TaxCreditIncentives(object):
	def assign(self): 
		pass

	def export(self) -> Dict[Dict]
		pass

	def __init__(self, *args, **kwargs): 
		pass

	itc_fed_amount = float
	itc_fed_amount_deprbas_fed = float
	itc_fed_amount_deprbas_sta = float
	itc_fed_percent = float
	itc_fed_percent_deprbas_fed = float
	itc_fed_percent_deprbas_sta = float
	itc_fed_percent_maxvalue = float
	itc_sta_amount = float
	itc_sta_amount_deprbas_fed = float
	itc_sta_amount_deprbas_sta = float
	itc_sta_percent = float
	itc_sta_percent_deprbas_fed = float
	itc_sta_percent_deprbas_sta = float
	itc_sta_percent_maxvalue = float
	ptc_fed_amount = tuple
	ptc_fed_escal = float
	ptc_fed_term = float
	ptc_sta_amount = tuple
	ptc_sta_escal = float
	ptc_sta_term = float


class PaymentIncentives(object):
	def assign(self): 
		pass

	def export(self) -> Dict[Dict]
		pass

	def __init__(self, *args, **kwargs): 
		pass

	cbi_fed_amount = float
	cbi_fed_deprbas_fed = float
	cbi_fed_deprbas_sta = float
	cbi_fed_maxvalue = float
	cbi_fed_tax_fed = float
	cbi_fed_tax_sta = float
	cbi_oth_amount = float
	cbi_oth_deprbas_fed = float
	cbi_oth_deprbas_sta = float
	cbi_oth_maxvalue = float
	cbi_oth_tax_fed = float
	cbi_oth_tax_sta = float
	cbi_sta_amount = float
	cbi_sta_deprbas_fed = float
	cbi_sta_deprbas_sta = float
	cbi_sta_maxvalue = float
	cbi_sta_tax_fed = float
	cbi_sta_tax_sta = float
	cbi_uti_amount = float
	cbi_uti_deprbas_fed = float
	cbi_uti_deprbas_sta = float
	cbi_uti_maxvalue = float
	cbi_uti_tax_fed = float
	cbi_uti_tax_sta = float
	ibi_fed_amount = float
	ibi_fed_amount_deprbas_fed = float
	ibi_fed_amount_deprbas_sta = float
	ibi_fed_amount_tax_fed = float
	ibi_fed_amount_tax_sta = float
	ibi_fed_percent = float
	ibi_fed_percent_deprbas_fed = float
	ibi_fed_percent_deprbas_sta = float
	ibi_fed_percent_maxvalue = float
	ibi_fed_percent_tax_fed = float
	ibi_fed_percent_tax_sta = float
	ibi_oth_amount = float
	ibi_oth_amount_deprbas_fed = float
	ibi_oth_amount_deprbas_sta = float
	ibi_oth_amount_tax_fed = float
	ibi_oth_amount_tax_sta = float
	ibi_oth_percent = float
	ibi_oth_percent_deprbas_fed = float
	ibi_oth_percent_deprbas_sta = float
	ibi_oth_percent_maxvalue = float
	ibi_oth_percent_tax_fed = float
	ibi_oth_percent_tax_sta = float
	ibi_sta_amount = float
	ibi_sta_amount_deprbas_fed = float
	ibi_sta_amount_deprbas_sta = float
	ibi_sta_amount_tax_fed = float
	ibi_sta_amount_tax_sta = float
	ibi_sta_percent = float
	ibi_sta_percent_deprbas_fed = float
	ibi_sta_percent_deprbas_sta = float
	ibi_sta_percent_maxvalue = float
	ibi_sta_percent_tax_fed = float
	ibi_sta_percent_tax_sta = float
	ibi_uti_amount = float
	ibi_uti_amount_deprbas_fed = float
	ibi_uti_amount_deprbas_sta = float
	ibi_uti_amount_tax_fed = float
	ibi_uti_amount_tax_sta = float
	ibi_uti_percent = float
	ibi_uti_percent_deprbas_fed = float
	ibi_uti_percent_deprbas_sta = float
	ibi_uti_percent_maxvalue = float
	ibi_uti_percent_tax_fed = float
	ibi_uti_percent_tax_sta = float
	pbi_fed_amount = tuple
	pbi_fed_escal = float
	pbi_fed_tax_fed = float
	pbi_fed_tax_sta = float
	pbi_fed_term = float
	pbi_oth_amount = tuple
	pbi_oth_escal = float
	pbi_oth_tax_fed = float
	pbi_oth_tax_sta = float
	pbi_oth_term = float
	pbi_sta_amount = tuple
	pbi_sta_escal = float
	pbi_sta_tax_fed = float
	pbi_sta_tax_sta = float
	pbi_sta_term = float
	pbi_uti_amount = tuple
	pbi_uti_escal = float
	pbi_uti_tax_fed = float
	pbi_uti_tax_sta = float
	pbi_uti_term = float


class SystemOutput(object):
	def assign(self): 
		pass

	def export(self) -> Dict[Dict]
		pass

	def __init__(self, *args, **kwargs): 
		pass

	degradation = tuple
	gen = tuple
	system_capacity = float


class Recapitalization(object):
	def assign(self): 
		pass

	def export(self) -> Dict[Dict]
		pass

	def __init__(self, *args, **kwargs): 
		pass

	system_lifetime_recapitalize = tuple
	system_recapitalization_cost = float
	system_recapitalization_escalation = float
	system_use_recapitalization = float


class TimeOfDelivery(object):
	def assign(self): 
		pass

	def export(self) -> Dict[Dict]
		pass

	def __init__(self, *args, **kwargs): 
		pass

	dispatch_factor1 = float
	dispatch_factor2 = float
	dispatch_factor3 = float
	dispatch_factor4 = float
	dispatch_factor5 = float
	dispatch_factor6 = float
	dispatch_factor7 = float
	dispatch_factor8 = float
	dispatch_factor9 = float
	dispatch_factors_ts = tuple
	dispatch_sched_weekday = tuple
	dispatch_sched_weekend = tuple
	ppa_multiplier_model = float
	system_use_lifetime_output = float


class ReserveAccounts(object):
	def assign(self): 
		pass

	def export(self) -> Dict[Dict]
		pass

	def __init__(self, *args, **kwargs): 
		pass

	equip1_reserve_cost = float
	equip1_reserve_freq = float
	equip2_reserve_cost = float
	equip2_reserve_freq = float
	equip3_reserve_cost = float
	equip3_reserve_freq = float
	reserves_interest = float


class Depreciation(object):
	def assign(self): 
		pass

	def export(self) -> Dict[Dict]
		pass

	def __init__(self, *args, **kwargs): 
		pass

	depr_alloc_custom_percent = float
	depr_alloc_macrs_15_percent = float
	depr_alloc_macrs_5_percent = float
	depr_alloc_sl_15_percent = float
	depr_alloc_sl_20_percent = float
	depr_alloc_sl_39_percent = float
	depr_alloc_sl_5_percent = float
	depr_bonus_fed = float
	depr_bonus_fed_custom = float
	depr_bonus_fed_macrs_15 = float
	depr_bonus_fed_macrs_5 = float
	depr_bonus_fed_sl_15 = float
	depr_bonus_fed_sl_20 = float
	depr_bonus_fed_sl_39 = float
	depr_bonus_fed_sl_5 = float
	depr_bonus_sta = float
	depr_bonus_sta_custom = float
	depr_bonus_sta_macrs_15 = float
	depr_bonus_sta_macrs_5 = float
	depr_bonus_sta_sl_15 = float
	depr_bonus_sta_sl_20 = float
	depr_bonus_sta_sl_39 = float
	depr_bonus_sta_sl_5 = float
	depr_custom_schedule = tuple
	depr_fedbas_method = float
	depr_itc_fed_custom = float
	depr_itc_fed_macrs_15 = float
	depr_itc_fed_macrs_5 = float
	depr_itc_fed_sl_15 = float
	depr_itc_fed_sl_20 = float
	depr_itc_fed_sl_39 = float
	depr_itc_fed_sl_5 = float
	depr_itc_sta_custom = float
	depr_itc_sta_macrs_15 = float
	depr_itc_sta_macrs_5 = float
	depr_itc_sta_sl_15 = float
	depr_itc_sta_sl_20 = float
	depr_itc_sta_sl_39 = float
	depr_itc_sta_sl_5 = float
	depr_stabas_method = float
	equip_reserve_depr_fed = float
	equip_reserve_depr_sta = float


class SalvageValue(object):
	def assign(self): 
		pass

	def export(self) -> Dict[Dict]
		pass

	def __init__(self, *args, **kwargs): 
		pass

	salvage_percentage = float


class SolutionMode(object):
	def assign(self): 
		pass

	def export(self) -> Dict[Dict]
		pass

	def __init__(self, *args, **kwargs): 
		pass

	ppa_escalation = float
	ppa_price_input = float
	ppa_soln_max = float
	ppa_soln_max_iterations = float
	ppa_soln_min = float
	ppa_soln_mode = float
	ppa_soln_tolerance = float


class ConstructionFinancing(object):
	def assign(self): 
		pass

	def export(self) -> Dict[Dict]
		pass

	def __init__(self, *args, **kwargs): 
		pass

	construction_financing_cost = float


class OtherCapitalCosts(object):
	def assign(self): 
		pass

	def export(self) -> Dict[Dict]
		pass

	def __init__(self, *args, **kwargs): 
		pass

	cost_dev_fee_percent = float
	cost_equity_closing = float
	cost_other_financing = float
	months_receivables_reserve = float
	months_working_reserve = float


class IRRTargets(object):
	def assign(self): 
		pass

	def export(self) -> Dict[Dict]
		pass

	def __init__(self, *args, **kwargs): 
		pass

	flip_target_percent = float
	flip_target_year = float
	tax_investor_equity_percent = float
	tax_investor_postflip_cash_percent = float
	tax_investor_postflip_tax_percent = float
	tax_investor_preflip_cash_percent = float
	tax_investor_preflip_tax_percent = float


class DeveloperCapitalRecovery(object):
	def assign(self): 
		pass

	def export(self) -> Dict[Dict]
		pass

	def __init__(self, *args, **kwargs): 
		pass

	sponsor_cap_recovery_mode = float
	sponsor_cap_recovery_year = float


class Battery(object):
	def assign(self): 
		pass

	def export(self) -> Dict[Dict]
		pass

	def __init__(self, *args, **kwargs): 
		pass

	batt_bank_replacement = tuple
	batt_computed_bank_capacity = float
	batt_replacement_option = float
	batt_replacement_schedule = tuple
	battery_per_kWh = float
	en_batt = float


class Outputs(object):
	def assign(self): 
		pass

	def export(self) -> Dict[Dict]
		pass

	def __init__(self, *args, **kwargs): 
		pass

	adjusted_installed_cost = float
	analysis_period_irr = float
	cbi_fedtax_total = float
	cbi_statax_total = float
	cbi_total = float
	cbi_total_fed = float
	cbi_total_oth = float
	cbi_total_sta = float
	cbi_total_uti = float
	cf_annual_costs = tuple
	cf_battery_replacement_cost = tuple
	cf_battery_replacement_cost_schedule = tuple
	cf_disbursement_equip1 = tuple
	cf_disbursement_equip2 = tuple
	cf_disbursement_equip3 = tuple
	cf_disbursement_om = tuple
	cf_disbursement_receivables = tuple
	cf_ebitda = tuple
	cf_effective_tax_frac = tuple
	cf_energy_net = tuple
	cf_energy_net_apr = tuple
	cf_energy_net_aug = tuple
	cf_energy_net_dec = tuple
	cf_energy_net_dispatch1 = tuple
	cf_energy_net_dispatch2 = tuple
	cf_energy_net_dispatch3 = tuple
	cf_energy_net_dispatch4 = tuple
	cf_energy_net_dispatch5 = tuple
	cf_energy_net_dispatch6 = tuple
	cf_energy_net_dispatch7 = tuple
	cf_energy_net_dispatch8 = tuple
	cf_energy_net_dispatch9 = tuple
	cf_energy_net_feb = tuple
	cf_energy_net_jan = tuple
	cf_energy_net_jul = tuple
	cf_energy_net_jun = tuple
	cf_energy_net_mar = tuple
	cf_energy_net_may = tuple
	cf_energy_net_monthly_firstyear_TOD1 = tuple
	cf_energy_net_monthly_firstyear_TOD2 = tuple
	cf_energy_net_monthly_firstyear_TOD3 = tuple
	cf_energy_net_monthly_firstyear_TOD4 = tuple
	cf_energy_net_monthly_firstyear_TOD5 = tuple
	cf_energy_net_monthly_firstyear_TOD6 = tuple
	cf_energy_net_monthly_firstyear_TOD7 = tuple
	cf_energy_net_monthly_firstyear_TOD8 = tuple
	cf_energy_net_monthly_firstyear_TOD9 = tuple
	cf_energy_net_nov = tuple
	cf_energy_net_oct = tuple
	cf_energy_net_sep = tuple
	cf_energy_value = tuple
	cf_feddepr_custom = tuple
	cf_feddepr_macrs_15 = tuple
	cf_feddepr_macrs_5 = tuple
	cf_feddepr_me1 = tuple
	cf_feddepr_me2 = tuple
	cf_feddepr_me3 = tuple
	cf_feddepr_sl_15 = tuple
	cf_feddepr_sl_20 = tuple
	cf_feddepr_sl_39 = tuple
	cf_feddepr_sl_5 = tuple
	cf_feddepr_total = tuple
	cf_federal_tax_frac = tuple
	cf_fedtax = tuple
	cf_fedtax_income_prior_incentives = tuple
	cf_fedtax_income_with_incentives = tuple
	cf_fedtax_taxable_incentives = tuple
	cf_funding_equip1 = tuple
	cf_funding_equip2 = tuple
	cf_funding_equip3 = tuple
	cf_funding_om = tuple
	cf_funding_receivables = tuple
	cf_insurance_expense = tuple
	cf_length = float
	cf_net_salvage_value = tuple
	cf_om_capacity_expense = tuple
	cf_om_fixed_expense = tuple
	cf_om_fuel_expense = tuple
	cf_om_opt_fuel_1_expense = tuple
	cf_om_opt_fuel_2_expense = tuple
	cf_om_production_expense = tuple
	cf_operating_expenses = tuple
	cf_pbi_fedtax_total = tuple
	cf_pbi_statax_total = tuple
	cf_pbi_total = tuple
	cf_pbi_total_fed = tuple
	cf_pbi_total_oth = tuple
	cf_pbi_total_sta = tuple
	cf_pbi_total_uti = tuple
	cf_ppa_price = tuple
	cf_pretax_cashflow = tuple
	cf_project_financing_activities = tuple
	cf_project_investing_activities = tuple
	cf_project_me1cs = tuple
	cf_project_me1ra = tuple
	cf_project_me2cs = tuple
	cf_project_me2ra = tuple
	cf_project_me3cs = tuple
	cf_project_me3ra = tuple
	cf_project_mecs = tuple
	cf_project_operating_activities = tuple
	cf_project_ra = tuple
	cf_project_receivablesra = tuple
	cf_project_return_aftertax = tuple
	cf_project_return_aftertax_cash = tuple
	cf_project_return_aftertax_irr = tuple
	cf_project_return_aftertax_npv = tuple
	cf_project_return_pretax = tuple
	cf_project_return_pretax_irr = tuple
	cf_project_return_pretax_npv = tuple
	cf_project_wcra = tuple
	cf_property_tax_assessed_value = tuple
	cf_property_tax_expense = tuple
	cf_ptc_fed = tuple
	cf_ptc_sta = tuple
	cf_recapitalization = tuple
	cf_reserve_equip1 = tuple
	cf_reserve_equip2 = tuple
	cf_reserve_equip3 = tuple
	cf_reserve_interest = tuple
	cf_reserve_om = tuple
	cf_reserve_receivables = tuple
	cf_reserve_total = tuple
	cf_revenue_apr = tuple
	cf_revenue_aug = tuple
	cf_revenue_dec = tuple
	cf_revenue_dispatch1 = tuple
	cf_revenue_dispatch2 = tuple
	cf_revenue_dispatch3 = tuple
	cf_revenue_dispatch4 = tuple
	cf_revenue_dispatch5 = tuple
	cf_revenue_dispatch6 = tuple
	cf_revenue_dispatch7 = tuple
	cf_revenue_dispatch8 = tuple
	cf_revenue_dispatch9 = tuple
	cf_revenue_feb = tuple
	cf_revenue_jan = tuple
	cf_revenue_jul = tuple
	cf_revenue_jun = tuple
	cf_revenue_mar = tuple
	cf_revenue_may = tuple
	cf_revenue_monthly_firstyear_TOD1 = tuple
	cf_revenue_monthly_firstyear_TOD2 = tuple
	cf_revenue_monthly_firstyear_TOD3 = tuple
	cf_revenue_monthly_firstyear_TOD4 = tuple
	cf_revenue_monthly_firstyear_TOD5 = tuple
	cf_revenue_monthly_firstyear_TOD6 = tuple
	cf_revenue_monthly_firstyear_TOD7 = tuple
	cf_revenue_monthly_firstyear_TOD8 = tuple
	cf_revenue_monthly_firstyear_TOD9 = tuple
	cf_revenue_nov = tuple
	cf_revenue_oct = tuple
	cf_revenue_sep = tuple
	cf_sponsor_aftertax = tuple
	cf_sponsor_aftertax_cash = tuple
	cf_sponsor_aftertax_irr = tuple
	cf_sponsor_aftertax_itc = tuple
	cf_sponsor_aftertax_npv = tuple
	cf_sponsor_aftertax_ptc = tuple
	cf_sponsor_aftertax_tax = tuple
	cf_sponsor_capital_recovery_balance = tuple
	cf_sponsor_capital_recovery_cash = tuple
	cf_sponsor_pretax = tuple
	cf_sponsor_pretax_cash_during_recovery = tuple
	cf_sponsor_pretax_cash_post_recovery = tuple
	cf_sponsor_pretax_irr = tuple
	cf_sponsor_pretax_npv = tuple
	cf_stadepr_custom = tuple
	cf_stadepr_macrs_15 = tuple
	cf_stadepr_macrs_5 = tuple
	cf_stadepr_me1 = tuple
	cf_stadepr_me2 = tuple
	cf_stadepr_me3 = tuple
	cf_stadepr_sl_15 = tuple
	cf_stadepr_sl_20 = tuple
	cf_stadepr_sl_39 = tuple
	cf_stadepr_sl_5 = tuple
	cf_stadepr_total = tuple
	cf_statax = tuple
	cf_statax_income_prior_incentives = tuple
	cf_statax_income_with_incentives = tuple
	cf_statax_taxable_incentives = tuple
	cf_state_tax_frac = tuple
	cf_tax_investor_aftertax = tuple
	cf_tax_investor_aftertax_cash = tuple
	cf_tax_investor_aftertax_irr = tuple
	cf_tax_investor_aftertax_itc = tuple
	cf_tax_investor_aftertax_max_irr = tuple
	cf_tax_investor_aftertax_npv = tuple
	cf_tax_investor_aftertax_ptc = tuple
	cf_tax_investor_aftertax_tax = tuple
	cf_tax_investor_pretax = tuple
	cf_tax_investor_pretax_irr = tuple
	cf_tax_investor_pretax_npv = tuple
	cf_total_revenue = tuple
	cost_financing = float
	cost_installed = float
	cost_installedperwatt = float
	cost_prefinancing = float
	debt_fraction = float
	depr_alloc_custom = float
	depr_alloc_macrs_15 = float
	depr_alloc_macrs_5 = float
	depr_alloc_none = float
	depr_alloc_none_percent = float
	depr_alloc_sl_15 = float
	depr_alloc_sl_20 = float
	depr_alloc_sl_39 = float
	depr_alloc_sl_5 = float
	depr_alloc_total = float
	depr_fedbas_after_itc_custom = float
	depr_fedbas_after_itc_macrs_15 = float
	depr_fedbas_after_itc_macrs_5 = float
	depr_fedbas_after_itc_sl_15 = float
	depr_fedbas_after_itc_sl_20 = float
	depr_fedbas_after_itc_sl_39 = float
	depr_fedbas_after_itc_sl_5 = float
	depr_fedbas_after_itc_total = float
	depr_fedbas_cbi_reduc_custom = float
	depr_fedbas_cbi_reduc_macrs_15 = float
	depr_fedbas_cbi_reduc_macrs_5 = float
	depr_fedbas_cbi_reduc_sl_15 = float
	depr_fedbas_cbi_reduc_sl_20 = float
	depr_fedbas_cbi_reduc_sl_39 = float
	depr_fedbas_cbi_reduc_sl_5 = float
	depr_fedbas_cbi_reduc_total = float
	depr_fedbas_custom = float
	depr_fedbas_first_year_bonus_custom = float
	depr_fedbas_first_year_bonus_macrs_15 = float
	depr_fedbas_first_year_bonus_macrs_5 = float
	depr_fedbas_first_year_bonus_sl_15 = float
	depr_fedbas_first_year_bonus_sl_20 = float
	depr_fedbas_first_year_bonus_sl_39 = float
	depr_fedbas_first_year_bonus_sl_5 = float
	depr_fedbas_first_year_bonus_total = float
	depr_fedbas_fixed_amount_custom = float
	depr_fedbas_fixed_amount_macrs_15 = float
	depr_fedbas_fixed_amount_macrs_5 = float
	depr_fedbas_fixed_amount_sl_15 = float
	depr_fedbas_fixed_amount_sl_20 = float
	depr_fedbas_fixed_amount_sl_39 = float
	depr_fedbas_fixed_amount_sl_5 = float
	depr_fedbas_fixed_amount_total = float
	depr_fedbas_ibi_reduc_custom = float
	depr_fedbas_ibi_reduc_macrs_15 = float
	depr_fedbas_ibi_reduc_macrs_5 = float
	depr_fedbas_ibi_reduc_sl_15 = float
	depr_fedbas_ibi_reduc_sl_20 = float
	depr_fedbas_ibi_reduc_sl_39 = float
	depr_fedbas_ibi_reduc_sl_5 = float
	depr_fedbas_ibi_reduc_total = float
	depr_fedbas_itc_fed_reduction_custom = float
	depr_fedbas_itc_fed_reduction_macrs_15 = float
	depr_fedbas_itc_fed_reduction_macrs_5 = float
	depr_fedbas_itc_fed_reduction_sl_15 = float
	depr_fedbas_itc_fed_reduction_sl_20 = float
	depr_fedbas_itc_fed_reduction_sl_39 = float
	depr_fedbas_itc_fed_reduction_sl_5 = float
	depr_fedbas_itc_fed_reduction_total = float
	depr_fedbas_itc_sta_reduction_custom = float
	depr_fedbas_itc_sta_reduction_macrs_15 = float
	depr_fedbas_itc_sta_reduction_macrs_5 = float
	depr_fedbas_itc_sta_reduction_sl_15 = float
	depr_fedbas_itc_sta_reduction_sl_20 = float
	depr_fedbas_itc_sta_reduction_sl_39 = float
	depr_fedbas_itc_sta_reduction_sl_5 = float
	depr_fedbas_itc_sta_reduction_total = float
	depr_fedbas_macrs_15 = float
	depr_fedbas_macrs_5 = float
	depr_fedbas_percent_amount_custom = float
	depr_fedbas_percent_amount_macrs_15 = float
	depr_fedbas_percent_amount_macrs_5 = float
	depr_fedbas_percent_amount_sl_15 = float
	depr_fedbas_percent_amount_sl_20 = float
	depr_fedbas_percent_amount_sl_39 = float
	depr_fedbas_percent_amount_sl_5 = float
	depr_fedbas_percent_amount_total = float
	depr_fedbas_percent_custom = float
	depr_fedbas_percent_macrs_15 = float
	depr_fedbas_percent_macrs_5 = float
	depr_fedbas_percent_qual_custom = float
	depr_fedbas_percent_qual_macrs_15 = float
	depr_fedbas_percent_qual_macrs_5 = float
	depr_fedbas_percent_qual_sl_15 = float
	depr_fedbas_percent_qual_sl_20 = float
	depr_fedbas_percent_qual_sl_39 = float
	depr_fedbas_percent_qual_sl_5 = float
	depr_fedbas_percent_qual_total = float
	depr_fedbas_percent_sl_15 = float
	depr_fedbas_percent_sl_20 = float
	depr_fedbas_percent_sl_39 = float
	depr_fedbas_percent_sl_5 = float
	depr_fedbas_percent_total = float
	depr_fedbas_prior_itc_custom = float
	depr_fedbas_prior_itc_macrs_15 = float
	depr_fedbas_prior_itc_macrs_5 = float
	depr_fedbas_prior_itc_sl_15 = float
	depr_fedbas_prior_itc_sl_20 = float
	depr_fedbas_prior_itc_sl_39 = float
	depr_fedbas_prior_itc_sl_5 = float
	depr_fedbas_prior_itc_total = float
	depr_fedbas_sl_15 = float
	depr_fedbas_sl_20 = float
	depr_fedbas_sl_39 = float
	depr_fedbas_sl_5 = float
	depr_fedbas_total = float
	depr_stabas_after_itc_custom = float
	depr_stabas_after_itc_macrs_15 = float
	depr_stabas_after_itc_macrs_5 = float
	depr_stabas_after_itc_sl_15 = float
	depr_stabas_after_itc_sl_20 = float
	depr_stabas_after_itc_sl_39 = float
	depr_stabas_after_itc_sl_5 = float
	depr_stabas_after_itc_total = float
	depr_stabas_cbi_reduc_custom = float
	depr_stabas_cbi_reduc_macrs_15 = float
	depr_stabas_cbi_reduc_macrs_5 = float
	depr_stabas_cbi_reduc_sl_15 = float
	depr_stabas_cbi_reduc_sl_20 = float
	depr_stabas_cbi_reduc_sl_39 = float
	depr_stabas_cbi_reduc_sl_5 = float
	depr_stabas_cbi_reduc_total = float
	depr_stabas_custom = float
	depr_stabas_first_year_bonus_custom = float
	depr_stabas_first_year_bonus_macrs_15 = float
	depr_stabas_first_year_bonus_macrs_5 = float
	depr_stabas_first_year_bonus_sl_15 = float
	depr_stabas_first_year_bonus_sl_20 = float
	depr_stabas_first_year_bonus_sl_39 = float
	depr_stabas_first_year_bonus_sl_5 = float
	depr_stabas_first_year_bonus_total = float
	depr_stabas_fixed_amount_custom = float
	depr_stabas_fixed_amount_macrs_15 = float
	depr_stabas_fixed_amount_macrs_5 = float
	depr_stabas_fixed_amount_sl_15 = float
	depr_stabas_fixed_amount_sl_20 = float
	depr_stabas_fixed_amount_sl_39 = float
	depr_stabas_fixed_amount_sl_5 = float
	depr_stabas_fixed_amount_total = float
	depr_stabas_ibi_reduc_custom = float
	depr_stabas_ibi_reduc_macrs_15 = float
	depr_stabas_ibi_reduc_macrs_5 = float
	depr_stabas_ibi_reduc_sl_15 = float
	depr_stabas_ibi_reduc_sl_20 = float
	depr_stabas_ibi_reduc_sl_39 = float
	depr_stabas_ibi_reduc_sl_5 = float
	depr_stabas_ibi_reduc_total = float
	depr_stabas_itc_fed_reduction_custom = float
	depr_stabas_itc_fed_reduction_macrs_15 = float
	depr_stabas_itc_fed_reduction_macrs_5 = float
	depr_stabas_itc_fed_reduction_sl_15 = float
	depr_stabas_itc_fed_reduction_sl_20 = float
	depr_stabas_itc_fed_reduction_sl_39 = float
	depr_stabas_itc_fed_reduction_sl_5 = float
	depr_stabas_itc_fed_reduction_total = float
	depr_stabas_itc_sta_reduction_custom = float
	depr_stabas_itc_sta_reduction_macrs_15 = float
	depr_stabas_itc_sta_reduction_macrs_5 = float
	depr_stabas_itc_sta_reduction_sl_15 = float
	depr_stabas_itc_sta_reduction_sl_20 = float
	depr_stabas_itc_sta_reduction_sl_39 = float
	depr_stabas_itc_sta_reduction_sl_5 = float
	depr_stabas_itc_sta_reduction_total = float
	depr_stabas_macrs_15 = float
	depr_stabas_macrs_5 = float
	depr_stabas_percent_amount_custom = float
	depr_stabas_percent_amount_macrs_15 = float
	depr_stabas_percent_amount_macrs_5 = float
	depr_stabas_percent_amount_sl_15 = float
	depr_stabas_percent_amount_sl_20 = float
	depr_stabas_percent_amount_sl_39 = float
	depr_stabas_percent_amount_sl_5 = float
	depr_stabas_percent_amount_total = float
	depr_stabas_percent_custom = float
	depr_stabas_percent_macrs_15 = float
	depr_stabas_percent_macrs_5 = float
	depr_stabas_percent_qual_custom = float
	depr_stabas_percent_qual_macrs_15 = float
	depr_stabas_percent_qual_macrs_5 = float
	depr_stabas_percent_qual_sl_15 = float
	depr_stabas_percent_qual_sl_20 = float
	depr_stabas_percent_qual_sl_39 = float
	depr_stabas_percent_qual_sl_5 = float
	depr_stabas_percent_qual_total = float
	depr_stabas_percent_sl_15 = float
	depr_stabas_percent_sl_20 = float
	depr_stabas_percent_sl_39 = float
	depr_stabas_percent_sl_5 = float
	depr_stabas_percent_total = float
	depr_stabas_prior_itc_custom = float
	depr_stabas_prior_itc_macrs_15 = float
	depr_stabas_prior_itc_macrs_5 = float
	depr_stabas_prior_itc_sl_15 = float
	depr_stabas_prior_itc_sl_20 = float
	depr_stabas_prior_itc_sl_39 = float
	depr_stabas_prior_itc_sl_5 = float
	depr_stabas_prior_itc_total = float
	depr_stabas_sl_15 = float
	depr_stabas_sl_20 = float
	depr_stabas_sl_39 = float
	depr_stabas_sl_5 = float
	depr_stabas_total = float
	effective_tax_rate = float
	firstyear_energy_dispatch1 = float
	firstyear_energy_dispatch2 = float
	firstyear_energy_dispatch3 = float
	firstyear_energy_dispatch4 = float
	firstyear_energy_dispatch5 = float
	firstyear_energy_dispatch6 = float
	firstyear_energy_dispatch7 = float
	firstyear_energy_dispatch8 = float
	firstyear_energy_dispatch9 = float
	firstyear_energy_price1 = float
	firstyear_energy_price2 = float
	firstyear_energy_price3 = float
	firstyear_energy_price4 = float
	firstyear_energy_price5 = float
	firstyear_energy_price6 = float
	firstyear_energy_price7 = float
	firstyear_energy_price8 = float
	firstyear_energy_price9 = float
	firstyear_revenue_dispatch1 = float
	firstyear_revenue_dispatch2 = float
	firstyear_revenue_dispatch3 = float
	firstyear_revenue_dispatch4 = float
	firstyear_revenue_dispatch5 = float
	firstyear_revenue_dispatch6 = float
	firstyear_revenue_dispatch7 = float
	firstyear_revenue_dispatch8 = float
	firstyear_revenue_dispatch9 = float
	flip_actual_irr = float
	flip_actual_year = float
	flip_target_irr = float
	flip_target_year = float
	ibi_fedtax_total = float
	ibi_statax_total = float
	ibi_total = float
	ibi_total_fed = float
	ibi_total_oth = float
	ibi_total_sta = float
	ibi_total_uti = float
	issuance_of_equity = float
	itc_disallow_fed_fixed_custom = float
	itc_disallow_fed_fixed_macrs_15 = float
	itc_disallow_fed_fixed_macrs_5 = float
	itc_disallow_fed_fixed_sl_15 = float
	itc_disallow_fed_fixed_sl_20 = float
	itc_disallow_fed_fixed_sl_39 = float
	itc_disallow_fed_fixed_sl_5 = float
	itc_disallow_fed_fixed_total = float
	itc_disallow_fed_percent_custom = float
	itc_disallow_fed_percent_macrs_15 = float
	itc_disallow_fed_percent_macrs_5 = float
	itc_disallow_fed_percent_sl_15 = float
	itc_disallow_fed_percent_sl_20 = float
	itc_disallow_fed_percent_sl_39 = float
	itc_disallow_fed_percent_sl_5 = float
	itc_disallow_fed_percent_total = float
	itc_disallow_sta_fixed_custom = float
	itc_disallow_sta_fixed_macrs_15 = float
	itc_disallow_sta_fixed_macrs_5 = float
	itc_disallow_sta_fixed_sl_15 = float
	itc_disallow_sta_fixed_sl_20 = float
	itc_disallow_sta_fixed_sl_39 = float
	itc_disallow_sta_fixed_sl_5 = float
	itc_disallow_sta_fixed_total = float
	itc_disallow_sta_percent_custom = float
	itc_disallow_sta_percent_macrs_15 = float
	itc_disallow_sta_percent_macrs_5 = float
	itc_disallow_sta_percent_sl_15 = float
	itc_disallow_sta_percent_sl_20 = float
	itc_disallow_sta_percent_sl_39 = float
	itc_disallow_sta_percent_sl_5 = float
	itc_disallow_sta_percent_total = float
	itc_fed_fixed_total = float
	itc_fed_percent_total = float
	itc_fed_qual_custom = float
	itc_fed_qual_macrs_15 = float
	itc_fed_qual_macrs_5 = float
	itc_fed_qual_sl_15 = float
	itc_fed_qual_sl_20 = float
	itc_fed_qual_sl_39 = float
	itc_fed_qual_sl_5 = float
	itc_fed_qual_total = float
	itc_sta_fixed_total = float
	itc_sta_percent_total = float
	itc_sta_qual_custom = float
	itc_sta_qual_macrs_15 = float
	itc_sta_qual_macrs_5 = float
	itc_sta_qual_sl_15 = float
	itc_sta_qual_sl_20 = float
	itc_sta_qual_sl_39 = float
	itc_sta_qual_sl_5 = float
	itc_sta_qual_total = float
	itc_total = float
	itc_total_fed = float
	itc_total_sta = float
	lcoe_nom = float
	lcoe_real = float
	lcoptc_fed_nom = float
	lcoptc_fed_real = float
	lcoptc_sta_nom = float
	lcoptc_sta_real = float
	lppa_nom = float
	lppa_real = float
	nominal_discount_rate = float
	npv_annual_costs = float
	npv_energy_nom = float
	npv_energy_real = float
	npv_ppa_revenue = float
	ppa = float
	ppa_escalation = float
	ppa_multipliers = tuple
	ppa_price = float
	present_value_fuel = float
	present_value_insandproptax = float
	present_value_oandm = float
	present_value_oandm_nonfuel = float
	prop_tax_assessed_value = float
	purchase_of_property = float
	salvage_value = float
	size_of_equity = float
	sponsor_aftertax_development = float
	sponsor_aftertax_equity = float
	sponsor_aftertax_irr = float
	sponsor_aftertax_npv = float
	sponsor_pretax_development = float
	sponsor_pretax_equity = float
	sponsor_pretax_irr = float
	sponsor_pretax_npv = float
	tax_investor_aftertax_irr = float
	tax_investor_aftertax_npv = float
	tax_investor_pretax_irr = float
	tax_investor_pretax_npv = float
	wacc = float


class Equpartflip(object):
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

	FinancialParameters = FinancialParameters
	SystemCosts = SystemCosts
	TaxCreditIncentives = TaxCreditIncentives
	PaymentIncentives = PaymentIncentives
	SystemOutput = SystemOutput
	Recapitalization = Recapitalization
	TimeOfDelivery = TimeOfDelivery
	ReserveAccounts = ReserveAccounts
	Depreciation = Depreciation
	SalvageValue = SalvageValue
	SolutionMode = SolutionMode
	ConstructionFinancing = ConstructionFinancing
	OtherCapitalCosts = OtherCapitalCosts
	IRRTargets = IRRTargets
	DeveloperCapitalRecovery = DeveloperCapitalRecovery
	Battery = Battery
	Outputs = Outputs


def default(config) -> Equpartflip
	pass

def new() -> Equpartflip
	pass

def wrap(ssc_data_t) -> Equpartflip
	pass

__loader__ = None 

__spec__ = None
