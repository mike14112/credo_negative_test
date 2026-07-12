# MyCredo Business Internet Banking Automation Tests

Automation tests for negative authorization scenarios of MyCredo Business Internet Banking.

## Application Version

The provided task link pointed to the beta version of MyCredo Business Internet Banking.

During implementation, it was found that the beta version supports only the Georgian language and does not include Megrelian and Svan language support. The required support for all three languages (Georgian, Megrelian, and Svan) is available only on the legacy authorization page.

Therefore, the automated tests were implemented against the legacy version:

https://old.mycredo.ge/landing/main/auth

## Tech Stack

- Python
- Selenium WebDriver
- Pytest
- Allure Report
- WebDriver Manager
- Faker
- Page Object Model (POM)

## Project Structure

```
├── config/          # Configuration files
├── core/            # Driver setup
├── elements/        # Web element classes
├── components/      # Reusable components
├── pages/           # Page Objects
├── tests/           # Test cases
├── utils/           # Utilities
├── conftest.py
├── requirements.txt
└── README.md
```

## Installation

Install dependencies:

```
pip install -r requirements.txt
```

## Run Tests

Run tests:

```
pytest 
```

Run with Allure:

```
pytest --alluredir=allure-results
```

Open Allure report:

```
allure serve allure-results
```

## Test Coverage

Implemented negative authorization scenarios for:

- Georgian language
- Megrelian language
- Svanuri language
