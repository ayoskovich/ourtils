from ourtils.excel import index_to_excel_column, excel_column_index


def test_excel_indexes():
    for i in range(1, 100):
        colname: str = index_to_excel_column(i)
        colindex: int = excel_column_index(colname)
        assert colindex == i

    assert index_to_excel_column(5) == "E"
    assert excel_column_index("E") == 5
