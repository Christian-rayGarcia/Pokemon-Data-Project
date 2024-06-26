from data_extraction import DataExtraction


def process_pokemon_base_data(pokemon_base_info):
	pokemon_type = [result['type']['name'] for result in pokemon_base_info['types']]
	return {
		"Index": pokemon_base_info["id"],
		"Name": pokemon_base_info["name"],
		"Type": " ".join(pokemon_type)
	}


base_url = "https://pokeapi.co/api/v2/"
endpoint = "pokemon"
output_file = "pokemon_base_info.csv"

fetcher = DataExtraction(base_url, endpoint, process_pokemon_base_data, output_file)
fetcher.get_data()
