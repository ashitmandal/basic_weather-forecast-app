# Python Weather Forecast Application

A simple Python-based Weather Forecast application with automated testing using Pytest and CI/CD using GitHub Actions.

## Features

- Python-based weather forecast application
- Automated testing with Pytest
- Isolated Python virtual environment
- GitHub Actions CI pipeline
- Ubuntu-based GitHub-hosted runner
- Automated test report generation

## Technology Stack

- Python 3.11
- Pytest
- Git
- GitHub Actions
- Ubuntu Linux

## Project Structure

```text
basic_weather-forecast-app/
│
├── src/
│   └── main.py
│
├── tests/
│   └── test_main.py
│
├── .github/
│   └── workflows/
│       └── python-tests.yml
│
├── requirements.txt
├── README.md
└── .gitignore
```

## Local Setup (Windows)

### 1. Clone the repository

```powershell
git clone <YOUR_GITHUB_REPOSITORY_URL>
cd basic_weather-forecast-app
```

### 2. Create virtual environment

```powershell
py -3.11 -m venv .venv
```

### 3. Activate virtual environment

```powershell
.\.venv\Scripts\Activate.ps1
```

### 4. Install dependencies

```powershell
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
```

### 5. Run the application

```powershell
python -m src.main
```

### 6. Run automated tests

```powershell
python -m pytest -v -s
```

## CI/CD Pipeline

This project uses GitHub Actions to automate testing.

### Workflow triggers

- Push to any branch
- Pull request targeting `main`
- Manual execution through GitHub Actions

### Pipeline execution

1. Checkout source code.
2. Configure Python 3.11