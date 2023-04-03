from src.pre_built.sorting import sort_by

dic_mock = {"title": "Maquinista", "salary": "2000", "type": "trainee"}
dick_mock2 = {
    "title": "Analista de Software",
    "salary": "4000",
    "type": "full time",
}
dick_mock3 = {"title": "Motorista", "salary": "3000", "type": "full time"}

array_of_dict = [dic_mock, dick_mock2, dick_mock3]


def test_sort_by_criteria():
    result = sort_by(array_of_dict, "min_salary")
    assert result == dic_mock
