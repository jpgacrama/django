# Django Web Server

This is a Python Django web server project.

## Prerequisites

- Python 3.11 or higher
- Django 3.2.5 or higher

## Installation

1. Clone the repository:

   ```bash
   git clone git@github.com:jpgacrama/django.git
   ```

2. Change to the project directory:

   ```bash
   cd django
   ```

3. Create a virtual environment:

   ```bash
   conda create -n django python=3.11
   conda install -c anaconda django
   ```

4. Activate the virtual environment:

   - For Linux/macOS:

     ```bash
     conda activate django
     ```

5. Install the project dependencies:

   *TBD: requirements.txt will be created soon. When it is available, just type the command below*

   ```bash
   pip install -r requirements.txt
   ```

## Configuration

1. Create a `.env` file in the project root directory and configure any necessary environment variables, such as database credentials or secret keys.

2. Edit the `settings.py` file in the project's main directory and update the necessary settings like database connection, static files, etc.

## Database Setup

1. Run the migrations to create the database tables:

   ```bash
   python manage.py migrate
   ```

2. (Optional) Load initial data if available:

   ```bash
   python manage.py loaddata initial_data
   ```

## Run the Server

Start the Django development server:

```bash
python manage.py runserver
```

By default, the server will run at `http://127.0.0.1:8000/`.

## Usage

Access the web application by visiting `http://127.0.0.1:8000/` in your web browser.

## DB Migrations

* `python manage.py makemigrations reviews`
* `python manage.py migrate reviews`

## License

This project is licensed under the [MIT License](LICENSE).
