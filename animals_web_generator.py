import data_fetcher

def serialize_animal(animal):
    """Converts an individual animal's data into an HTML <li> element.
    Handles name, diet, type, and location."""
    output_data_of_animals = ""
    animal_name = animal.get("name", "Unknown")
    characteristics = animal["characteristics"]
    animal_type = characteristics.get("type",  "Unknown")
    animal_diet = characteristics.get("diet",  "Unknown")
    first_location = animal.get("locations")[0]
    output_data_of_animals += (
        '<li class="cards__item">\n'
        f'<div class="card__title">{animal_name}</div>\n'
        f'<p class="card__text">\n'
        f'<strong>Diet:</strong> {animal_diet}<br/>\n'
        f'<strong>Location:</strong> {first_location}<br/>\n'
        f'<strong>Type:</strong> {animal_type}<br/>\n'
        '</p>'
        '</li>'
    )

    return output_data_of_animals

def animal_details(animals_data):
    """Iterates through a list of animal data and generates HTML for each.
    Provides a default message when no data is available."""
    if not animals_data:
        return '<li class="cards__item"><div class="card__title">Animal data not found.</div></li>'

    output = ""
    for animal_obj in animals_data:
        output += serialize_animal(animal_obj)
    return output


def replace_data_in_html (data):
    """Replaces a placeholder (__REPLACE_ANIMALS_INFO__) in a template HTML file with the generated animal data.
    Writes the updated HTML to a new file."""
    with open('animals_template.html', 'r') as file:
        html_content = file.read()

    new_output = html_content.replace("__REPLACE_ANIMALS_INFO__", f"{data}")

    with open('animals.html', 'w') as output_file:
        output_file.write(new_output)


def main():
    input_animal_name = input("Enter the name of an Animal: ")
    data = data_fetcher.fetch_data(input_animal_name)
    animals_list = animal_details(data)
    replace_data_in_html(animals_list)
    print(f"Website was successfully generated to the file animals.html")


if __name__ == "__main__":
    main()
