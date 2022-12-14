# Analysis Prime Number Algorithms

[![License: MIT](https://img.shields.io/github/license/ILoveBacteria/analysis-prime-number-algorithms)](https://github.com/ILoveBacteria/analysis-prime-number-algorithms/blob/master/LICENSE)
[![Issues](https://img.shields.io/github/issues/ILoveBacteria/analysis-prime-number-algorithms)](https://github.com/ILoveBacteria/analysis-prime-number-algorithms/issues)
[![Forks](https://img.shields.io/github/forks/ILoveBacteria/analysis-prime-number-algorithms)](https://github.com/ILoveBacteria/analysis-prime-number-algorithms/network/members)
[![Stars](https://img.shields.io/github/stars/ILoveBacteria/analysis-prime-number-algorithms)]()
[![Watchers](https://img.shields.io/github/watchers/ILoveBacteria/analysis-prime-number-algorithms)]()
[![Last commit](https://img.shields.io/github/last-commit/ILoveBacteria/analysis-prime-number-algorithms)](https://github.com/ILoveBacteria/analysis-prime-number-algorithms/commits/master)

## Description

This is my project for the course "Data Structures" at Shahid Beheshti University. The project is about analyzing the performance of some prime number algorithms. Analysis is done by measuring the time of each algorithm. Creating graphs and tables is done by using the [matplotlib](https://matplotlib.org) library and generating a pdf file is done by using the [FPDF](https://pyfpdf.readthedocs.io/en/latest/) library.
 
## How To Test On Your Machine

### What You Need?

- Python 3.10
- JDK 11
- Pipenv

1. Clone the repository

```bash
git clone https://github.com/ILoveBacteria/analysis-prime-number-algorithms.git
```

2. Go to the project directory

3. Compile Java code then run the `Main` class

```bash
javac -d ./out ./src/*.java
java -cp ./out Main
```

4. Install python dependencies

```bash
pipenv sync
```

5. Run the python script

```bash
pipenv run python analysis.py
```

6. Open the generated pdf file in the `output` directory