"""
Tests for Drinks Data Analysis
"""

import os
import pytest
from mylib.lib import (
    extract,
    load_data,
    describe,
    query,
    example_transform,
    start_spark,
    end_spark,
)


@pytest.fixture(scope="module")
def spark():
    spark = start_spark("TestApp")
    yield spark
    end_spark(spark)


def test_extract():
    file_path = extract()
    assert os.path.exists(file_path) is True


def test_load_data(spark):
    df = load_data(spark)
    assert df is not None
    assert df.count() > 0  # Ensure data is loaded


def test_describe(spark):
    df = load_data(spark)
    result = describe(df)
    assert result is None  # Assuming `describe` logs the output without returning


def test_query(spark):
    df = load_data(spark)
    query_str = (
        "SELECT country, beer_servings, total_litres_of_pure_alcohol "
        "FROM Drinks "
        "WHERE beer_servings > 100"
    )
    result = query(spark, df, query_str, "Drinks")
    assert result is None  # Assuming `query` logs the output without returning


def test_example_transform(spark):
    df = load_data(spark)
    result = example_transform(df)
    assert (
        result is None
    )  # Assuming `example_transform` logs the output without returning


if __name__ == "__main__":
    test_extract()
    test_load_data(spark)
    test_describe(spark)
    test_query(spark)
    test_example_transform(spark)
