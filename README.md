# EDAExcelReport

EDAExcelReport is a Python package for generating detailed exploratory data analysis (EDA) reports specifically for datasets with binary target variables. The package creates comprehensive EDA reports in Excel format, which include statistics and visualizations in the form of table that help in understanding the distribution and relationship of various features with the target variable.

## Features

- Calculates frequency and distribution of feature values.
- Computes target rate, percentage of total target, and lift for each feature value.
- Automatically handles numeric and categorical data.
- Generates Excel reports with well-formatted tables and conditional formatting.
- Removes gridlines and adds borders for better readability.

## Installation

You can install the package via pip:

```sh
pip install EDAExcelReport      


## Usage

### Importing the package


from EDAR.excel_report import EDAExcelReport

### Example Usage

Import necessary libraries
import pandas as pd
import numpy as np
import os

# Import EDAExcelReport
from EDAR.excel_report import EDAExcelReport

# Loading the credit dataset
df = pd.read_csv(r"tests\credit_data.csv")
df.columns
df.isna().sum()
ignore_feats = ["ID", "OCCUPATION_TYPE", "DAYS_BIRTH", "DAYS_EMPLOYED", "FLAG_MOBIL"]
EDAExcelReport(df, 'target', r'tests\test_eda_report.xlsx', ignore_cols=ignore_feats)

