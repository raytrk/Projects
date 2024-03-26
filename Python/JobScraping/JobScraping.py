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

# todo: Figure out how to add in the link to the linkedin posting in my csv
# Figure out how to change the search terms for the python file especially the location

import requests
from bs4 import BeautifulSoup
import math
import pandas as pd
l = []
o = {}
k = []
target_url = 'https://www.linkedin.com/jobs-guest/jobs/api/seeMoreJobPostings/search?keywords=pharmaceutical%20data%20analyst&location=Singapore&geoId=102454443&currentJobId=3849461768&start={}'
for i in range(0, math.ceil(117/25)):

    res = requests.get(target_url.format(i))
    soup = BeautifulSoup(res.text, 'html.parser')
    alljobs_on_this_page = soup.find_all("li")
    print(len(alljobs_on_this_page))
    for x in range(0, len(alljobs_on_this_page)):
        jobid = alljobs_on_this_page[x].find(
            "div", {"class": "base-card"}).get('data-entity-urn').split(":")[3]
        l.append(jobid)

target_url = 'https://www.linkedin.com/jobs-guest/jobs/api/jobPosting/{}'
for j in range(0, len(l)):

    resp = requests.get(target_url.format(l[j]))
    soup = BeautifulSoup(resp.text, 'html.parser')

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

    k.append(o)
    o = {}

df = pd.DataFrame(k)
df.to_csv('linkedinjobs.csv', index=False, encoding='utf-8')
# print(k)
