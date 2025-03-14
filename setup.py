from setuptools import setup, find_packages

# List of contributors
contributors = [
    "Rohit Kosamkar <rohitkosamkar97@gmail.com>"
]

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="EDAExcelReport",  
    version="0.1.9",  
    author="Rohit Kosamkar",
    author_email="rohitkosamkar97@gmail.com",
    description="A Python package for generating detailed EDA reports in Excel format with structured insights and visualizations.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/rohit180497/EDAExcelReport",  
    packages=find_packages(),
    include_package_data=True,
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "Intended Audience :: Science/Research",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Topic :: Scientific/Engineering :: Artificial Intelligence",
        "Topic :: Scientific/Engineering :: Information Analysis",
        "Topic :: Scientific/Engineering :: Visualization",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    keywords=[
        "EDA", "Excel", "exploratory data analysis", "report", "pandas", "numpy", "openpyxl", 
        "machine learning", "data science", "data analysis", "EDAExcelReport", "profiling", 
        "Visualization", "Excel report", "python EDA report"
    ],
    python_requires='>=3.6',
    install_requires=[
        "pandas>=1.2.0",  
        "openpyxl>=3.0.0",
        "numpy>=1.19.0",
        "scikit-learn>=0.24.0",
        "datetime"
    ],
    entry_points={
        "console_scripts": [
            "eda_contributors=EDAExcelReport.contributors:set_contributors"
        ]
    },
    project_urls={
        "Bug Tracker": "https://github.com/rohit180497/EDAExcelReport/issues",
        "Documentation": "https://github.com/rohit180497/EDAExcelReport#readme",
        "Source Code": "https://github.com/rohit180497/EDAExcelReport"
    },
)