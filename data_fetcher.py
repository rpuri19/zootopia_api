import requests
API_KEY = '7JF2DdFDXolVEXVZEbe9pQ==S3VCmf2H6zPX1cvn'

def load_data(name):
    api_url = 'https://api.api-ninjas.com/v1/animals?name={}'.format(name)
    response = requests.get(api_url, headers={'X-Api-Key': API_KEY})
    if response.status_code == requests.codes.ok:
        animal_data = response.json()
        if not animal_data:  # Check if the response is empty
            print(f"The animal {name} doesn't exist.")
            return None
        else:
            return animal_data

    else:
        print("Error:", response.status_code, response.text)


def fetch_data(animal_name):
    data_of_animals = load_data(animal_name)
    return data_of_animals

