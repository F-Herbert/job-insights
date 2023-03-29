from functools import lru_cache
from typing import List, Dict
import csv

path = 'data/jobs.csv'


@lru_cache
def read(path: str) -> List[Dict]:
    list_dict = []
    with open(path) as file:
        contents = csv.DictReader(file)
        print(contents)
        for content in contents:
            list_dict.append(content)
    return list_dict


def get_unique_job_types(path: str) -> List[str]:
    contents = read(path)
    for content in contents:
        print(content['job_type'])


get_unique_job_types(path)


def filter_by_job_type(jobs: List[Dict], job_type: str) -> List[Dict]:
    """Filters a list of jobs by job_type

    Parameters
    ----------
    jobs : list
        List of jobs to be filtered
    job_type : str
        Job type for the list filter

    Returns
    -------
    list
        List of jobs with provided job_type
    """
    raise NotImplementedError
