# Healthcare Management System

A small, test-only starter repository for a fictional healthcare company.

## Stack
- Python 3.10+
- FastAPI
- SQLite (local development)

## Features
- Patient records (dummy data only)
- Doctor directory
- Appointment creation and listing
- Basic health-check endpoint

## Quick start
```bash
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\\Scripts\\activate
pip install -r requirements.txt
uvicorn app.main:app --reload
```
Open http://127.0.0.1:8000/docs for the interactive API.

## Sample scripts
Example scripts for checking the API, listing patients, and creating fictional
demo records are in [`scripts/`](scripts/README.md). Start the API before
running them. Standalone in-memory examples for the project areas are in
[`src/`](src/README.md).

## Safety
This repository is a demonstration scaffold, not a production healthcare system.
Do not enter real patient information. It has no authentication, authorization,
audit logging, encryption, consent management, or regulatory compliance controls.
