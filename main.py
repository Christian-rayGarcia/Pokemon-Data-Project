import requests
import csv

# We use a session to reuse the underlying TCP connection
with requests.Session() as session:
	# Get the total count of Pokémon
	response = session.get("https://pokeapi.co/api/v2/pokemon?limit=1")
	response.raise_for_status()
	total_pokemon = response.json()['count']

	print(f"Total number of Pokémon: {total_pokemon}")

	# Initialise a list to hold Pokémon data
	pokemon_data = []

	for test in range(1, total_pokemon + 1):
		try:
			response = session.get(f"https://pokeapi.co/api/v2/pokemon/{test}")
			response.raise_for_status()
			pokemon_base_info = response.json()

			pokemon_type = [result['type']['name'] for result in pokemon_base_info['types']]
			Index = pokemon_base_info["id"]
			Name = pokemon_base_info["name"]
			Type = " ".join(pokemon_type)

			pokemon_data.append([Index, Name, Type])
		except requests.RequestException:
			break

# Write all data to the CSV file at once
with open("pokemon_base_info.csv", "w", newline='') as file:
	writer = csv.writer(file)
	writer.writerow(["Index", "Name", "Type"])  # Write header
	writer.writerows(pokemon_data)
