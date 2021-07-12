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

Running Tests
-------------

To run tests from the example project root directory, run the following commands:
* `pytest`
* `coverage run -m pytest`
* `python -m coverage xml`

Configure your own sonar-project.properties (root of the repository)
-------------
Set sonar.projectKey, sonar.projectName, and sonar.login parameters.
For instance Group-00


    # Required metadata
    sonar.projectKey=Group-01
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
