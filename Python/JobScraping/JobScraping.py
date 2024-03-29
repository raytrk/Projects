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

# Todo: See if i can improve the matching of the company, job title and level for each jobposting
''' 
company:        
<div class="topcard__flavor-row">
          <span class="topcard__flavor">
              <a class="topcard__org-name-link topcard__flavor--black-link" data-tracking-control-name="public_jobs_topcard-org-name" data-tracking-will-navigate href="https://www.linkedin.com/company/bytedance?trk=public_jobs_topcard-org-name" rel="noopener" target="_blank">

job title:
<h2 class="top-card-layout__title font-sans text-lg papabear:text-xl font-bold leading-open text-color-text mb-0 topcard__title">Data Analyst, BytePlus Recommend</h2>
              
level:
      <ul class="description__job-criteria-list">
        <li class="description__job-criteria-item">
          <h3 class="description__job-criteria-subheader">
            Seniority level
          </h3>
          <span class="description__job-criteria-text description__job-criteria-text--criteria">
            Mid-Senior level
          </span>
        </li>

'''

import requests
from bs4 import BeautifulSoup
import math
import pandas as pd
from datetime import date, timedelta
import re
l = {}  # dict of jobids: url
o = {}  # dictionary of the attributes for each job
k = []  # list of all the dicts of each job
curr_date = date.today()
prev_date = curr_date - timedelta(days=1)

# target_url = 'https://www.linkedin.com/jobs-guest/jobs/api/seeMoreJobPostings/search?keywords=Python%20%28Programming%20Language%29&location=Las%20Vegas%2C%20Nevada%2C%20United%20States&geoId=100293800&currentJobId=3415227738&start={}'
# target_url = 'https://www.linkedin.com/jobs-guest/jobs/api/seeMoreJobPostings/search?currentJobId=3758282638&geoId=102454443&keywords=data&location=Singapore&start={}'
target_url = 'https://www.linkedin.com/jobs-guest/jobs/api/seeMoreJobPostings/search?keywords=pharmaceutical%20data%20analyst&location=Singapore&geoId=102454443&currentJobId=3849461768&start={}'

# Obtain all the jobids
for i in range(0, 500, 25):  # range(0, 500, 25):

    res = requests.get(target_url.format(i))
    soup = BeautifulSoup(res.text, 'html.parser')
    alljobs_on_this_page = soup.find_all("li")
    alljobsurls_on_this_page = soup.find_all(
        'a', class_='base-card__full-link')
    # print(len(alljobs_on_this_page))
    for x in range(0, len(alljobs_on_this_page)):
        if alljobs_on_this_page[x].find("div", {"class": "base-card"}) is not None:
            jobid = alljobs_on_this_page[x].find(
                "div", {"class": "base-card"}).get('data-entity-urn').split(":")[3]
            # Extract the 'href' attribute containing the URL
            try:
                url = alljobsurls_on_this_page[x].get('href')
            except:
                url = ''
            l[jobid] = url

target_url = 'https://www.linkedin.com/jobs-guest/jobs/api/jobPosting/{}'

# for each job
for jobid, l_url in l.items():

    s_url = target_url.format(jobid)
    resp = requests.get(s_url)
    soup = BeautifulSoup(resp.text, 'html.parser')

    o['job_id'] = jobid

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

    # o['short_url'] = s_url
    o["long_url"] = l_url

    k.append(o)
    o = {}

df = pd.DataFrame(k)
df.to_csv(f'linkedinjobs{curr_date}.csv', index=False, encoding='utf-8')

df = pd.read_csv(f'linkedinjobs{curr_date}.csv',
                 index_col=False, encoding='utf-8')

prev_df = pd.read_csv(
    f'linkedinjobs{prev_date}.csv', index_col=False, encoding='utf-8')

new_df = df[~df['job_id'].isin(prev_df['job_id'])]

new_df.to_csv(f'new_linkedinjobs{curr_date}.csv',
              index=False, encoding='utf-8')

# #print(k)
