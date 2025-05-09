# Weather Data Downloader and Analysis

## Project Overview

This project scrapes a government website to find and download a specific weather data file from **2021**, based on the **Last Modified timestamp** (2024-01-19 10:27). Once the file is downloaded, the script loads the data into **Pandas**, finds the record with the highest `HourlyDryBulbTemperature`, and prints those records to the command line.

### Steps Involved:
1. **Web Scraping**: Scrape the webpage for the list of files, analyze the structure, and find the file corresponding to the **Last Modified timestamp** "2024-01-19 10:27".
2. **Download the File**: Build the URL required to download the file and save it locally.
3. **Load Data into Pandas**: Read the downloaded file into a Pandas DataFrame.
4. **Data Analysis**: Find and print the records with the highest `HourlyDryBulbTemperature`.

