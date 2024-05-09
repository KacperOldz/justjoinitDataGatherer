import tkinter as tk
from tkinter import filedialog
import main

actualDir = "./saves/save1"
fileName = "all-locations.txt"
saveDir = "saves/save1"
configDirLabel = "config.json"

def select_txt_file():
    global fileName
    fileName = filedialog.askopenfilename(filetypes=[("Text files", "*.txt")])
    txtDirLabel.config(text=fileName)

def select_config_file():
    global configDir
    configDir = filedialog.askopenfilename(filetypes=[("Json files", "*.json")])
    configDirLabel.config(text=configDir)

def select_folder_file():
    global saveDir
    saveDir = filedialog.askdirectory()
    folderDirLabel.config(text=saveDir)


def drawGraphButton():
    data = main.readData(fileName)
    colors, languages = main.getGraphColorsAndLabels(configDirLabel)
    main.drawGraph(colors, languages, data)

def getDataButton():
    LOCATIONS, TECHS, EXPERIENCE = main.getDesiredLanguagesTechsAndExperience(configDir)
    print(LOCATIONS, TECHS, EXPERIENCE)
    main.getAndSaveDataFromWebside(LOCATIONS, TECHS, EXPERIENCE, saveDir)

def createGUI():
    global txtDirLabel, configDirLabel, folderDirLabel
    select_button = tk.Button(root, text="Select .txt File", command=select_txt_file)
    select_button.grid(row=0, column=0,padx=10,pady=10)
    txtDirLabel = tk.Label(root, text="directiory")
    txtDirLabel.grid(row=0, column=1, padx=10, pady=10)

    select_config_button = tk.Button(root, text="Select .json File", command=select_config_file)
    select_config_button.grid(row=1,column=0,padx=10,pady=10)
    configDirLabel = tk.Label(root, text="directiory")
    configDirLabel.grid(row=1, column=1, padx=10, pady=10)

    select_folder_button = tk.Button(root, text="Select Save Folder", command=select_folder_file)
    select_folder_button.grid(row=2,column=0,padx=10,pady=10)
    folderDirLabel = tk.Label(root, text="directiory")
    folderDirLabel.grid(row=2, column=1, padx=10, pady=10)

    execute_button = tk.Button(root, text="Draw Graph", command=drawGraphButton)
    execute_button = tk.Button(root, text="Get Data", command=getDataButton)

# Create the main window
root = tk.Tk()
root.title("Selectable List")

# Run the GUI event loop
createGUI()
root.mainloop()
