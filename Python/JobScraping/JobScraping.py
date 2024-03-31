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

# Todo: Other websites mycareersfuture, glassdoor
# Todo: Do a readme as well

from pathlib import Path
import requests
from bs4 import BeautifulSoup
import math
import pandas as pd
import datetime
import re
import os
import path
import time
l = {}  # dict of jobids: url
o = {}  # dictionary of the attributes for each job
k = []  # list of all the dicts of each job
curr_date = datetime.date.today()

# Obtain max largest date currently
current_dir = Path.cwd()
files_in_cwd = os.listdir(current_dir)

dates_in_files = sum([re.findall(r'\d\d\d\d-\d\d-\d\d', x)
                     for x in files_in_cwd], [])
dates_in_files = [datetime.datetime.strptime(
    x, '%Y-%m-%d').date() for x in dates_in_files]

prev_date = max([x for x in dates_in_files if x != curr_date])

# target_url = 'https://www.linkedin.com/jobs-guest/jobs/api/seeMoreJobPostings/search?keywords=Python%20%28Programming%20Language%29&location=Las%20Vegas%2C%20Nevada%2C%20United%20States&geoId=100293800&currentJobId=3415227738&start={}'
# target_url = 'https://www.linkedin.com/jobs-guest/jobs/api/seeMoreJobPostings/search?currentJobId=3758282638&geoId=102454443&keywords=data&location=Singapore&start={}'
target_url = 'https://www.linkedin.com/jobs-guest/jobs/api/seeMoreJobPostings/search?keywords=pharmaceutical%20data%20analyst&location=Singapore&geoId=102454443&currentJobId=3849461768&start={}'


# Obtain all the jobids
for i in range(0, 1000, 25):

    res = requests.get(target_url.format(i))
    soup = BeautifulSoup(res.text, 'html.parser')

    print(res.status_code)
    alljobs_on_this_page = soup.find_all("li")
    alljobsurls_on_this_page = soup.find_all(
        'a', class_='base-card__full-link')
    # print(len(alljobs_on_this_page))
    for x in range(0, len(alljobs_on_this_page)):
        if alljobs_on_this_page[x].find("div", {"class": "base-card"}) is not None:
            jobid = alljobs_on_this_page[x].find(
                "div", {"class": "base-card"}).get('data-entity-urn').split(":")[3]
            # Extract the 'href' attribute containing the URL
            # try:
            #     url = alljobsurls_on_this_page[x].get('href')
            # except:
            #     url = f'https://www.linkedin.com/jobs-guest/jobs/api/jobPosting/{jobid}'

            # l[jobid] = url

            o['job_id'] = jobid
            o['company'] = alljobs_on_this_page[x].find(
                "a", class_="hidden-nested-link").text.strip()
            o["job-title"] = alljobs_on_this_page[x].find(
                "span", class_="sr-only").text.strip()
            try:
                o['date'] = alljobs_on_this_page[x].find(
                    'time', class_='job-search-card__listdate').get('datetime')
            except:
                o['date'] = None

            o["long_url"] = alljobs_on_this_page[x].find(
                'a', class_='base-card__full-link absolute top-0 right-0 bottom-0 left-0 p-0 z-[2]').get('href')

        k.append(o)
        o = {}


# for each job
# realised i was getting too many 429 status codes if I run this,

# target_url = 'https://www.linkedin.com/jobs-guest/jobs/api/jobPosting/{}'

# for jobid, l_url in l.items():
#     o['job_id'] = jobid

    # s_url = target_url.format(jobid)
    # resp = requests.get(s_url)
    # soup = BeautifulSoup(resp.text, 'html.parser')

    # Obtain the relevant information
    # try:
    #     o["company"] = soup.find(
    #         "div", {"class": "top-card-layout__card"}).find("a").find("img").get('alt')
    # except:
    #     o["company"] = None

    # try:
    #     o["company"] = soup.find(
    #         "a", class_="topcard__org-name-link topcard__flavor--black-link").text.strip()
    # except:
    #     o["company"] = None

    # try:
    #     o["job-title"] = soup.find(
    #         "div", {"class": "top-card-layout__entity-info"}).find("a").text.strip()
    # except:
    #     o["job-title"] = None

    # try:
    #     o["level"] = soup.find("ul", {"class": "description__job-criteria-list"}).find(
    #         "li").text.replace("Seniority level", "").strip()
    # except:
    #     o["level"] = None

    # # o['short_url'] = s_url
    # o["long_url"] = l_url

    # k.append(o)
    # o = {}

# Create today's csv file
df = pd.DataFrame(k)
df.dropna(how='all', inplace=True)
df.sort_values(by='date', ascending=False, inplace=True)
df.to_csv(f'linkedinjobs{curr_date}.csv', index=False, encoding='utf-8')

# Compare with the latest previous csv file
prev_df = pd.read_csv(
    f'linkedinjobs{prev_date}.csv', index_col=False, encoding='utf-8')

new_df = df[~df['job_id'].isin(prev_df['job_id'])]

new_df.to_csv(f'new_linkedinjobs{curr_date}.csv',
              index=False, encoding='utf-8')
