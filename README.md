# CI-Pipeline-with-Docker

This is a containerized Django REST API project with a working CI pipeline powered by GitHub Actions. It was built to fulfill requirements similar to Assignment #122, with Docker image creation and automated testing.

---

## 📁 Project Structure

- `ci_cd_app/` – Main Django app with an `Animal` model
- `Dockerfile` – Docker configuration to build the image
- `.github/workflows/ci.yml` – GitHub Actions workflow for CI
- `requirements.txt` – Python dependencies

---

## 🚀 Tech Stack

- Python 3.11  
- Django 5.2  
- Django REST Framework  
- Docker  
- GitHub Actions  

---

## 🐳 Using Docker

### Build the Docker image:

docker build -t ci_cd_app .
Run tests inside the container:

docker run --rm ci_cd_app
✅ GitHub Actions – CI Pipeline
The GitHub Actions workflow automatically:

Builds the Docker image

Runs Django tests (python manage.py test)

Workflow File:
Located at: .github/workflows/ci.yml

🔐 Environment Variables (GitHub Secrets)
The following environment variables are stored as GitHub Secrets:

SECRET_KEY – Your Django secret key

DEBUG – Set to False in CI

They are injected into the environment during workflow execution.

📊 API Overview
This project includes a simple Animal API (CRUD operations):

GET /api/animals/

POST /api/animals/

PUT /api/animals/<id>/

DELETE /api/animals/<id>/

🧪 Running Tests Locally
python manage.py test
