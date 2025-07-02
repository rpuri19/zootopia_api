# Animal Data Fetcher

This project fetches detailed information about animals using the API provided by [API Ninjas](https://api-ninjas.com/). The script allows users to input the name of an animal, fetches the animal's data, and updates an HTML file with this data.

## Features

- Fetch animal information like diet, type, and location.
- Dynamically updates an HTML file with the retrieved data.
- Handles API request errors and missing data gracefully.

## Installation

### Prerequisites

Make sure you have **Python 3.6+** installed on your machine.

## Installation

To install this project, simply clone the repository and install the dependencies in requirements.txt using `pip`

## Usage

To use this project, run **animals_web_generator.py**

## Important

Please note an API key is needed :)

You can get the API key at [API Ninjas](https://api-ninjas.com/api/animals)

Create a `.env` file in the root directory of the project and add your API key:

```env
API_NINJAS_KEY=your_api_key_here
```


example screenshots: 

![Alt Text](images/enter_name.png)

![Alt Text](images/result_html_page.png)