# JamieLiu_Mini10
[![CI](https://github.com/nogibjj/JamieLiu_Mini10/actions/workflows/cicd.yml/badge.svg)](https://github.com/nogibjj/JamieLiu_Mini10/actions/workflows/cicd.yml)

## Project Overview
This project uses **PySpark** to process and analyze global alcohol consumption data. It includes steps for data extraction, loading, transformation, and querying. The project runs in a **GitHub Codespaces** environment and provides a CI/CD pipeline for testing and code quality checks.

## Project Structure
```
JamieLiu_Mini10/
├── data/                       # Contains the downloaded dataset
│   └── drinks.csv
├── mylib/
│   ├── __init__.py             
│   └── lib.py                  # Core PySpark functions (extract, load, transform, etc.)
├── .devcontainer/
│   ├── devcontainer.json       # Config for Codespaces environment
│   └── Dockerfile              # Dockerfile for environment setup
├── .github/workflows/
│   └── cicd.yml                # GitHub Actions workflow for CI/CD
├── .gitignore
├── main.py                     # Main script to execute data processing
├── test_main.py                # Tests for the data processing pipeline
├── requirements.txt            # Project dependencies
├── Makefile                    # Automation tasks
└── README.md                   # Project documentation
```

## Setup and Usage

1. **Open Codespaces**: Go to the GitHub repository and open it in Codespaces.
2. **Wait for Environment Setup**: Codespaces will automatically install dependencies and configure the environment.
3. **Run the Project**: Once setup is complete, run the main script:
   `python main.py`

## Core Functions
The main functions in `mylib/lib.py` include:

1. **extract**: Downloads the dataset from a specified URL and saves it to the `data/` directory.
2. **load_data**: Loads the dataset into a PySpark DataFrame with a defined schema.
3. **describe**: Logs descriptive statistics of the DataFrame.
4. **query**: Runs a SQL query on the loaded DataFrame and logs the results.
5. **example_transform**: Adds a new column to categorize countries based on beer consumption levels.


## Process

The workflow of this project is organized as follows:

1. **Extract the Dataset**: 
   - The `extract` function downloads the dataset from a specified URL and saves it to the `data/` directory.
   - This step ensures the latest version of the data is available for processing.

2. **Initialize Spark Session**:
   - The `start_spark` function initializes a Spark session, which is required for distributed data processing with PySpark.

3. **Load the Dataset**:
   - The `load_data` function reads the `drinks.csv` file into a PySpark DataFrame with a specified schema.
   - It also logs a preview of the data to help verify that it has loaded correctly.

4. **Descriptive Statistics**:
   - The `describe` function computes summary statistics (e.g., mean, standard deviation) for the dataset.
   - This step helps to understand the general distribution of data values.

5. **Query the Data**:
   - The `query` function performs SQL queries on the dataset to extract specific insights.
   - For example, one query filters countries with high beer consumption by selecting records where `beer_servings` exceeds a threshold.

6. **Data Transformation**:
   - The `example_transform` function performs transformations on the data, such as categorizing countries based on beer consumption levels.
   - This step is useful for creating derived columns or labels for further analysis.

7. **End Spark Session**:
   - The `end_spark` function closes the Spark session, freeing up resources.


## Output Log

The results of each step in the data processing pipeline are recorded in a markdown file [pyspark_output.md](./pyspark_output.md). 