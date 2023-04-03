from src.pre_built.brazilian_jobs import read_brazilian_file

path = "tests/mocks/brazilians_jobs.csv"
dic_mock = {"title": "Maquinista", "salary": "2000", "type": "trainee"}


def test_brazilian_jobs():
    result = read_brazilian_file(path)
    assert result[0] == dic_mock
