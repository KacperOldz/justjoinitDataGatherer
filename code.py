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


def checkIfInputIsRight(min, max, inputText="Select option:"):
    while True:
        try:
            index = int(input(inputText))
            if min <= index < max:
                return index
            else:
                print("Invalid index. Please enter a valid number.")
        except ValueError:
            print("Invalid input. Please enter a valid number.")

def getDesiredLanguagesTechsAndExperience():
    global LOCATIONS, TECHS, EXPERIENCE
    with open(actualDir + 'config.json', 'r') as file:
        json_data = file.read()
        data = json.loads(json_data)
    LOCATIONS = data["locations"]
    print(LOCATIONS)
    TECHS = [lang["link"] for lang in data["languages"]]
    EXPERIENCE = [filter["link"] for filter in data["filters"]]

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

def getAndSaveDataFromWebside():
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

def selectSave():
    global actualDir
    folders = [folder for folder in os.listdir("./saves") if os.path.isdir(os.path.join("./saves", folder))]
    for i in range(0, len(folders)):
        print(str(i) + ". " + folders[i])
    index = checkIfInputIsRight(0, len(folders))
    actualDir = "./saves/" + folders[int(index)] + '/'

def getGraphColorsAndLabels():
    global colors, languages
    with open(actualDir + 'config.json', 'r') as file:
        json_data = file.read()
        config = json.loads(json_data)

    colors = [lang["color"] for lang in config["languages"]]
    languages = [lang["label"] for lang in config["languages"]]

def drawGraph():
    for j in range(0, len(colors)):
        x = [datetime.strptime(line[0], "%Y-%m-%d") for line in data]
        y = [int(line[j+1]) for line in data]
        plt.plot(x, y, color=colors[j], label=languages[j])
    plt.xlabel('Date')
    plt.ylabel('Amount')
    plt.xticks(rotation=45)
    plt.legend()
    plt.show()
def readData(fileName):
    with open(fileName, 'r') as file:
        lines = file.readlines()
        for line in lines:
            elements = line.split()
            data.append([num for num in elements[0:len(elements)]])

def drawGraphForDesiredDataFile():
    global data
    txt_files = [file for file in os.listdir(actualDir) if file.endswith('.txt')]
    for i, txt_file in enumerate(txt_files):
        print(f"{i}. {txt_file}")
    print("Colors: " + str(colors))
    print("Languages: " + str(languages))

    index = checkIfInputIsRight(0 , len(txt_files))
    readData(txt_files[index])
    drawGraph()

def main():
    """Main function to scrape data and save it."""
    con = True
    while con:
        selectSave()
        getDesiredLanguagesTechsAndExperience()
        if int(input("Save or read?")) == 0:
            getAndSaveDataFromWebside()
        else:
            getGraphColorsAndLabels()
            drawGraphForDesiredDataFile()



if __name__ == "__main__":
    main()
