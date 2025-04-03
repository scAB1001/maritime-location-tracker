# Maritime Tracker & Mini Search Engine

---

## 🎯 Project Goals

- Develop a headless Django REST API for tracking maritime vessels, leveraging asynchronous data ingestion.
- Demonstrate geospatial capabilities using PostgreSQL + PostGIS for ship location data.
- Provide advanced text and geospatial search with Elasticsearch.
- Showcase cloud deployment on Heroku using Celery/Redis for background tasks.
- Build a separate JavaScript front end (React, Vue, or Angular) to consume and visualize the API data.

### Supported Examples

- **Real-time Ship Updates**: Ingest AIS (Automatic Identification System) data periodically to track vessel locations.
- **Search & Filter**: Search ships by name, location, or cargo type using Elasticsearch’s advanced querying.
- **Geospatial Queries**: Find ships within a certain radius of a port or bounding box, powered by PostGIS.
- **Analytics**: Potentially provide a summary of vessel types, busiest ports, etc.

### Architecture Overview

```plaintext
                         +------------------+
                         |  JavaScript      |
                         |  Front End (React,
                         |  Vue, or Angular)|
                         +--------^---------+
                                  |
                                  | (API Calls)
                                  |
+---------------------------------v-------------------------------+
|                 Django REST API (Backend)                       |
|                                                                 |
|  +--------------------+    +-------------------------+           |
|  |  Models (Ships,    |    |  Celery (Scheduler)     |           |
|  |  Ports, etc.)      |    |  + Redis (Message       |           |
|  +--------------------+    |    Broker)              |           |
|         |                   +----------^-------------+           |
|         | (ORM)                        |                         |
|         v                              | (tasks)                 |
|  PostgreSQL (with PostGIS)  <---->  Elasticsearch                |
|  (geospatial storage)                (advanced text/geo search)  |
+------------------------------------------------------------------+

                     Hosted on Heroku (Containers / Dynos)
```

1. Front End calls REST endpoints on your Django backend.  
2. Django uses PostgreSQL (with PostGIS) to store maritime data (ship positions, port info, etc.).  
3. Celery workers (with Redis as the broker) run asynchronous tasks for fetching AIS data, indexing records in Elasticsearch, etc.  
4. Elasticsearch provides advanced text searching and geospatial queries.  
5. Everything runs on Heroku via multiple dynos (web dyno for Django, worker dyno for Celery, possibly a separate add-on or external service for Elasticsearch and Redis).

### Intelligent Design Goals

- ✅Headlessly serve data through a Django REST API  
- ✅Store and handle geospatial data in PostgreSQL  
- ✅Use Elasticsearch for advanced search  
- ✅Rely on Celery + Redis for asynchronous tasks  
- ✅Deploy to Heroku.

---

---

## 📁 Project Structure

Below is an example directory layout for a Poetry-based Django project with a separate “maritime” app, plus Celery tasks:

```plaintext
maritime-tracker/
├─ .gitignore
├─ README.md
├─ pyproject.toml
├─ poetry.lock
├─ core/
│  ├─ __init__.py
│  ├─ asgi.py
│  ├─ settings.py
│  ├─ urls.py
│  └─ wsgi.py
├─ maritime/
│  ├─ __init__.py
│  ├─ admin.py
│  ├─ apps.py
│  ├─ models.py
│  ├─ tasks.py
│  ├─ views.py
│  └─ ...
└─ ...
```

---

## 🚀 Quick Start

### Poetry Setup

```powershell
# From maritime-tracker/ (root dir)
poetry self add poetry-plugin-shell   # (Optional: adds the 'shell' plugin for convenience)
poetry lock --no-cache --regenerate   # Create or refresh the lock file
poetry self show plugins

poetry env use python3.10
poetry install                        # Install dependencies from pyproject.toml
```

### Django setup

```powershell
# From maritime-tracker/ (root dir)
django-admin startproject core .
python manage.py runserver            # (first time only)
python manage.py showmigrations
```

### Running the program

```powershell
# Typical local run
python manage.py migrate
python manage.py runserver
```

Output:

```powershell
[INFO] Starting development server at http://127.0.0.1:8000/
```

---

## 🧪 Poetry Dependencies

Inside `pyproject.toml`, for example:

```toml
[tool.poetry]
name = "maritime-tracker"
version = "0.1.0"
description = "Django-based maritime tracking app"
authors = ["Your Name <you@example.com>"]

[tool.poetry.dependencies]
python = "^3.10"
django = "^4.2"
djangorestframework = "^3.14"
celery = "^5.2"
redis = "^4.5"
elasticsearch-dsl = "^7.4"  # optional if using Elasticsearch

[tool.poetry.dev-dependencies]
pytest = "^7.0"
```

---

## Tech Stack

- **Django + DRF** – Backend REST API
- **PostgreSQL** – Relational database (with PostGIS for geospatial)
- **Heroku** – Cloud hosting for deployment
- **Celery/Redis** – For background tasks, scheduling data ingestion
- **Elasticsearch** – Advanced text/geo queries
- **Poetry** – Python dependency management
- **VS Code** – Development and debugging

---

## Future Directions

- **Docker**: Containerize the application for consistent deployments.  
- **Geospatial Enhancements**: Leverage PostGIS for complex location queries (e.g., nearest port calculations).  
- **CICD Pipelines**: Automate testing, linting, and deployment with GitHub Actions or a similar service.  
- **Additional Data Sources**: Integrate multiple AIS providers, or add real-time event tracking.  
- **Front-End Visualizations**: Use interactive map frameworks (Leaflet, Mapbox) for real-time ship location plotting.

---

## ✅ Last Verified

> **Windows 11 + Python 3.10 + Poetry 1.8.2**

---

## Git Setup

### Ignore Unnecessary Files

`.gitignore` at the root (maritime-tracker/):

```plaintext
__pycache__/
*.py[cod]
.vscode/
.env/
.venv/
poetry.lock
```

*(Note: You may want to commit `poetry.lock` if you want to ensure exact dependency versions across environments.)*

### First Commit

```powershell
git init
git remote add origin https://github.com/YOUR_USERNAME/YOUR_REPO.git
git remote -v
git checkout -b main
git add .
git commit -m "Initial commit: Maritime Tracker"
git push -u origin main
```
