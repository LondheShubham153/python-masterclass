import requests

def fetch_joke(api_url):
    """Fetch a joke from the specified API URL."""
    try:
        response = requests.get(api_url)
        response.raise_for_status()  # Raise an error if the request failed
        return response.json()
    except requests.RequestException as e:
        print(f"Error fetching joke: {e}")
        return None

def display_joke(joke_data):
    """Display the joke based on its type."""
    if joke_data is None:
        return
    
    if joke_data.get('type') == 'single':
        print(joke_data.get('joke'))
    elif joke_data.get('type') == 'twopart':
        print(joke_data.get('setup'))
        print(joke_data.get('delivery'))
    else:
        print("Unknown joke format received.")

def main():
    jokes_api_url = "https://v2.jokeapi.dev/joke/Programming"
    joke_data = fetch_joke(jokes_api_url)
    display_joke(joke_data)

if __name__ == "__main__":
    main()

