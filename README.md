# URL Shortener

A simple web application to shorten URLs and store them with a custom name for easy identification. Built with Flask and SQLite.

## Features

- Shorten any URL and give it a custom name.
- Prevents shortening the same URL multiple times.
- View all shortened URLs.
- Redirect to the original URL using the shortened URL.

## Getting Started

### Prerequisites

- Python 3.x
- Flask
- SQLite

### Installation

1. Clone the repository:
    ```sh
    git clone https://github.com/umer-jahangier/URL-Shortner.git
    cd url-shortener
    ```

2. Create and activate a virtual environment (optional but recommended):
    ```sh
    python -m venv venv
    source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
    ```

3. Install the required packages:
    ```sh
    pip install -r requirements.txt
    ```

4. Initialize the database:
    ```sh
    python -c "from Url_Shortner import init_db; init_db()"
    ```

5. Run the application:
    ```sh
    python Url_Shortner.py
    ```

6. Open your browser and navigate to `http://127.0.0.1:5000`.

## Project Structure

- `Url_Shortner.py`: Main application file containing the Flask routes and logic.
- `urls.db`: SQLite database file to store URLs.
- `templates/`: Directory containing HTML templates.
  - `index.html`: Main page template.
  - `list_urls.html`: Template to list all shortened URLs.
  - `shortened.html`: Template to display the shortened URL.
- `static/`: Directory containing static files (CSS).
  - `styles.css`: CSS file for styling the HTML pages.
- `requirements.txt`: List of required Python packages.

## Usage

### Shorten a URL

1. Enter a name and the original URL in the form on the main page.
2. Click "Shorten" to generate a shortened URL.
3. If the URL has already been shortened, an error message will be displayed with the existing name.

### View All Shortened URLs

1. Click the "View All Shortened URLs" button on the main page.
2. A table listing all shortened URLs along with their names and original URLs will be displayed.
3. Clicking on a shortened URL or an original URL will open it in a new tab.

### Redirect to Original URL

1. Enter the shortened URL in the browser's address bar.
2. You will be redirected to the original URL.

