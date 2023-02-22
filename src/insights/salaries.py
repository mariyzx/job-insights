from typing import Union, List, Dict
import csv


def read(path: str) -> List[Dict]:
    with open(path) as file:
        reader = csv.DictReader(file, delimiter=",")
        data = [row for row in reader]

        return data


def get_max_salary(path: str) -> int:
    jobs = read(path)
    all_salaries = []
    for job in jobs:
        if job["max_salary"] != '' and job["max_salary"].isnumeric():
            all_salaries.append(int(job["max_salary"]))
    max_salary = max(all_salaries)
    return max_salary


def get_min_salary(path: str) -> int:
    jobs = read(path)
    all_salaries = []
    for job in jobs:
        if job["min_salary"] != '' and job["min_salary"].isnumeric():
            all_salaries.append(int(job["min_salary"]))
    max_salary = min(all_salaries)
    return max_salary


def is_not_empty(*values):
    is_valid_values = True
    for value in values:
        if (value == ''):
            is_valid_values = False
            break
    return is_valid_values


def is_int(*values):
    is_valid_values = True
    for value in values:
        if (type(value) != int):
            is_valid_values = False
            break
    return is_valid_values


def matches_salary_range(job: Dict, salary: Union[int, str]) -> bool:
    if 'min_salary' not in job or 'max_salary' not in job:
        raise ValueError('empty fields')

    min_salary = job["min_salary"]
    max_salary = job["max_salary"]

    if (not is_int(min_salary, max_salary)):
        raise ValueError('value is not numeric')
    elif min_salary > max_salary:
        raise ValueError('min_salary greater than max_salary')
    else:
        return min_salary <= int(salary) <= max_salary


def filter_by_salary_range(
    jobs: List[dict],
    salary: Union[str, int]
) -> List[Dict]:
    list_jobs = []

    try:
        for job in jobs:
            if int(job["min_salary"]) <= int(salary) <= int(job["max_salary"]):
                list_jobs.append(job)
    except TypeError:
        raise ValueError("error")
    finally:
        return list_jobs
