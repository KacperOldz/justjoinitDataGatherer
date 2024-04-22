import requests
from bs4 import BeautifulSoup
import datetime
import re
import json
import os

BASE_URL = "https://justjoin.it"
EXPERIENCE = ["/", "/experience-level_junior?index=0#more-filters"]
actualDir = "./"

def readInfo():
    global LOCATIONS, TECHS
    with open(actualDir + 'config.json', 'r') as file:
        json_data = file.read()
        data = json.loads(json_data)
    LOCATIONS = data["locations"]
    print(LOCATIONS)
    TECHS = [lang["link"] for lang in data["languages"]]
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
    parent_element = soup.find(class_="css-ggjav7")
    if parent_element:
        element = parent_element.find(class_="css-9hflmo")
        if element:
            return extract_numbers_from_string(element.text)
    print("Element not found.")
    return 0

def save_data_to_file(content, filename):
    """Saves data to a file."""
    with open(filename, 'at') as file:
        file.write(content)

def getAndSaveData():
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
                        description += " " + "0"
                else:
                    print("Failed to fetch page content.")

        save_data_to_file(description, actualDir + location[1:] + ".txt")

def selectSave():
    global actualDir
    folders = [folder for folder in os.listdir("./saves") if os.path.isdir(os.path.join("./saves", folder))]
    for i in range(0, len(folders)):
        print(str(i) + ". " + folders[i])
    index = input("Select save: ")
    actualDir = "./saves/" + folders[int(index)] + '/'

def main():
    """Main function to scrape data and save it."""
    selectSave()
    readInfo()
    getAndSaveData()


if __name__ == "__main__":
    main()
