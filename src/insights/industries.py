from typing import List, Dict
import csv


def read(path: str) -> List[Dict]:
    with open(path) as file:
        reader = csv.DictReader(file, delimiter=",")
        data = [row for row in reader]

        return data


def get_unique_industries(path: str) -> List[str]:
    industries = read(path)
    unique_industries = {industry["industry"] for industry in industries}
    without_empty_industry = list(filter(None, unique_industries))
    return without_empty_industry


def filter_by_industry(jobs: List[Dict], industry: str) -> List[Dict]:
    """Filters a list of jobs by industry

    Parameters
    ----------
    jobs : list
        List of jobs to be filtered
    industry : str
        Industry for the list filter

    Returns
    -------
    list
        List of jobs with provided industry
    """
    raise NotImplementedError
