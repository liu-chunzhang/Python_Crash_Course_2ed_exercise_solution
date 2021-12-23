def make_car(manufacturer, itstype, **parameters):
	parameters['manufacturer'] = manufacturer.title()
	parameters['itstype'] = itstype
	return parameters

car = make_car('subaru', 'outback', color='blue', tow_package=True)
print(car)