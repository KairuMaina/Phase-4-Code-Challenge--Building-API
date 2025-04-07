# Superheroes API

Welcome to the Superheroes API! This project is designed to manage superheroes, their powers, and the relationships between them. With this API, you can:

- View a list of superheroes and their associated powers.
- Access specific superheroes or powers by their IDs.
- Update power descriptions.
- Add new hero-power associations.

## Table of Contents

1. [Requirements](#requirements)
2. [Setup](#setup)
3. [Database Initialization](#database-initialization)
4. [Running the App](#running-the-app)
5. [API Endpoints](#api-endpoints)
6. [Testing](#testing)
7. [Contributing](#contributing)
8. [License](#license)

## Requirements

To get started with the project, you'll need the following:

- Python 3.x
- Flask
- Flask-SQLAlchemy
- Flask-Migrate
- Alembic
- SQLite (or another database of your choice)

## Setup

### 1. Clone the repository

```bash
git clone https://github.com/yourusername/superheroes-api.git
cd superheroes-api

2. Install dependencies
Set up a virtual environment and install the necessary dependencies:

bash
Copy
Edit
python3 -m venv venv
source venv/bin/activate  # On Windows, use venv\Scripts\activate
pip install -r requirements.txt
3. Create a .env file (optional for configuration)
bash
Copy
Edit
# .env file
FLASK_APP=app.py
FLASK_ENV=development
DATABASE_URL=sqlite:///heroes.db  # Adjust the database URL if you're using something else
Database Initialization
Once you've installed the dependencies, it's time to initialize and migrate the database:

Initialize the migrations folder:

bash
Copy
Edit
flask db init
Create an initial migration:

bash
Copy
Edit
flask db migrate -m "Initial migration"
Apply the migration:

bash
Copy
Edit
flask db upgrade
(Optional) Seed the database with sample data:

bash
Copy
Edit
python seed.py
Running the App
To run the application locally, execute the following:

bash
Copy
Edit
flask run --port 5555
This starts the Flask development server on http://127.0.0.1:5555.

API Endpoints
1. GET /heroes
Retrieve a list of all superheroes.

Example request:

bash
Copy
Edit
curl -X GET http://127.0.0.1:5555/heroes
Response:

json
Copy
Edit
[
  {
    "id": 1,
    "name": "Kamala Khan",
    "super_name": "Ms. Marvel"
  },
  {
    "id": 2,
    "name": "Doreen Green",
    "super_name": "Squirrel Girl"
  },
  ...
]
2. GET /heroes/:id
Retrieve details of a specific superhero, including their powers.

Example request:

bash
Copy
Edit
curl -X GET http://127.0.0.1:5555/heroes/1
Response:

json
Copy
Edit
{
  "id": 1,
  "name": "Kamala Khan",
  "super_name": "Ms. Marvel",
  "powers": [
    {
      "id": 1,
      "name": "super strength",
      "description": "gives the wielder super-human strength"
    },
    {
      "id": 2,
      "name": "flight",
      "description": "gives the wielder the ability to fly through the skies at supersonic speed"
    }
  ]
}
3. GET /powers
Retrieve a list of all available powers.

Example request:

bash
Copy
Edit
curl -X GET http://127.0.0.1:5555/powers
Response:

json
Copy
Edit
[
  {
    "id": 1,
    "name": "super strength",
    "description": "gives the wielder super-human strength"
  },
  {
    "id": 2,
    "name": "flight",
    "description": "gives the wielder the ability to fly through the skies at supersonic speed"
  }
]
4. GET /powers/:id
Retrieve details of a specific power.

Example request:

bash
Copy
Edit
curl -X GET http://127.0.0.1:5000/powers/1
Response:

json
Copy
Edit
{
  "id": 1,
  "name": "super strength",
  "description": "gives the wielder super-human strength"
}
5. PATCH /powers/:id
Update the description of a specific power.

Example request:

bash
Copy
Edit
curl -X PATCH http://127.0.0.1:5000/powers/1 -d '{"description": "enhances the user's strength to super-human levels"}' -H "Content-Type: application/json"
Response:

json
Copy
Edit
{
  "id": 1,
  "name": "super strength",
  "description": "enhances the user's strength to super-human levels"
}
6. POST /hero_powers
Add a new power association to a hero.

Example request:

bash
Copy
Edit
curl -X POST http://127.0.0.1:5000/hero_powers -d '{"hero_id": 1, "power_id": 1, "strength": "strong"}' -H "Content-Type: application/json"
Response:

json
Copy
Edit
{
  "id": 1,
  "hero_id": 1,
  "power_id": 1,
  "strength": "strong"
}
Testing
You can use curl to test the API endpoints as shown above. The API responds with JSON data for each request.

Contributing
Feel free to fork this repository and submit pull requests if you find bugs or want to enhance the functionality. Just ensure all tests are passing before submitting.

License
This project is open-source and available under the MIT License