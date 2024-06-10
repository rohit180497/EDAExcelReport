from setuptools import setup, find_packages

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name="EDAExcelReport",  
    version="0.1.2",  
    author="Rohit Kosamkar",
    author_email="rohitkosamkar97@gmail.com",
    description="A package for generating EDA reports",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/rohit180497/EDAExcelReport",  
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Intended Audience :: Developers",
        "Intended Audience :: Science/Research",
        "Topic :: Scientific/Engineering :: Artificial Intelligence",
        "Topic :: Scientific/Engineering :: Information Analysis",
        "Topic :: Scientific/Engineering :: Visualization",
    ],
    keywords="EDA Excel exploratory data analysis report pandas numpy openpyxl machine learning data science data analysis rohit kosamkar EDAExcelReport",
    python_requires='>=3.6',
    install_requires=[
        "pandas",  
        "openpyxl",
        "numpy",
        "scikit-learn",
        "datetime"
    ],
)