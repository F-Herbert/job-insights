from src.pre_built.sorting import sort_by
import pytest


@pytest.fixture
def file():
    return [
        {"date_posted": "2023-01-18", "max_salary": 5000, "min_salary": ""},
        {"date_posted": "", "max_salary": 3000, "min_salary": 2000},
        {"date_posted": "2023-02-01", "max_salary": "", "min_salary": 5000},
    ]


def test_sort_by_criteria(file):
    sort_by(file, "date_posted")
    assert file[0]["date_posted"] == "2023-02-01"
