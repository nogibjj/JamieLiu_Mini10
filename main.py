"""
Main CLI or app entry point
"""

from mylib.lib import (
    extract,
    load_data,
    describe,
    query,
    example_transform,
    start_spark,
    end_spark,
)


def main():
    # Extract data
    extract()
    # Start Spark session
    spark = start_spark("DrinksDataAnalysis")
    # Load data into DataFrame
    df = load_data(spark)
    # Example metrics
    describe(df)
    # Query
    sql_query = (
        "SELECT country, beer_servings, total_litres_of_pure_alcohol "
        "FROM Drinks "
        "WHERE beer_servings > 100"
    )
    query(
        spark,
        df,
        sql_query,
        "Drinks",
    )
    # Example transform
    example_transform(df)
    # End Spark session
    end_spark(spark)


if __name__ == "__main__":
    main()
