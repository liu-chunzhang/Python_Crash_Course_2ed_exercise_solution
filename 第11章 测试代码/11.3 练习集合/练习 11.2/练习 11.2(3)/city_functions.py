def city_in_country(city, country, population=''):
	if population:
		message = f"{city}, {country} - population {population}"
	else :
		message = f"{city}, {country}"
	return message.title()