import requests
from bs4 import BeautifulSoup as bs
import pandas as pd

# Set the parameters for the job search
position = 'data scientist'
location = 'Medellín'

# Create the URL for the search based on the parameters
url_search = 'http://api.scraperapi.com?api_key=78a886ae4fad62c98b5b0fe5a13de167&amp;amp;amp;amp;url=https://www.linkedin.com/jobs/search/?keywords=%s&location=%s' % (
    position, location)

# Set the header for the request
head = {'User-Agent': 'Mozilla/5.0'}

# Send a GET request to the URL and store the response
response = requests.get(url_search, headers=head).text

# Create a BeautifulSoup object from the response
soup = bs(response)

# Find the job search results list in the HTML
joblist = soup.find('ul', attrs={"class": "jobs-search__results-list"})

# Find all the jobs in the results list
alljobs = joblist.find_all('li')

# Get the first job in the list for testing purposes
job = alljobs[0]

# Extract the location from the job
location = job.find('span', attrs={"class": "job-search-card__location"}).text

# Extract the title from the job
title = job.find('div', {'class': 'base-search-card__info'}).h3.text

# Extract the company name from the job
company = job.find('div', {'class': 'base-search-card__info'}).h4.text

# Extract the URL for the job listing
joburl = job.find("a").get("href")

# Create a pandas DataFrame to store the job information
df_jobs = pd.DataFrame(columns=['Location', 'Title', 'Company', 'Url'])

# Loop through all the jobs in the list and extract the relevant information
for i in range(len(alljobs)):
    job = alljobs[i]
    location = job.find(
        'span', attrs={"class": "job-search-card__location"}).text.replace('\n', '')
    title = job.find(
        'div', {'class': 'base-search-card__info'}).h3.text.replace('\n', '')
    company = job.find(
        'div', {'class': 'base-search-card__info'}).h4.text.replace('\n', '')
    joburl = job.find("a").get("href")
    df_jobs = df_jobs.append({'Location': location, 'Title': title,
                             'Company': company, 'Url': joburl}, ignore_index=True)

# Save the job information to a CSV file
df_jobs.to_csv('Trabajos.csv')
