from functools import lru_cache
from typing import List, Dict
import csv


@lru_cache
def read(path: str) -> List[Dict]:
    list_dict = []
    with open(path) as file:
        contents = csv.DictReader(file)
        for content in contents:
            list_dict.append(content)
    return list_dict


def get_unique_job_types(path: str) -> List[str]:
    contents = read(path)
    filter_contents = []
    for content in contents:
        if content["job_type"] not in filter_contents:
            filter_contents.append(content["job_type"])

    return filter_contents


def filter_by_job_type(jobs: List[Dict], job_type: str) -> List[Dict]:
    list_of_jobs = []
    for job in jobs:
        if job['job_type'] == job_type:
            list_of_jobs.append(job["job_type"])
    return list_of_jobs
