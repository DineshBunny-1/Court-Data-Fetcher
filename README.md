# Court-Data Fetcher & Mini-Dashboard

## Project Overview
This project is a small web application that allows users to query Indian court case details by selecting the **Case Type**, **Case Number**, and **Filing Year**. It fetches and displays case metadata such as parties’ names, hearing dates, and links to the latest orders or judgments in PDF format from a selected court's public website. Users can view details and download PDFs directly from the app.

---

## Court Chosen

At present, this project **does not integrate with any real court website**. Instead, it uses static/sample data to simulate the case fetching functionality.

Future versions may implement scraping from the Delhi High Court ([https://delhihighcourt.nic.in/](https://delhihighcourt.nic.in/)) or a District Court eCourts portal ([https://districts.ecourts.gov.in/](https://districts.ecourts.gov.in/)).

The project structure and UI are designed to support real-time integration when court data scraping is implemented.


---

## Features
- **User Interface:** Simple web form with dropdowns and inputs for:
  - Case Type
  - Case Number
  - Filing Year
- **Backend:**
  - Programmatic scraping of the court website upon form submission.
  - Parsing of:
    - Parties’ names
    - Filing and next-hearing dates
    - Links to order/judgment PDFs (most recent shown by default)
- **Storage:**
  - Logs all queries and raw HTML responses in SQLite database.
- **Display:**
  - Clean rendering of parsed case details.
  - Downloadable PDF links for latest orders.
- **Error Handling:**
  - User-friendly messages for invalid input or site downtime.

---

## Technology Stack
- **Backend:** Python with Flask (or your preferred stack)
- **Scraping:** Requests + BeautifulSoup or Selenium for dynamic content
- **Database:** SQLite for lightweight local storage
- **Frontend:** HTML, CSS, and JavaScript (vanilla or lightweight framework)
- **Others:** Use of headless browser (Selenium or Playwright) to bypass view-state or handle dynamic tokens

---

## Setup Instructions

### Prerequisites
- Python 3.8+
- pip package manager
- SQLite (usually bundled with Python)
- Chrome or Firefox browser (for Selenium/Playwright headless browsing)

### Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/court-data-fetcher.git
   cd court-data-fetcher
Create and activate a virtual environment:

bash
Copy
Edit
python -m venv venv
source venv/bin/activate      # On Windows: venv\Scripts\activate
Install dependencies:

bash
Copy
Edit
pip install -r requirements.txt
Configure environment variables (optional):
Create a .env file with variables like:

ini
Copy
Edit
FLASK_ENV=development
DATABASE_URL=sqlite:///court_data.db
Run the Flask app:

bash
Copy
Edit
flask run
Open your browser at http://localhost:5000

CAPTCHA and View-State Handling Strategy
The Delhi High Court site uses dynamic tokens in the request parameters to prevent CSRF attacks.

To bypass these:

The scraper first performs a GET request to load the initial page and parse hidden tokens (viewstate, eventvalidation, etc.)

These tokens are then included in the POST request for submitting the query.

CAPTCHA:

Currently, the Delhi High Court site does not enforce CAPTCHA for basic case status queries.

If CAPTCHA is introduced, a manual input field is displayed on the UI for users to enter the CAPTCHA text.

Alternatively, integration with a remote CAPTCHA-solving service (e.g., 2Captcha) can be added.

All token extraction and submission logic is documented in the code comments.

Database Schema
Table: queries

id INTEGER PRIMARY KEY AUTOINCREMENT

case_type TEXT

case_number TEXT

filing_year TEXT

timestamp DATETIME DEFAULT CURRENT_TIMESTAMP

raw_response TEXT (stores raw HTML or JSON response for debugging)

Error Handling
If case number is invalid or no data is found, a user-friendly message is shown.

If court website is down or unreachable, the app displays an informative error and suggests retrying later.

Optional Extras
Dockerfile included for containerized deployment.

Pagination support for multiple orders/judgments.

Basic unit tests for scraper and API endpoints.

GitHub Actions CI workflow for automatic testing.

License
This project is licensed under the MIT License. See the LICENSE file for details.

Demo
Please refer to the demo.mp4 file in the repo root for a ≤5-minute screen capture showing the full end-to-end flow.

Contact
For questions or contributions, open an issue or contact:

Your Name — your.email@example.com
GitHub: https://github.com/yourusername
