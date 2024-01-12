# This Python script uses Playwright and Pandas to scrape job details from a Naukri.com remote jobs page and saves the data to a CSV file.

## Dependencies

- `playwright`: Used for browser automation.
- `rich`: Provides rich text formatting for console output.
- `pandas`: Handles data manipulation and CSV file creation.

## Setup

1. Install Python: Make sure you have Python installed on your machine. You can download it from [python.org](https://www.python.org/downloads/).

2. Install dependencies: Run the following command to install the required libraries.

    ```bash
    pip install playwright rich pandas
    ```

    You can also create a virtual environment for this project.

3. Run the script: Execute the script using the following command.

    ```bash
    python your_script_name.py
    ```

    Replace `your_script_name.py` with the name of your Python script.

## Scraping Logic

The `process_page` function locates job elements on the page, extracts details, and appends them to the `job_data` list. The details include job title, company name, experience, and job description.

## Save to CSV

The `save_to_csv` function converts the `job_data` list to a Pandas DataFrame and saves it to a CSV file named `naukri_jobstwo.csv`.

## Pagination

The script iterates through pages by clicking the "Next" button up to 40 times, allowing for the scraping of multiple pages.

## Execution

1. URLs to scrape are defined in the `urls_to_process` list.

2. The script launches a Chromium browser, processes each URL, and saves the data to a CSV file.

   
# Disclaimer

This script is provided for educational and demonstration purposes only. The authors do not endorse or encourage any form of web scraping that violates the terms of service or policies of the targeted website. 

Use this script responsibly and ensure compliance with the terms and conditions of the websites you intend to scrape. Web scraping can put a load on the server and may impact the performance for other users. Make sure to review and respect the website's `robots.txt` file and terms of service before scraping.

The authors are not responsible for any legal issues, damages, or misuse arising from the use of this script. It is your responsibility to ensure that your actions are in accordance with the applicable laws and regulations.

Always refer to the website's terms of service and legal guidelines to understand the limitations and permissions for web scraping activities.

**Use this script at your own risk.**

