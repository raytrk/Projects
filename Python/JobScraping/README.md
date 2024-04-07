# Web Scrapping LinkedIn Jobs

## Description:

### Summary:

> This Project collates the latest jobs from a particular LinkedIn query and outputs a CSV file with details of the job listing.

### Tools used:

1. Python
2. Virtual Environments
3. Docker Containers

### Main Features:

#### Features:

1. Scraping of LinkedIn jobs based on keywords and location
2. Extraction of job details: job ID, company, job title, date posted, and job URL
3. Listings are sorted in descending order based on listing date to show the latest listings at the top.
4. CSV file generation
5. Dockerize the project (optional for containerized execution)

#### Input:

Customize Search Criteria:

- Modify the target_url variable in the script to include your desired keywords and location parameters. You can find these parameters in the URL of a LinkedIn job search page

#### Output:

The script creates and updates the CSV file containing the latest list of scraped job data in the relevant linkedinjobs directory

### Learning Points:

1. LinkedIn may throttle or block excessive scraping requests, leading to inconsistent results but regular scraping that updates the latest file of jobs should help cirvumvent this issue.
2. Using Docker is not as overwhelming as imagined, but it is important to add in not just the python file used but also the paths that the script references.

## References

1. Virtual environments: https://docs.python.org/3/library/venv.html#how-venvs-work
2. Scraping Linkedin default file from: https://www.scrapingdog.com/blog/scrape-linkedin-jobs/
3. Docker:
   a. https://docs.docker.com/get-started/overview/
   b. https://www.youtube.com/watch?v=jtBVppyfDbE
   c. https://www.youtube.com/watch?v=0UG2x2iWerk
