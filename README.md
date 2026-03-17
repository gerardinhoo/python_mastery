# Python Mastery

A collection of Python projects demonstrating API development, automation, CLI tooling, and scripting.

## Project Structure

```
python_mastery/
├── api/                   # FastAPI web application
│   ├── __init__.py
│   ├── app.py             # API routes and application entry point
│   └── models.py          # Pydantic data models
├── scripts/               # Standalone utility scripts
│   ├── api_fetcher.py     # GitHub API client
│   ├── automation.py      # Project directory inspector & shell runner
│   ├── devops_tool.py     # CLI system checker
│   └── premier_league.py  # Premier League standings display
├── .gitignore
├── README.md
└── requirements.txt
```

## Setup

```bash
# Create and activate a virtual environment
python3 -m venv venv
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt
```

## Usage

### FastAPI Application

Run the API server:

```bash
uvicorn api.app:app --reload
```

Available endpoints:

- `GET /` — Welcome message
- `GET /health` — Health check
- `GET /system` — System information
- `POST /users` — Create a user (JSON body: `name`, `role`, `hobby`)
- `GET /users` — List all users
- `GET /users/{name}` — Get a user by name

### Scripts

**GitHub API Fetcher** — Fetch public GitHub user info:

```bash
python -m scripts.api_fetcher
```

**Automation Script** — Inspect the project directory and run common shell checks:

```bash
python -m scripts.automation
```

**DevOps Tool** — CLI to check installed dev tools and system info:

```bash
python -m scripts.devops_tool --python --git --system
```

**Premier League Standings** — Display Premier League 2025-2026 results:

```bash
python -m scripts.premier_league
```

## Tech Stack

- Python 3.14
- FastAPI
- Pydantic
- Requests
- Uvicorn
