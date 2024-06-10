from setuptools import setup, find_packages

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name="EDA_report",  
    version="0.1.0",  
    author="Rohit Kosamkar",
    author_email="rohitkosamkar97@gmail.com",
    description="A package for generating EDA reports",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/rohit180497/EDA_report",  
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
    install_requires=[
        "pandas",  # Add other dependencies as needed
        "openpyxl",
        "numpy",
        "scikit-learn",
        "datetime"
    ],
)