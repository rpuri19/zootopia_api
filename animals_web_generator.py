import data_fetcher

def serialize_animal(animal):
    output_data_of_animals = ""
    animal_name = animal["name"]
    characteristics = animal["characteristics"]
    animal_type = characteristics.get("type")
    animal_diet = characteristics.get("diet")
    first_location = animal.get("locations")[0]
    output_data_of_animals += '<li class="cards__item">\n'
    output_data_of_animals += f'<div class="card__title">{animal_name}</div>\n'
    output_data_of_animals += f'<p class="card__text">\n'
    output_data_of_animals += f'<strong>Diet:</strong> {animal_diet}<br/>\n'
    output_data_of_animals += f'<strong>Location:</strong> {first_location}<br/>\n'
    output_data_of_animals += f'<strong>Type:</strong> {animal_type}<br/>\n'
    output_data_of_animals += '</p>'
    output_data_of_animals += '</li>'
    return output_data_of_animals

def animal_details(animals_data):
    if not animals_data:
        # Return a placeholder message if no data is available
        return '<li class="cards__item"><div class="card__title">Animal data not found.</div></li>'

    output = ""
    for animal_obj in animals_data:
        output += serialize_animal(animal_obj)
    return output


def replace_data_in_html (data):
    # Open the HTML file
    with open('animals_template.html', 'r') as file:
        # Read the file's contents
        html_content = file.read()

    new_output = html_content.replace("__REPLACE_ANIMALS_INFO__", f"{data}")
    #print(new_output)

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
