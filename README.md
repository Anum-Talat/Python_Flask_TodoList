# Flask To-Do App with Docker and GitHub Actions CI

A simple Flask To-Do application with automated tests, Docker containerization, and a GitHub Actions continuous integration (CI) pipeline.

## Project Overview

This project demonstrates how to test and containerize a Python Flask application and automate validation using GitHub Actions.

The CI workflow runs when code is pushed to the repository or a pull request is opened. It installs the Python dependencies, runs the test suite, and builds a Docker image.

## Features

- Flask web application with SQLite database storage
- Add, update, delete, and clear To-Do items
- Automated tests using pytest
- Docker image built from a custom Dockerfile
- GitHub Actions workflow for continuous integration
- Docker build caching through appropriately ordered image layers

## Technology Stack

- Python 3.13
- Flask
- SQLite
- pytest
- Docker
- GitHub Actions
- Git and GitHub

## CI Pipeline

The workflow is defined in `.github/workflows/ci.yml`.

The pipeline performs these steps:

1. Checks out the repository.
2. Sets up Python 3.13 on an Ubuntu runner.
3. Installs dependencies from `requirements.txt`.
4. Runs the automated tests using `python -m pytest`.
5. Builds the Docker image using `docker build -t flask-todo:ci .`.

If a test fails, the workflow stops before the Docker image build step. A successful run confirms that the tests passed and the image build completed.

**Note:** The workflow builds the Docker image but does not publish it to Docker Hub or deploy the application.

## Run the Application Locally

### Prerequisites

- Python 3.13 or a compatible Python installation
- Git

### Setup

Clone the repository:

```bash
git clone YOUR_GITHUB_REPOSITORY_URL
cd YOUR_REPOSITORY_FOLDER
```

Create and activate a virtual environment.

On Windows:

```powershell
python -m venv .venv
.venv\Scripts\Activate.ps1
```

On macOS or Linux:

```bash
python3 -m venv .venv
source .venv/bin/activate
```

Install dependencies:

```bash
python -m pip install -r requirements.txt
```

Run the tests:

```bash
python -m pytest
```

Start the application:

```bash
python app.py
```

Open `http://localhost:8000` in your browser.

## Run with Docker

Build the image:

```bash
docker build -t flask-todo:ci .
```

Run a container:

```bash
docker run --name flask-todo-container -p 8000:8000 flask-todo:ci
```

Open `http://localhost:8000`.

To stop the container, press `Ctrl+C` if running in the foreground. If you started it in detached mode, use:

```bash
docker stop flask-todo-container
```

To remove a stopped container:

```bash
docker rm flask-todo-container
```

## Database Persistence

The application uses SQLite. Database persistence depends on where the database file is stored.

Data written to a container's writable layer can remain when that same container is stopped and restarted. Removing the container and creating a new one does not preserve that layer. A Docker volume or a suitable bind mount can be used when database persistence across container recreation is required.

## Project Structure

```text
.
├── .github/
│   └── workflows/
│       └── ci.yml
├── .dockerignore
├── Dockerfile
├── app.py
├── functions.py
├── requirements.txt
└── test_app.py
```

## What I Learned

- Testing Flask routes and database-related behavior with pytest
- Separating application dependencies from the host environment
- Building and running Docker containers
- Understanding Docker image layers and build caching
- Automating tests and Docker image builds with GitHub Actions
- Troubleshooting Git repository configuration and Python dependencies

## Future Improvements

- Add a Docker Compose configuration
- Introduce persistent database storage with a Docker volume
- Publish the Docker image to a container registry
- Explore deployment automation as a separate pipeline stage

## Scope of the CI Workflow

This project currently demonstrates continuous integration: automated testing and Docker image building. Container registry publishing and application deployment are not included in the current workflow.


https://github.com/user-attachments/assets/2c35bb24-fe3d-43b6-9c54-c2de26bc19be

