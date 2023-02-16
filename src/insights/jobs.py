from functools import lru_cache
from typing import List, Dict
import csv


@lru_cache
def read(path: str) -> List[Dict]:
    with open(path) as file:
        reader = csv.DictReader(file, delimiter=",")
        data = [row for row in reader]

        return data


def get_unique_job_types(path: str) -> List[str]:
    jobs = read(path)
    unique_jobs = {job["job_type"] for job in jobs}
    return unique_jobs


def filter_by_job_type(jobs: List[Dict], job_type: str) -> List[Dict]:
    all_jobs = []
    for job in jobs:
        if job["job_type"] == job_type:
            all_jobs.append(job)
    return all_jobs
