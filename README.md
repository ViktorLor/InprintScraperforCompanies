# Webscraping impressum and inprint data from german companies

Author: Viktor Loreth

Date: 20.09.23

---

## Description:

This is a project to automatically scrape impressum data from german companies:

"Official Company Name | Tax number/UID | Company number | Telephone | Website | Email | Address Street | Address PLZ | Address City | Address Country | Revenue | Employees | sector"

## Usage:

1. Install geckodriver for firefox or chrome
2. Fill out the list in main.py with the companies you want to scrape
3. Run main.py
4. click all companies in the google search results. Filter for the real companies, as google search is only 90% accurate.
5. Str+a to copy all and paste into the responding txt file.
6. Run Adjustchatgptprompt.py to scrape the data and get the required tables.
7. Done! The results are in the folder companies_prompt_files
8. Write an additional script to aggregate the data as required.

## Requirements:

- Python 3.7+
- Selenium
- Firefox or Chrome
- geckodriver or chromedriver
- openai
- openai api key