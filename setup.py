from setuptools import setup, find_packages

# List of contributors
contributors = [
    "Rohit Kosamkar <rohitkosamkar97@gmail.com>",
    "Viraj Pai",
    "KP"
    
]



with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name="EDAExcelReport",  
    version="0.1.6",  
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
        "Development Status :: 4 - Beta",
    ],
    keywords="EDA Excel exploratory data analysis report pandas numpy openpyxl machine learning data science data analysis EDAExcelReport profiling Visualization Excel report python EDA reort",
    python_requires='>=3.6',
    install_requires=[
        "pandas",  
        "openpyxl",
        "numpy",
        "scikit-learn",
        "datetime"
    ],

     metadata={
        "contributors": ", ".join(contributors)
    }
)