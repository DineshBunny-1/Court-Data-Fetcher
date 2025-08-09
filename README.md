Court-Data Fetcher & Mini-Dashboard
A lightweight web application to fetch and display public case data from Indian court websites. This project provides a simple, clean interface for users to query case information and view the latest details.

License: MIT License

► Tech Stack
Frontend: HTML, Tailwind CSS, Vanilla JavaScript

Backend: Python with Flask

Data Source: Direct API Integration (simulated)

Database: SQLite

Python Environment: venv

► Setup and Installation
Follow these steps to run the application locally.

1. Prerequisites
Python 3.8+

pip (Python package installer)

2. Clone the Repository
First, clone this repository to your local machine:

git clone <your-repository-url>
cd court-data-fetcher

3. Backend Setup
Set up a Python virtual environment and install the required dependencies.

# Create a virtual environment
python -m venv venv

# Activate the virtual environment
# On Windows:
venv\Scripts\activate
# On macOS/Linux:
source venv/bin/activate

# Install the required Python packages
pip install Flask flask-cors requests

4. Running the Application
A. Start the Backend Server:

In your terminal (with the virtual environment activated), run the Flask server:

python app.py

You should see output indicating the server is running on http://127.0.0.1:5000. A database file named query_log.db will be automatically created.

B. Open the Frontend:

Navigate to the project folder and open the index.html file in your web browser. You can now use the interface to search for cases.

To test, use a valid case number from the mock data, e.g., Case Number 12345 and Year 2024.

► API Integration
This project has been designed to connect to an external API that provides case details. The web scraping logic has been removed in favor of this more robust method.

Current Implementation (Simulation):

The app.py script currently simulates a call to an external API. It contains a mock database of cases to demonstrate the functionality of:

Receiving a request from the frontend.

Searching through a list of results returned by an API.

Finding the specific case that matches the user's query.

Mapping the API data to the format required by the frontend.

How to Use Your Real API:

To connect to your actual API, you will need to edit the fetch_data_from_external_api function in app.py:

Uncomment import requests.

Replace the placeholder API_KEY and API_URL with your actual credentials.

Uncomment the requests.get(...) block to make a live network request.

Adjust the field mapping (e.g., case['petitioner']) to match the field names in your API's JSON response.

► Project File Structure
index.html: The main frontend file containing the HTML structure and CSS.

script.js: Contains all the client-side JavaScript for handling user input, API calls, and displaying results.

app.py: The Flask backend server that handles API requests, calls the external case API, and logs data to the database.

query_log.db: The SQLite database file where all search queries and their corresponding results are stored.
