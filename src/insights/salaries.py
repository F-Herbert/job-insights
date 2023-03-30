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
    """Filters a list of jobs by salary range

    Parameters
    ----------
    jobs : list
        The jobs to be filtered
    salary : int
        The salary to be used as filter

    Returns
    -------
    list
        Jobs whose salary range contains `salary`
    """
    raise NotImplementedError
