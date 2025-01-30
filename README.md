# Automated Crawling and Testing for an E-Commerce Website

This project automates the process of **crawling** a sample e-commerce website (e.g., Amazon India) and **testing** basic functionalities. It **extracts product information** (name, price, rating, URL), **validates** the presence of core elements on the product page (e.g., “Add to Cart” button, product details, and image gallery), and **stores** the results in a CSV file. Test results are logged for further analysis.

---

## Table of Contents

- [Project Overview](#project-overview)
- [Features](#features)
- [Project Structure](#project-structure)
- [Prerequisites](#prerequisites)
- [Installation & Setup](#installation--setup)
- [Usage](#usage)
- [Configuration](#configuration)
- [Parallel Testing (Bonus)](#parallel-testing-bonus)
- [Troubleshooting](#troubleshooting)
- [Assumptions](#assumptions)
- [License](#license)

---

## Project Overview

- **Crawl** e-commerce website pages with Selenium.
- **Extract** product data from search results (name, price, rating, URL).
- **Test** presence of key page elements such as “Add to Cart.”
- **Log** results and store product data in a CSV file.
- **Bonus**: Demonstrate pagination crawling, Selenium Grid for parallel testing, and simple responsiveness checks.

---

## Features

1. **Automated Search**: Searches for a given keyword (e.g., “laptop”).  
2. **Product Extraction**: Collects product details from multiple pages.  
3. **CSV Export**: Stores extracted data in `products.csv`.  
4. **Functional Testing**: Verifies product-page elements using Selenium.  
5. **Logging**: Records pass/fail test results in `test_log.log`.  
6. **Parallel Testing** (bonus): Demonstrates running tests via Selenium Grid.  
7. **Responsive Testing** (bonus): Simulates different screen sizes.

---

## Project Structure


**Key Files**:

- **`main.py`**: Entry point to run the entire suite via `pytest.main()`.
- **`config.py`**: Contains global settings like `BASE_URL`, search keywords, file paths, etc.
- **`tests/`**: All test files using **pytest**:
  - **`conftest.py`**: Holds the **init_driver** fixture for Selenium WebDriver setup.
  - **`test_search.py`**: Tests search functionality and product extraction.
  - **`test_product_page.py`**: Validates product page elements.
  - **`parallel_tests/test_parallel.py`**: Demonstrates Selenium Grid usage (bonus).
- **`pages/`**: Page Object Model classes:
  - **`base_page.py`**: Common methods (e.g., waits, element finders).
  - **`homepage.py`**, **`search_results_page.py`**, **`product_page.py`**.
- **`utils/`**: Utility modules:
  - **`logger.py`**: Logging setup.
  - **`csv_writer.py`**: Writing extracted data to CSV.
- **`output/`**: Stores logs (`test_log.log`) and product data (`products.csv`).

---

## Prerequisites

- Python 3.7+ (recommended Python 3.9+ or later).
- Google Chrome or another browser supported by Selenium.
- [ChromeDriver](https://chromedriver.chromium.org/) installed (or specify the path in `conftest.py` if needed).

---

## Installation & Setup

1. **Clone the repository**:
   ```bash
   git clone https://github.com/shivaniyadav06/AutomatedCrawlingProject

cd AutomatedCrawlingProject
python -m venv myenv
source myenv/bin/activate
pip install -r requirements.txt
pytest --version
pytest --maxfail=1 --disable-warnings -v

