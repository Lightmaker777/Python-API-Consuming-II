import requests
import json

# Step 3: Create GET requests
pokemon_response = requests.get("https://fakerapi.it/api/v1/pokemon?_quantity=15")
images_response = requests.get("https://fakerapi.it/api/v1/images?_quantity=15&_type=people")
places_response = requests.get("https://fakerapi.it/api/v1/places?_quantity=15")

# Step 4: Convert and store responses in JSON files
pokemon_data = pokemon_response.json()
images_data = images_response.json()
places_data = places_response.json()

with open("pokemon_data.json", "w") as file:
    json.dump(pokemon_data, file, indent=2)

with open("images_data.json", "w") as file:
    json.dump(images_data, file, indent=2)

with open("places_data.json", "w") as file:
    json.dump(places_data, file, indent=2)

# Step 5: Create new dictionaries
poke_locations = []

# Add these lines for debugging
print("Pokemon Response:", pokemon_response.json())
print("Images Response:", images_response.json())
print("Places Response:", places_response.json())

for i in range(15):
    try:
        pokemon_name = pokemon_data['data'][i]["name"]
        image_link = images_data['data'][i]["url"]
        location = {
            "latitude": places_data['data'][i]["latitude"],
            "longitude": places_data['data'][i]["longitude"]
        }

        poke_location = {
            "pokemon": pokemon_name,
            "image": image_link,
            "location": location
        }

        poke_locations.append(poke_location)
    except KeyError as e:
        print(f"KeyError at index {i}: {e}")
        print("Pokemon Response:", pokemon_data)
        print("Images Response:", images_data)
        print("Places Response:", places_data)

# Step 6: Print the results
for i, poke_location in enumerate(poke_locations, 1):
    print(f"--------\nPokemon {i}\n--------")
    print(f"Name: {poke_location['pokemon']}")
    print(f"Image: {poke_location['image']}")
    print(f"Latitude: {poke_location['location']['latitude']}")
    print(f"Longitude: {poke_location['location']['longitude']}")
