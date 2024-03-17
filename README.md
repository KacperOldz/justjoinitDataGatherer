# JustJoin.it Job Scraping Script

This Python script scrapes job data from the JustJoin.it website based on specified locations, technologies, and experience levels. It fetches information such as the number of job offers available for each combination of location, technology, and experience level and saves it to text files.

## Features

- Scrapes job data from JustJoin.it for specified locations, technologies, and experience levels.
- Extracts the number of job offers available for each combination.
- Saves the data to text files for further analysis.

## Requirements

- Python 3.x
- `requests` library (to make HTTP requests)
- `BeautifulSoup` library (for HTML parsing)

## Usage

1. Clone this repository:

```bash
git clone https://github.com/your-username/justjoinit-scraper.git
```

2. Navigate to the project directory:

```bash
cd justjoinit-scraper
```

3. Install dependencies:

```bash
pip install -r requirements.txt
```

4. Run the script:

```bash
python code.py
```

## Configuration

- Modify the `LOCATIONS`, `TECHS`, and `EXPERIENCE` lists in the `code.py` file to specify the desired locations, technologies, and experience levels for scraping job data.
- Adjust the `BASE_URL` constant if the JustJoin.it website URL changes in the future.

## Files

- `code.py`: The main Python script for scraping job data.
- `requirements.txt`: A text file containing the required Python libraries.
- `README.md`: This README file providing information about the script.
