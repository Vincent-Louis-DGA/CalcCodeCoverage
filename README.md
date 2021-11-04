Python Testing Example: unittest
================================
This is the example project for
[Python Testing 101: doctest](https://automationpanda.com/2017/03/06/python-testing-101-doctest/),
part of the
[Python Testing 101 series](https://automationpanda.com/2017/03/06/python-testing-101-introduction/)
from [Automation Panda](https://automationpanda.com/).
It will work for Python 2 and 3.

Project Structure
-----------------
This project has two packages:
* `com.automationpanda.example` contains `calc.py`, which has a basic Calculator class.
* `com.automationpanda.tests` contains `test_calc.py`, which contains `unittest` test cases.


TP N°1 Technical Debt (part 1)
-----------------


Download or Clone this repo : 'git clone https://github.com/Vincent-Louis-DGA/CalcCodeCoverage/



Configure your own sonar-project.properties (root of the repository)
-------------
Chose your Group and set the column "Name" of the googlesheet "Identifiers-TP" https://docs.google.com/spreadsheets/d/1p7gKri37ioQVs517oSxreZ9eFs0bAkwmTSx-rDYbqLI/edit?usp=sharing


Set these parameters in your own sonar-project.properties : sonar.projectKey, sonar.projectName, and sonar.login.


For instance Group-00


    # Required metadata
    sonar.projectKey=Group-00
    sonar.projectName=Projet VincentLouis-PerrineLabarthe 
    sonar.projectVersion=1

    # Language
    #sonar.language=python

    # Comma-separated paths to directories with sources (required)
    sonar.sources=.
    sonar.python.coverage.reportPaths=test/coverage.xml

    # Encoding of the source files
    sonar.sourceEncoding=UTF-8

    sonar.host.url=https://lintycloud.linty-services.com
    sonar.login=ac3bbaa6cexxxxxxxxxxxxxee9a3164cec


Running SonarScanner
-------------
To run sonarscanner, download it https://binaries.sonarsource.com/Distribution/sonar-scanner-cli/sonar-scanner-cli-4.6.2.2472.zip, unzip the file and then execute the following command (in a terminal drag and drop sonar-scanner script) at the root of the repository, let's say on sonar-project.properties
* `/Users/path/to/sonar-scanner-yourVersion-yourOS/bin/sonar-scanner`

Results analysis
-------------
Find your project at this url https://lintycloud.linty-services.com

Provide a synthesis of bugs, code smell or vulnerabilities (Overall Code)



TP N°1 Technical Debt (part 2)
-----------------

Add python files in your repo

Re-run sonarscanner

Provide a synthesis of bugs, code smell or vulnerabilities (New Code)

Define a remediation startegy



TP N°2 Code Coverage
-----------------


Running Tests
-------------

To run tests, run the following commands from the example project root directory after having downloaded CalcCodeCoverage source code:
* `pytest`
* `coverage run -m pytest`
* `python -m coverage xml`


Running SonarScanner
-------------
To run sonarscanner, download it https://binaries.sonarsource.com/Distribution/sonar-scanner-cli/sonar-scanner-cli-4.6.2.2472.zip, unzip the file and then execute the following command (in a terminal drag and drop sonar-scanner script) at the root of the repository, let's say on sonar-project.properties
* `/Users/path/to/sonar-scanner-yourVersion-yourOS/bin/sonar-scanner`


Results analysis
-------------
Provide a synthesis of code coverage

Why the coverage of com/automationpanda/example/calc.py is not fully achieved?

Could you provide a solution to reach 100% of line coverage?


