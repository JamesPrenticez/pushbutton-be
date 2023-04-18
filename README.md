# Backing Sheets - Backend

## Installation Instructions
Azure Functions require Python 3.9.x

### Installation
Hint: You may need to run terminal as administrator

```sh
pip install virtualenv
```

```sh
virtualenv venv --python=python3.9.13
```
============================================
============================================
```sh
. venv/Scripts/activate
```
============================================
============================================

```sh
pip install -r requirements.txt
```

cd backend 
cp .env.example .env
update the .env file

cd frontend
npm i
npm run dev

## Testing

To run all the tests:

```sh
(venv) $ python -m pytest -v
```

To check the code coverage of the tests:

```sh
(venv) $ python -m pytest --cov-report term-missing --cov=project


```bash
frontend
backend
│   README.md
│   app.py
│
└───project
│   │   __init__.py
│   │   function.json
│   │
│   └───routes
│       │   __init__.py
│       │   home.py
│   
└───HandleApproach
    │   __init__.py
    │   function.json
```
