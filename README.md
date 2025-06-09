## SauceDemo Login Automation

This is a Web UI automation project built using **Python**, **Selenium WebDriver**, **pytest**, and **Page Object Model (POM)** design pattern to test the login functionality of [https://www.saucedemo.com](https://www.saucedemo.com).

---

## Project Overview

This project performs automated testing on the login page of SauceDemo. It covers:
- Valid login
- Invalid login
- Empty fields
- Partial inputs (only username / only password)
- Testing with different demo users like `locked_out_user`, `problem_user`, `performance_glitch_user`, etc.

Test structure follows the Page Object Model (POM) to keep code clean and reusable.

---

## How to Set Up the Environment

### Prerequisites:

- Python (3.7 or above) installed  
- Pycharm IDE installed
- Selenium installed
- Pytest framework installed
- Google Chrome browser
- ChromeDriver 

---

## How to Run the Test

- Open the terminal 
- Navigate to the project root directory where your tests_login.py file is
- Run all test files starting with test_ (like test_login.py) command using pytest

---

## How to Generate the HTML Report

- Make sure pytest-html is installed. If not, install it by using **pip install pytest-html** command in the terminal
- Run the tests with the HTML report by **pytest --html=reports/report.html** command
- After running, go to the **reports/ folder** and open **report.html** in a browser to view the test results

---

## Explanation of Each Dependency Used

- **selenium** - Automates browser actions like clicking, typing, and navigation
- **pytest** - Python testing framework used to write and run test cases
- **pytest-html** -	Generates a HTML report of the test results
- **webdriver-manager** - Automatically manages the browser driver
- **config.py** - Stores sensitive data like username, password, and base URL
- **locator.py** - Stores all element locators in one place to avoid repetition
- **Page Object Model (POM)** - Design pattern used to keep test code clean and reusable