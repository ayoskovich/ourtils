import pandas as pd
from ourtils.modeling import standardize


def test_standardize_whole_frame():
    frame = pd.DataFrame({"a": [1, 2, 3, 4, 5]})
    frame.apply(standardize)


def test_standardize_values():
    actual = standardize(pd.Series([1, 2, 3, 4, 5]))
    expected = pd.Series(
        [
            -1.414213562373095,
            -0.7071067811865475,
            0.0,
            0.7071067811865475,
            1.414213562373095,
        ]
    )
    pd.testing.assert_series_equal(actual, expected)
