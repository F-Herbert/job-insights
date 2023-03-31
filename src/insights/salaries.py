from typing import Union, List, Dict
from src.insights.jobs import read
# src.insights.
path = "data/jobs.csv"


def get_max_salary(path: str) -> int:
    contents = read(path)
    all_values = []
    for content in contents:
        if content["max_salary"] not in contents:
            if not content["max_salary"].isalpha():
                all_values.append(content["max_salary"])
    all_values_wihout_space = [
        int(value) for value in all_values if value != ""
    ]
    max_number = max(all_values_wihout_space)
    return max_number


def get_min_salary(path: str) -> int:
    contents = read(path)
    all_values = []
    for content in contents:
        if content["min_salary"] not in contents:
            if not content["min_salary"].isalpha():
                all_values.append(content["min_salary"])
    all_values_wihout_space = [
        int(value) for value in all_values if value != ""
    ]
    return min(all_values_wihout_space)


def matches_salary_range(job: Dict, salary: Union[int, str]) -> bool:
    try:
        min_salary = int(job["min_salary"])
        max_salary = int(job["max_salary"])
        salary = int(salary)
    except TypeError:
        raise ValueError("Invalid number")
    except KeyError:
        raise ValueError("Invalid number")
    else:
        if min_salary > max_salary:
            raise ValueError("Min greater than Max")
        return min_salary <= salary <= max_salary


def filter_by_salary_range(
    jobs: List[dict], salary: Union[str, int]
) -> List[Dict]:
    jobs_valids = []
    for job in jobs:
        try:
            result = matches_salary_range(job, salary)
            print(result)
            if result is True:
                jobs_valids.append(job)
        except Exception:
            pass
    return jobs_valids


jobs = [
        {"max_salary": 0, "min_salary": 10},
        {"max_salary": 10, "min_salary": 100},
        {"max_salary": 10000, "min_salary": 200},
        {"max_salary": 15000, "min_salary": 0},
        {"max_salary": 1500, "min_salary": 0},
        {"max_salary": -1, "min_salary": 10},
    ]


# print(filter_by_salary_range(jobs, 100))
