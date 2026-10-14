import pytest
import tempfile
import os
import sqlite3

import app
import my_functions

@pytest.fixture
def client():
    og_database = my_functions.DATABASE
    with tempfile.TemporaryDirectory() as temp_dir:
        db_path = os.path.join(temp_dir, "test_database.db")

        my_functions.DATABASE = db_path
        app.app.config["TESTING"] = True

        try: 
            with app.app.test_client() as client:
                yield client
        finally:
            my_functions.DATABASE = og_database

        

def test_home_page(client):
    response = client.get("/")

    assert response.status_code == 200


def test_add(client):
    response = client.post("/add", data={"title": "Learn pytest"})

    assert response.status_code == 302

    conn = sqlite3.connect(my_functions.DATABASE)
    cursor = conn.cursor()
    cursor.execute("SELECT title FROM todo")
    rows= cursor.fetchall()
    conn.close()

    assert ("Learn pytest",) in rows


def test_update(client):
    # First create a todo
    client.post("/add", data={"title": "Learn pytest"})

    # Update todo with ID 1
    response = client.get("/update/1")
    assert response.status_code == 302

    # Check the Database
    conn = sqlite3.connect(my_functions.DATABASE)
    cursor = conn.cursor()
    cursor.execute("SELECT status FROM todo WHERE todo_id = 1")
    row = cursor.fetchone()
    conn.close()

    assert row[0] == 1


def test_delete(client):
    # Create a todo
    client.post("/add", data={"title": "Learn pytest"})

    # Delete the todo
    response = client.get("/delete/1")

    assert response.status_code == 302

    # Verify that the todo no longer exists
    conn = sqlite3.connect(my_functions.DATABASE)
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM todo WHERE todo_id = 1")
    row = cursor.fetchone()
    conn.close()

    assert row is None

def test_clear(client):
    # Create two todos
    client.post("/add", data={"title": "Learn pytest"})
    client.post("/add", data={"title": "Learn Github Actions"})

    # Clear all todos
    response = client.get("/clear")

    assert response.status_code == 302

    #verify that no todos remain
    conn = sqlite3.connect(my_functions.DATABASE)
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM todo")
    rows = cursor.fetchall()
    conn.close()

    assert rows == []
