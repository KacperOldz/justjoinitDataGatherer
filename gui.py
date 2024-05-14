import tkinter as tk
from tkinter import filedialog
import main

actualDir = "./saves/save1"  # Default directory
fileName = "all-locations.txt"  # Default filename
saveDir = "saves/save1"  # Default save directory
configDirLabel = "config.json"  # Default config directory

def select_txt_file():
    """Select a text file using a file dialog"""
    global fileName
    fileName = filedialog.askopenfilename(filetypes=[("Text files", "*.txt")])
    txtDirLabel.config(text=fileName)

def select_config_file():
    """Select a configuration file using a file dialog"""
    global configDir
    configDir = filedialog.askopenfilename(filetypes=[("Json files", "*.json")])
    configDirLabel.config(text=configDir)

def select_folder_file():
    """Select a folder using a folder dialog."""
    global saveDir
    saveDir = filedialog.askdirectory()
    folderDirLabel.config(text=saveDir)

def drawGraphButton():
    """Read data from selected file get graph colors and labels from selected configuration file and draw graph."""
    data = main.readData(fileName)
    colors, languages = main.getGraphColorsAndLabels(configDir)
    main.drawGraph(colors, languages, data)

def getDataButton():
    """Get desired locations technologies and experience levels from selected configuration file and save data from websites."""
    LOCATIONS, TECHS, EXPERIENCE = main.getDesiredLanguagesTechsAndExperience(configDir)
    print(LOCATIONS, TECHS, EXPERIENCE)
    main.getAndSaveDataFromWebside(LOCATIONS, TECHS, EXPERIENCE, saveDir)

def createGUI():
    """Create GUI elements."""
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

    draw_button = tk.Button(root, text="Draw Graph", command=drawGraphButton)
    draw_button.grid(row=3,column=0,padx=10,pady=10)
    save_button = tk.Button(root, text="Get Data", command=getDataButton)
    save_button.grid(row=3,column=1,padx=10,pady=10)
    root.mainloop()


# Create the main window
root = tk.Tk()
root.title("JustJoin.it scrapper")

# Run the GUI event loop
createGUI()
