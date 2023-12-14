import requests
import json
from faker import Faker

# Install the required libraries
# !pip3 install faker

# Import the Faker library
fake = Faker()

# Step 2: Create GET requests
pokemon_api_url = "https://pokeapi.co/api/v2/pokemon"
images_api_url = "https://fakerapi.it/api/v1/images?_type=people&__quantity=15"
users_api_url = "https://fakerapi.it/api/v1/places?__quantity=15"

pokemon_response = requests.get(pokemon_api_url).json()
images_response = requests.get(images_api_url).json()
users_response = requests.get(users_api_url).json()

# Step 4: Convert and store responses in JSON files
with open('pokemon_data.json', 'w') as pokemon_file:
    json.dump(pokemon_response, pokemon_file, indent=2)

with open('images_data.json', 'w') as images_file:
    json.dump(images_response, images_file, indent=2)

with open('users_data.json', 'w') as users_file:
    json.dump(users_response, users_file, indent=2)

# Step 5: Create new dictionaries
# Print the structure of images_response
print(json.dumps(images_response, indent=2))

# Create new dictionaries
poke_locations = []

for i in range(min(15, len(images_response['data']))):
    poke_location = {
        "pokemon": pokemon_response['results'][i]['name'],
        "image": images_response['data'][i]['url'],
        "location": fake.local_latlng(),
    }
    poke_locations.append(poke_location)


# Step 6: Print the results
for i, location in enumerate(poke_locations, 1):
    print(f"--------\nPokemon {i}\n--------")
    print(f"Name: {location['pokemon']}")
    print(f"Image: {location['image']}")
    print(f"Latitude: {location['location'][0]}")
    print(f"Longitude: {location['location'][1]}")

# Step 7: Create personalized requests and present the data
# You can explore the suggested APIs and implement your ideas here.