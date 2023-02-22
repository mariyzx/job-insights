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


def matches_salary_range(job: Dict, salary: Union[int, str]) -> bool:
    if 'min_salary' not in job or 'max_salary' not in job:
        raise ValueError('empty fields')
    if type(job["min_salary"]) != int or type(job["max_salary"]) != int:
        raise ValueError('value is not numeric')
    elif job["min_salary"] > job["max_salary"]:
        raise ValueError('min_salary greater than max_salary')
    else:
        return job["min_salary"] <= int(salary) <= job["max_salary"]


def filter_by_salary_range(
    jobs: List[dict],
    salary: Union[str, int]
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
