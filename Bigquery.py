import asyncio
from pyppeteer import launch

async def scrape_jobs_from_indeed(job_title, location):
    browser = await launch(headless=False)  # Set to True to run headless
    page = await browser.newPage()

    # Navigate to Indeed
    await page.goto('https://www.indeed.com/')

    # Input job title
    await page.waitForSelector('input[name="q"]')
    await page.type('input[name="q"]', job_title)

    # Clear the default location
    location_input_selector = 'input[name="l"]'
    await page.waitForSelector(location_input_selector)
    await page.click(location_input_selector, {'clickCount': 3})  # Triple click to select all text
    await page.keyboard.press('Backspace')  # Clear the text

    # Input new location
    await page.type(location_input_selector, location)

    # Click search button
    await page.waitForSelector('button[type="submit"]')
    await page.click('button[type="submit"]')

    # Wait for navigation
    await page.waitForNavigation()

    # Apply "Date Posted" filter for "Last 3 days"
    await page.waitForSelector('#filter-dateposted', {'visible': True})
    await page.click('#filter-dateposted')

    # Wait for the dropdown to become visible and select the "Last 3 days" option
    await page.waitForSelector('a[href*="&fromage=3"]', {'visible': True})
    await page.click('a[href*="&fromage=3"]')

    # Wait for jobs to be filtered
    await page.waitForSelector('.jobsearch-SerpJobCard', {'visible': True})

    # Extract job details from the filtered results
    job_listings = await page.evaluate('''() => {
        const jobs = [];
        const jobCards = document.querySelectorAll('.jobsearch-SerpJobCard');
        jobCards.forEach((jobCard) => {
            const titleElement = jobCard.querySelector('.title a');
            const companyElement = jobCard.querySelector('.company');
            const locationElement = jobCard.querySelector('.location');
            const summaryElement = jobCard.querySelector('.summary');

            jobs.push({
                title: titleElement ? titleElement.innerText.trim() : '',
                company: companyElement ? companyElement.innerText.trim() : '',
                location: locationElement ? locationElement.innerText.trim() : '',
                summary: summaryElement ? summaryElement.innerText.trim() : '',
            });
        });
        return jobs;
    }''')

    # Close the browser
    await browser.close()

    return job_listings

# Run the function
job_title = "Software Engineer"
location = "New York, NY"

job_listings = asyncio.get_event_loop().run_until_complete(scrape_jobs_from_indeed(job_title, location))

# Print the job listings
for job in job_listings:
    print(f"Title: {job['title']}")
    print(f"Company: {job['company']}")
    print(f"Location: {job['location']}")
    print(f"Summary: {job['summary']}\n")
