from playwright.sync_api import sync_playwright
from rich import print
import pandas as pd
import time

# Scraping logic 
def process_page(page, job_data):
    # Locate all job elements on the page
    main_divs = page.locator("//div[contains(@class, 'srp-jobtuple-wrapper')]").all()

    for job in main_divs:
        # Extract job details using locators
        job_title = job.locator("//a[contains(@class, 'title')]").inner_text()
        company_name = job.locator("//a[contains(@class, 'comp-name')]").inner_text()

        # Check if the locator for experience is available
        expwdth_locator = job.locator("span.expwdth")
        exprice = expwdth_locator.inner_text() if expwdth_locator.is_visible() else "Not specified"

        test = job.locator("div.row4")
        job_description = test.inner_text() if expwdth_locator.is_visible() else "Not specified"

        # Append job details to the job_data list
        job_data.append({
            'job_title': job_title,
            'company_name': company_name,
            'exprice': exprice,
            'job_description': job_description
        })

        # Print job details for each job
        print(f"Job title: {job_title}, Company name: {company_name},  Experience: {exprice}, Job description: {job_description}")

# Save data to CSV file 
def save_to_csv(job_data):
    # Convert job_data list to a DataFrame and save it to a CSV file
    df = pd.DataFrame(job_data)
    df.to_csv('naukri_jobstwo.csv', index=False)

if __name__ == '__main__':
    # List of URLs to process
    urls_to_process = [
        "https://www.naukri.com/remote-jobs"
    ]

    job_data = []  # List to store job details

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)

        for url in urls_to_process:
            page = browser.new_page()
            page.set_viewport_size({"width": 1480, "height": 1080})
            page.goto(url)
            page.wait_for_load_state("networkidle")
            
            # Process the current page
            process_page(page, job_data)

            # Pagination: Click "Next" button and process the next page
            for _ in range(40):
                next_button = page.query_selector('a.styles_btn-secondary__2AsIP:has-text("Next")')
                if next_button:
                    next_button.click()
                    page.wait_for_load_state("networkidle")
                    time.sleep(4)  # Adding a delay to ensure the page loads completely
                    process_page(page, job_data)  # Process each page

            # Close the page after processing
            page.close()

        # Save the data to CSV after processing all URLs
        save_to_csv(job_data)

        # Close the browser after processing all URLs
        browser.close()
