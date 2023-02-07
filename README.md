# LinkedIn Job Scraper

This script is a job scraper that retrieves job information from LinkedIn. The user can specify the job title and location they want to search for and the script will return a CSV file with information about the available jobs.

## Getting Started

The following instructions will guide you through how to run this script on your local machine.

### Prerequisites

The following packages are required to run this script:

- requests
- bs4
- pandas

### Installing

To install the required packages, open a terminal and run the following command:

```sh
pip install requests bs4 pandas
```

### Usage

- Set the parameters for the job search by replacing the `position` and `location` variables with the desired job title and location, respectively.

- Replace the `url_search` variable with your own API key for [scraperapi.com](https://www.scraperapi.com/).

- Run the script by executing the following command in your terminal:

```sh
python linkedin_job_scraper.py
```

- A CSV file named `Trabajos.csv` will be generated in the same directory as the script. The file will contain information about the job search results, including the location, title, company, and URL for each job listing.

## Built With

- [requests](https://docs.python-requests.org/en/master/) - A Python library used to send HTTP requests.
- [BeautifulSoup](https://www.crummy.com/software/BeautifulSoup/bs4/doc/) - A Python library used to parse HTML and XML.
- [pandas](https://pandas.pydata.org/) - A Python library used for data analysis and manipulation.

## License

This project is Open source
