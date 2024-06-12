# FileoperationPythonV3
File Upload Feature and Data Analysis

# Django CSV Upload and Analysis

This project is a Django application that allows users to upload CSV files, reads the CSV data using pandas, displays basic analysis, and generates histograms for data visualization.

## Features

- Upload CSV files
- Read and process CSV files using pandas
- Display basic statistical analysis of the CSV data
- Generate and display histograms for data visualization

## Technologies Used

- Python
- Django
- pandas
- matplotlib
- Bootstrap (for styling)

## Getting Started

### Prerequisites

- Python 3.x
- pip (Python package installer)
- virtualenv (recommended)

### Installation

1. **Clone the repository:**

    ```bash
    git clone https://github.com/yourusername/django-csv-upload.git
    cd django-csv-upload
    ```

2. **Create a virtual environment and activate it:**

    ```bash
    python3 -m venv env
    source env/bin/activate   # On Windows use `env\Scripts\activate`
    ```

3. **Install the required packages:**

   
    pip install -r requirements.txt
  

4. **Apply migrations:**

   
    python manage.py migrate
   

5. **Run the development server:**

   
    python manage.py runserver
   

6. **Visit the application in your browser:**

    Open `http://127.0.0.1:8000/fileupload` in your web browser.

## Usage

1. **Upload CSV File:**
    - Go to the home page.
    - Click on "Upload CSV" and select a CSV file from your computer.

2. **View Analysis:**
    - After uploading, By clicking files tab you will see all uploaded files you have to click on particular file button to show data of csv.

3. **View Histogram:**
    - click on show hist button to see Histogram and Data analysis (Mean,Mode,Standard deviation).



