```
# JustJoin.it Scraper

This script scrapes job data from the JustJoin.it website based on predefined configurations and saves it to text files. It also provides functionality to visualize the scraped data using matplotlib.

## Requirements
- Python 3.x
- requests
- BeautifulSoup4
- matplotlib

## Installation
1. Clone the repository: `git clone https://github.com/your_username/justjoin-it-scraper.git`
2. Install the required packages: `pip install -r requirements.txt`

## Usage
1. Run the `main.py` script: `python main.py`
2. Select a save folder or create a new one.
3. Choose whether to fetch and save data or read and visualize existing data.
4. If fetching data, the script will scrape job data from JustJoin.it based on the configurations provided in `config.json` and save it to text files.
5. If reading data, the script will prompt you to select a data file to visualize. It will then plot the data using matplotlib.

## Configuration
- `config.json`: Contains configurations for the script, including locations, languages, filters, and colors for visualization.

## File Structure
- `main.py`: Main script file to run.
- `config.json`: Configuration file.
- `saves/`: Folder containing saved data files.
- `README.md`: This file.

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
```
