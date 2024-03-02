# Use library to call API
import requests

# The URL of API to get the Joke
jokes_api = "https://v2.jokeapi.dev/joke/Programming"

# Perform GET request , GET = Read
response = requests.get(jokes_api)

# Printing the response
print(response.json()["joke"])



