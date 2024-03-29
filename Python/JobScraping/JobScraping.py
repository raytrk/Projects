# This script serves to scrape websites daily from the following websites
'''
1. Linkedin
2. Mycareersfuture
3. Glassdoor

References:
Virtual environments: https://docs.python.org/3/library/venv.html#how-venvs-work
Scraping Linkedin default file from: https://www.scrapingdog.com/blog/scrape-linkedin-jobs/
Docker: https://www.youtube.com/watch?v=jtBVppyfDbE
Docker: https://www.youtube.com/watch?v=0UG2x2iWerk
'''

# Todo: Figure out how to obtain the url to the job posting
# Todo: Figure out how to compare with the csv from the day before and obtain the new postings - can use the compare pandas function

import requests
from bs4 import BeautifulSoup
import math
import pandas as pd
from datetime import date, timedelta
import re
l = []  # list of jobids
o = {}  # dictionary of the attributes for each job
k = []  # list of all the dicts of each job
curr_date = date.today()
prev_date = curr_date - timedelta(days=1)

# target_url = 'https://www.linkedin.com/jobs-guest/jobs/api/seeMoreJobPostings/search?keywords=Python%20%28Programming%20Language%29&location=Las%20Vegas%2C%20Nevada%2C%20United%20States&geoId=100293800&currentJobId=3415227738&start={}'
# target_url = 'https://www.linkedin.com/jobs-guest/jobs/api/seeMoreJobPostings/search?currentJobId=3758282638&geoId=102454443&keywords=data&location=Singapore&start={}'
target_url = 'https://www.linkedin.com/jobs-guest/jobs/api/seeMoreJobPostings/search?keywords=pharmaceutical%20data%20analyst&location=Singapore&geoId=102454443&currentJobId=3849461768&start={}'

# Obtain all the jobids
for i in range(0, 500, 25):

    res = requests.get(target_url.format(i))
    soup = BeautifulSoup(res.text, 'html.parser')
    alljobs_on_this_page = soup.find_all("li")
    # print(len(alljobs_on_this_page))
    for x in range(0, len(alljobs_on_this_page)):
        if alljobs_on_this_page[x].find("div", {"class": "base-card"}) is not None:
            jobid = alljobs_on_this_page[x].find(
                "div", {"class": "base-card"}).get('data-entity-urn').split(":")[3]
            l.append(jobid)

target_url = 'https://www.linkedin.com/jobs-guest/jobs/api/jobPosting/{}'

# for each job
for j in range(0, len(l)):

    resp = requests.get(target_url.format(l[j]))
    soup = BeautifulSoup(resp.text, 'html.parser')

    # Obtain the relevant information
    try:
        o["company"] = soup.find(
            "div", {"class": "top-card-layout__card"}).find("a").find("img").get('alt')
    except:
        o["company"] = None

    try:
        o["job-title"] = soup.find(
            "div", {"class": "top-card-layout__entity-info"}).find("a").text.strip()
    except:
        o["job-title"] = None

    try:
        o["level"] = soup.find("ul", {"class": "description__job-criteria-list"}).find(
            "li").text.replace("Seniority level", "").strip()
    except:
        o["level"] = None

    try:
        o["url"] = soup.findall('a', href=True)[1]['href']
    except:
        o["url"] = None

    k.append(o)
    o = {}

df = pd.DataFrame(k)
df.to_csv(f'linkedinjobs{curr_date}.csv', index=False, encoding='utf-8')

# #prev_df = pd.read_csv(f'linkedinjobs{prev_date}.csv', index=False, encoding='utf-8')

# #print(k)
