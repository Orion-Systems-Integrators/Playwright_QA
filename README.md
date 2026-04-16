# Playwright Python Automation Framework

This project provides a clean Playwright automation framework in Python using pytest and the pytest-playwright plugin.

## Folder structure

```text
config/
pages/
tests/
utils/
conftest.py
pytest.ini
requirements.txt
```

## What is included

- Organized folder structure for automation assets
- Page Object Model classes for login, dashboard, and product pages
- Shared pytest fixtures in `conftest.py`
- Environment-driven settings via `.env`
- Example smoke and regression tests

## Setup

1. Create a virtual environment.
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Install Playwright browsers:
   ```bash
   python -m playwright install
   ```
4. Copy `.env.example` to `.env` and update values.
5. Replace the sample locators in the page classes with selectors from your application.

## Run tests

```bash
pytest
```

For Scenario 1 & Scenario 2 
Run only smoke tests:

```bash
pytest -m smoke
```

For Scenario 3 
Run only regression tests:

```bash
pytest -m regression  

```

## Notes

- Python Playwright projects typically use `pytest` as the test runner rather than the Node.js `@playwright/test` runner.
- The provided tests are intentionally skipped until the base URL and selectors are updated for the real application.
