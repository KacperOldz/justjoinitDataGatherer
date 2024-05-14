import requests
from bs4 import BeautifulSoup
from datetime import datetime
import matplotlib.pyplot as plt
import re
import json
import os

BASE_URL = "https://justjoin.it"
actualDir = "./"
data = []

def getDesiredLanguagesTechsAndExperience(configDir):
    """
    :param configDir: Path to config.json file.
    :return: Returns arrays containing LOCATIONS, TECHS and EXPERIENCE
    """
    with open(configDir, 'r') as file:
        json_data = file.read()
        data = json.loads(json_data)
    LOCATIONS = data["locations"]
    print(LOCATIONS)
    TECHS = [lang["link"] for lang in data["languages"]]
    EXPERIENCE = [filter["link"] for filter in data["filters"]]
    return LOCATIONS, TECHS, EXPERIENCE

def extract_numbers_from_string(input_string):
    """
    :param input_string: String to extract number from.
    :return: Returns number extracted from string.
    """
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

def getAndSaveDataFromWebside(LOCATIONS, TECHS, EXPERIENCE, actualDir):
    """
    :param LOCATIONS: Array containing locations.
    :param TECHS: Array containing techs.
    :param EXPERIENCE: Array containing experience.
    :param actualDir: Directory to save files in.
    """
    for location in LOCATIONS:
        description = "\n" + datetime.now().strftime("%Y-%m-%d")
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
                        description += " 0"
                else:
                    description += " 0"

        save_data_to_file(description, actualDir + location[1:] + ".txt")

def getGraphColorsAndLabels(dir):
    """
    :param dir: Directory containing directory to the json file
    :return: Returns colors and languages arrays extracted from config.json
    """
    with open(dir, 'r') as file:
        json_data = file.read()
        config = json.loads(json_data)

    colors = [lang["color"] for lang in config["languages"]]
    languages = [lang["label"] for lang in config["languages"]]
    return colors, languages

def drawGraph(colors, languages, data, offset = 0):
    """
    :param colors: Colors array.
    :param languages: Languages array.
    :param data: Data array.
    """
    offset = len(colors) * offset
    for j in range(0, len(colors)):
        x = [datetime.strptime(line[0], "%Y-%m-%d") for line in data]
        y = [int(line[j+1+offset]) for line in data]
        plt.plot(x, y, color=colors[j], label=languages[j])
    plt.xlabel('Date')
    plt.ylabel('Amount')
    plt.xticks(rotation=45)
    plt.legend()
    plt.show()

def readData(fileName):
    """
    :param fileName: Name of file to read data from
    :return: Returns data array
    """
    data = []
    with open(fileName, 'r') as file:
        lines = file.readlines()
        for line in lines:
            elements = line.split()
            data.append([num for num in elements[0:len(elements)]])
    return data

def getFiltersLabels(configDir):
    """
    :param configDir: directory of config file
    :return: list of filter names
    """
    with open(configDir, 'r') as file:
        json_data = file.read()
        data = json.loads(json_data)
    labels = [filter["label"] for filter in data["filters"]]
    return labels


