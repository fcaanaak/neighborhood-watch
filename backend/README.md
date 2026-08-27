# Backend Setup

## Dependencies
- Python Version 3.12.3
- MySQL Server Version 9.7.2 

## First-time Setup

1. Create a new Python Virtual Environment in this folder (backend)
2. Activate the virtual environment
3. Run `pip install -r requirements.txt` to get dependencies installed in venv
4. Run the `dbsetup.sql` script from Notion to create the necessary user and DB.
5. Get the `.env` file from Notion and put it in the root folder (backend)

## Running the project
1. Activate The virtual environment (if not already active)
2. Run `python3 manage.py runserver`

