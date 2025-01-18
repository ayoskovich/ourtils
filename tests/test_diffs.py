from pathlib import Path
import pandas as pd
import pytest
from ourtils.diffs import DataFrameDiffer, compare_sets, SetComparison

SAMPLE_DATA_LOCATION = Path("tests/sample_data")


def _read_file(file_name: str) -> pd.DataFrame:
    return pd.read_csv(SAMPLE_DATA_LOCATION / file_name)


@pytest.fixture
def standard_sets():
    return {1, 2, 5}, {5, 7, 10}


@pytest.fixture
def base_data():
    return _read_file("base_data.csv")


@pytest.fixture
def new_data():
    return _read_file("new_data.csv")


def test_set_diff_values(capsys, standard_sets):
    diff = compare_sets(*standard_sets, report=False)
    assert isinstance(diff, SetComparison)
    assert diff.only_a == {1, 2}
    assert diff.only_b == {7, 10}
    assert diff.in_both == {5}
    print_statement = capsys.readouterr().out
    assert not print_statement


def test_set_diff_prints(capsys, standard_sets):
    compare_sets(*standard_sets, report=True)
    print_statement = capsys.readouterr().out
    assert "Only A: {1, 2}" in print_statement
    assert "Only B: {10, 7}" in print_statement


def test_set_diff_coersion():
    list_a = ["anthony", "elmo"]
    list_b = ["elmo"]
    compare_sets(list_a, list_b)


def test_dataframe_differ():
    df1 = pd.DataFrame({"a": [1, 2, 3], "b": [4, 5, 6]})
    df2 = pd.DataFrame({"a": [1, 2, 4], "B": [4, 5, 1], "c": [5, 6, 1]})
    diffy = DataFrameDiffer(df1, df2, "a")

    assert diffy.matching_columns == {"a", "b"}
    assert diffy.missing_columns == set()
    assert diffy.new_columns == {"c"}


def test_diff_attributes(base_data, new_data):
    diff = DataFrameDiffer(base_data, new_data, join_on=["group"])
    assert diff.n_changed_rows == 4
    assert diff.new_columns == {"extra"}
    assert diff.matching_columns == {"score", "group"}
