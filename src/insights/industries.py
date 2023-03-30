from typing import List, Dict
from src.insights.jobs import read
# src.insights.
path = 'data/jobs.csv'


def get_unique_industries(path: str) -> List[str]:
    contents = read(path)
    filter_contents = []
    for content in contents:
        if content['industry'] not in filter_contents:
            filter_contents.append(content['industry'])
    list_without_space = [char for char in filter_contents if char != '']
    return list_without_space


def filter_by_industry(jobs: List[Dict], industry: str) -> List[Dict]:
    list_of_jobs = []
    for job in jobs:
        if job['industry'] == industry:
            list_of_jobs.append(job["industry"])
    return list_of_jobs
