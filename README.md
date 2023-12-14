# Python-APIs-Consuming-Project-I

## Consuming and Manipulating REST API responses in Python

Using the [Requests](https://docs.python-requests.org/en/latest/) library of Python 3, you will write a short script that will create a bunch of requests to the [Faker API](https://fakerapi.it/en), save all that data, and will also combine+transform the response data into new Dictionaries that can be consumed.

### 1. Install Requests

First Step: Install the Requests library

```python
!pip3 install requests
```

OR

```python
$ python3 -m pip install requests
```

### 2. Import the Requests Library

### 3. Create the following requests

Using the Requests library, create the following GET requests to the [Faker APIs](https://fakerapi.it/en) and store the responses in variables.

1. Make a GET call to the Custom API and call a list of 15 Pokemon.
2. Make a GET call to the Images API and call a list of 15 images of `_Type=people`.
3. Make a GET call to the Users API and call a list of 15 Places.

### 4. Convert and store each response object to JSON files

To always have access to your data, parse the incoming objects into JSON format and save the objects in seperate JSON file format. It pays to know how to do this, as many times you will have to save responses to examining the structure on API responses, specially if you work in teams where your team creates its own APIs. Also when you have to work with the data in a quick local environment, like a Jupyter Notebook.

A really good tutorial on how to create JSON dumps can be found here: https://www.section.io/engineering-education/storing-data-in-python-using-json-module/

**NOTE: Save these JSON files locally, you will need them for the next Project!**


### 5. Create new dictionaries

From the received responses, create a list of new dictionaries that each has:

1. a Pokemon name,
2. an Image link to a Pokemon,
3. a Place.

```python
pokeLocation ={
    "pokemon": "Smeargle",
    "image": "https://lorempokemon.fakerapi.it/pokemon/500/400",
    "location": {
        "latitude": -78.909139,
        "longitude": -8.697088
    },
}
```
### 6. Print the results

Of course, raw data is tough to look at for humans. Let's make the responses human readable. 
For this, you will have to write several print statements that print each pokeLocation object in the following format:

````pip
--------
Pokemon 1
--------
Name: Smeargle
Image: https://lorempokemon.fakerapi.it/pokemon/500/400
Latitude: -78.909139
Longitude: -78.909139
--------
Pokemon 2
--------
...and so on for each Pokemon

````


### 7. Create personalized requests and present the data to the class

Now that you have made some GET requests using the [Requests](https://docs.python-requests.org/en/latest/)library and handled the responses, and presented the data in a human readable way, you should GET data from one of the Public APIs (in the link below) and come up with some cool ideas to print some data to the console. Be creative, have fun, and share the results with your class or breakout groups!

https://github.com/public-apis/public-apis

Some suggestions:
- Extend the current project with the [PokeAPI](https://pokeapi.co)

**Idea:** Extend the information for all 15 of your ```pokeLocation``` objects above. Simply send the name of the Pokemons to the API (as shown on the PokeAPI landing page) and get all sorts of data on your Pokemon. Check out the Docs for the Consumption-Only APi here: https://pokeapi.co/docs/v2 
Try to understand what all that data represents, this is usually something backend engineers should be comfortable doing as you might be working with lots of data!


 - Open Green Data [La Data Verte](https://ladataverte.fr/endpoint)
 
 **Idea:** La Data verte is a Public API for multiple environment indicators. Print reports to the console for given location. See the docuentation on: https://ladataverte.fr/endpoint   

 - Bitcoin price tickers [Crytonator](https://www.cryptonator.com/api?__cf_chl_jschl_tk__=pmd_0AMGyQPHVb5Sq4ySFB1UgUiznQ6FpRyCEpAQDigJjEU-1632254019-0-gqNtZGzNAhCjcnBszQeR)
 
 **Idea:** GET all the latest crypto data at intervals of your choosing (HINT: use loops 😉) and create a personalized live-ticker!