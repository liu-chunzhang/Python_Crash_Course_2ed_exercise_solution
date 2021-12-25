cities = {
	"Shanghai": {
		"Country": "China",
		"Population": 24_900_000,
		"fact": "it changes fast"
	},

	"New York": {
		"Country": "America",
		"Population": 8_510_000,
		"fact": "it is near to Atlantic Ocean"
	},

	"Moscow": {
		"Country": "Russia",
		"Population": 14_150_000,
		"fact": "it is the capital of Russia"
	}

}

for cityname, citycharacters in cities.items():
	for key, value in citycharacters.items():
		print(f"The {key} of {cityname} is that {value}.")