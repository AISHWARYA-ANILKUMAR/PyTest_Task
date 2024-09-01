#  Selenium Automation with Python (Pytest Framework)

This project contains automation scripts using Selenium with Python, organized with the Page Object Model (POM) and tested using the Pytest framework.

## Project Structure

      - pageObjects/: Contains Page Object Models (POMs) for different pages.
      - testCases/: Contains test cases organized by functionality.
      - env/: Virtual environment.
      - conftest.py: Contains configurations  for Pytest.
      - resources/: Contains resources needed for tests 
      - README.md: Instructions for setting up and running the project.

## Prerequisites

      - Python 3.10+
      - Chrome WebDriver 
      - Selenium, Pytest

## Installations

      - selenium
      - pytest
      - pytest-html

## Project Set Up

 1. Clone the repository :
    
          git clone <repository-url>

 2. Activate the virtual environment:
     
         env\Scripts\activate

 3. Install pytest, selenium, and optionally pytest-html for reports :

        pip install pytest selenium pytest-html

 4. To run all the test cases:
    
        pytest testCases
        or
        pytest

 5. To run individual test cases:

        pytest -v -s testCases/<test_case_file_name>.py

        e.g., pytest -v -s testCases/test_01_login.py

 6. To generate an HTML report:
 
        pytest --html=<report_name>.html
   
        e.g.,  pytest -rA --html="TestReport.html"








