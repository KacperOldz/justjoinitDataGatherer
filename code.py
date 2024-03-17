import requests
from bs4 import BeautifulSoup
import datetime
import re

# Constants
BASE_URL = "https://justjoin.it"
LOCATIONS = ["/all-locations", "/bialystok"]
TECHS = ["/java", "/javascript", "/python"]
EXPERIENCE = ["/", "/experience-level_junior?index=0#more-filters"]

def extract_numbers_from_string(input_string):
    """Extracts numbers from a string."""
    numbers = re.findall(r'\d+', input_string)
    return "".join(numbers)

def fetch_page_content(url):
    """Fetches the content of a webpage."""
    response = requests.get(url)
    if response.status_code == 200:
        return response.text
    else:
        print(f"Failed to fetch content from {url}")
        return None

def find_element_content(html):
    """Finds and extracts content from a specific element."""
    soup = BeautifulSoup(html, 'html.parser')
    element = soup.find(class_="css-ggjav7").find(class_="css-9hflmo")
    if element:
        return extract_numbers_from_string(element.text)
    else:
        print("Element not found.")
        return None

def save_data_to_file(content, filename):
    """Saves data to a file."""
    with open(filename, 'at') as file:
        file.write(content)

def main():
    """Main function to scrape data and save it."""
    for location in LOCATIONS:
        description = "\n" + datetime.datetime.now().strftime("%Y-%m-%d")
        for experience_level in EXPERIENCE:
            for tech in TECHS:
                url = BASE_URL + location + tech + experience_level
                print(url)
                html_content = fetch_page_content(url)
                if html_content:
                    element_content = find_element_content(html_content)
                    if element_content:
                        description += " " + element_content
                    else:
                        print("Element content not found.")
                else:
                    print("Failed to fetch page content.")

        save_data_to_file(description, location[1:] + ".txt")

if __name__ == "__main__":
    main()
