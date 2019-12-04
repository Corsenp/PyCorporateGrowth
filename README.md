# PyCorporateGrowth

PyCorporateGrowth is a school project (Assignment 9), the goal of this project is to scrape data from a corporation on yahoo finance website  
and to display two graphs, the revenue growth of the corporation and its profits.  
The script will ask the user for the tick of the corporation (Example : "F" for Ford, "TSLA" for Tesla, "GOOG" for Alphabet etc...)

## Installation

Python 3 is required in order to run this program  
Pipenv is required in order to run this program

### OSX

```bash
brew install python3
```

```bash
brew install pipenv
```

## Usage

In order to install the dependencies run :

```bash
pipenv install
```

Finally we will need the ChromeDriver in order to run this project
you can follow the [Installation steps here](https://sites.google.com/a/chromium.org/chromedriver/getting-started)

Then to run the project use the following command:

```bash
pipenv run python3.6 pycorporategrowth.py
```

### Pipenv Shell

If you want to run the script with the pipenv shell, just use :

```bash
pipenv shell
```

Then:

```bash
python pycorporategrowth.py
```

If you have any trouble with pipenv use the help flag:

```bash
pipenv --help
```

## License

[GNU General Public License v3.0](https://www.gnu.org/licenses/gpl-3.0.en.html)