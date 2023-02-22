from src.pre_built.brazilian_jobs import read_brazilian_file


def test_brazilian_jobs():
    jobs = read_brazilian_file('tests/mocks/brazilians_jobs.csv')
    keys = set()
    for job in jobs:
        for key in job.keys():
            keys.add(key)

    assert keys == {"title", "salary", "type"}
