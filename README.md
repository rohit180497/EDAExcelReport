In this `README.md`, I have included the following sections:
- Features
- Installation
- Usage
- Important Note about handling null values
- Input Parameters with descriptions
- Example Usage
- Screenshots
- License

Additionally, I've provided an example showing how to remove or impute null values before generating the EDA report. This ensures users understand the importance of handling null values in their datasets.



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
```

```python

# How to import?
from EDAR.excel_report import EDAExcelReport

```


```python
# Import necessary libraries
import pandas as pd
import numpy as np
import os
from EDAR.excel_report import EDAExcelReport

```

```python
# Loading the credit dataset
df = pd.read_csv(r"tests\credit_data.csv")
```

```python
df.columns
```
    Index(['ID', 'CODE_GENDER', 'FLAG_OWN_CAR', 'FLAG_OWN_REALTY', 'CNT_CHILDREN',
           'AMT_INCOME_TOTAL', 'NAME_INCOME_TYPE', 'NAME_EDUCATION_TYPE',
           'NAME_FAMILY_STATUS', 'NAME_HOUSING_TYPE', 'DAYS_BIRTH',
           'DAYS_EMPLOYED', 'FLAG_MOBIL', 'FLAG_WORK_PHONE', 'FLAG_PHONE',
           'FLAG_EMAIL', 'OCCUPATION_TYPE', 'CNT_FAM_MEMBERS', 'target'],
          dtype='object')


```python
df.isna().sum()
```
    ID                         0
    CODE_GENDER                0
    FLAG_OWN_CAR               0
    FLAG_OWN_REALTY            0
    CNT_CHILDREN               0
    AMT_INCOME_TOTAL           0
    NAME_INCOME_TYPE           0
    NAME_EDUCATION_TYPE        0
    NAME_FAMILY_STATUS         0
    NAME_HOUSING_TYPE          0
    DAYS_BIRTH                 0
    DAYS_EMPLOYED              0
    FLAG_MOBIL                 0
    FLAG_WORK_PHONE            0
    FLAG_PHONE                 0
    FLAG_EMAIL                 0
    OCCUPATION_TYPE        11323
    CNT_FAM_MEMBERS            0
    target                     0
    dtype: int64


```python
ignore_feats = ["ID", "OCCUPATION_TYPE", "DAYS_BIRTH", "DAYS_EMPLOYED", "FLAG_MOBIL"]
```

```python
EDAExcelReport(df, 'target',r'tests\test_eda_report.xlsx', ignore_cols= ignore_feats)
```

    Your EDA report is ready at tests\test_eda_report_20240610_153828.xlsx
    
    <ed_report.excel_report.EDAExcelReport at 0x188c09ee9f0>


## Important Note 

Ensure your dataset is free of null values before using the EDAExcelReport package. This is crucial because numeric data is bucketed during the analysis, and the presence of null values can interfere with the bucket creation process. Additionally, having null values in the dataset can lead to inaccurate or misleading results when showcasing the report to stakeholders.

### Example

```python
# Remove or impute null values
df.fillna(method='ffill', inplace=True)
```

## Input Parameters

### EDAExcelReport

```python

class EDAExcelReport:
    def __init__(self, data, target, report_path, ignore_cols=None, cat_label_enco_thresh=0.05, num_min_samples_leaf=0.1, conditional_color='red'):


`data:` The input DataFrame containing the dataset.
`target:` The name of the target column in the DataFrame.
`report_path:` The file path where the Excel report will be saved.
`ignore_cols:` (Optional) List of column names to ignore in the analysis.
`cat_label_enco_thresh:` (Optional) Threshold for label encoding of categorical variables (default is 0.05).
`num_min_samples_leaf:` (Optional) Minimum samples per leaf for numeric data bucketing (default is 0.1).
`conditional_color:` (Optional) The color used for conditional formatting in the report (default is 'red').

```
### Exploratory Data Analysis Excel File for above Credit Data you can download from here: 

[Download Excel File](https://github.com/rohit180497/EDAExcelReport/blob/main/tests/test_eda_report_20240610_153828.xlsx)

## Screenshots

### Screenshot 1
![Screenshot 1](https://github.com/rohit180497/EDAExcelReport/blob/main/images/Snapshot_of_EDA_excel_report1.png?raw=true)

### Screenshot 2
![Screenshot 2](https://github.com/rohit180497/EDAExcelReport/blob/main/images/Snapshot_of_EDA_excel_report2.png?raw=true)

### Screenshot 3
![Screenshot 3](https://github.com/rohit180497/EDAExcelReport/blob/main/images/Snapshot_of_EDA_excel_report3.png?raw=true)

### Screenshot 4
![Screenshot 4](https://github.com/rohit180497/EDAExcelReport/blob/main/images/Snapshot_of_EDA_excel_roc_report.png?raw=true)


## License

This project is licensed under the MIT License.

