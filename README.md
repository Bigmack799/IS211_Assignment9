# IS211_Assignment9
IS211_Assignment9

# Week 9: Web Scraping with Python

## Assignment Overview

This assignment demonstrates how Python can retrieve
information from webpages using HTTP and extract
structured HTML data with BeautifulSoup.

Two scripts were developed to collect and display
information from Wikipedia tables.

## Script 1: NASA Human Spaceflight Programs

File: scraper_one.py

Extracts NASA human spaceflight program information,
including program names, start dates, first crewed
flights, end dates, and mission counts.

Source:
https://en.wikipedia.org/wiki/List_of_NASA_missions

## Script 2: Renewable Electricity Production

File: scraper_two.py

Extracts renewable electricity production statistics
by country and territory, including total renewable
generation, hydroelectric, wind, and solar production,
and reporting year.

Electricity generation is measured in terawatt-hours
(TWh). Missing values are displayed as N/A.

Source:
https://en.wikipedia.org/wiki/List_of_countries_by_renewable_electricity_production

## Requirements

- Python 3
- BeautifulSoup4
- lxml

Install dependencies:

python -m pip install beautifulsoup4 lxml

## Running the Scripts

python scraper_one.py

python scraper_two.py

## Concepts Demonstrated

- HTTP requests using urllib.request
- HTML parsing with BeautifulSoup
- Extracting table rows and cells
- Cleaning text using regular expressions
- Displaying structured information in the terminal
- Basic exception handling

