import tkinter as tk
from tkinter import filedialog
import code

# Default file paths and directories
actualDir = "./saves/save1"
fileName = "all-locations.txt"
saveDir = "saves/save1"
configDir = "config.json"

def select_txt_file():
    """Function to open a file dialog and select a .txt file."""
    global fileName
    fileName = filedialog.askopenfilename(filetypes=[("Text files", "*.txt")])

def select_config_file():
    """Function to open a file dialog and select a .json configuration file."""
    global configDir
    configDir = filedialog.askopenfilename(filetypes=[("Json files", "*.json")])

def select_folder_file():
    """Function to open a file dialog and select a directory for saving files."""
    global saveDir
    saveDir = filedialog.askdirectory()

def drawGraphButton():
    """Function to draw a graph based on selected data and configuration."""
    data = main.readData(fileName)
    colors, languages = main.getGraphColorsAndLabels(configDir)
    main.drawGraph(colors, languages, data)

def getDataButton():
    """Function to get data from a website based on configuration and save it."""
    LOCATIONS, TECHS, EXPERIENCE = main.getDesiredLanguagesTechsAndExperience(configDir)
    print(LOCATIONS, TECHS, EXPERIENCE)
    main.getAndSaveDataFromWebside(LOCATIONS, TECHS, EXPERIENCE, saveDir)

def createGUI():
    """Function to create the graphical user interface."""
    # Buttons for selecting files and directories
    select_button = tk.Button(root, text="Select .txt File", command=select_txt_file)
    select_button.pack(padx=10, pady=10)

    select_config_button = tk.Button(root, text="Select .json File", command=select_config_file)
    select_config_button.pack(padx=10, pady=10)

    select_folder_button = tk.Button(root, text="Select Save Folder", command=select_folder_file)
    select_folder_button.pack(padx=10, pady=10)

    # Buttons for executing actions
    execute_button = tk.Button(root, text="Draw Graph", command=drawGraphButton)
    execute_button.pack(padx=10, pady=10)

    execute_button = tk.Button(root, text="Get Data", command=getDataButton)
    execute_button.pack(padx=10, pady=10)

# Create the main window
root = tk.Tk()
root.title("Selectable List")

# Run the GUI event loop
createGUI()
root.mainloop()
