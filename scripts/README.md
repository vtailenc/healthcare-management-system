# Sample scripts

These scripts use Python's standard library and talk to the local FastAPI demo.
Start the app from the repository root first:

```bash
uvicorn app.main:app --reload
```

In another terminal, run scripts from the repository root:

```bash
python scripts/check_api_health.py
python scripts/create_demo_patient.py
python scripts/list_patients.py
python scripts/create_demo_appointment.py --patient-id 1 --appointment-time 2026-12-01T10:30:00
```

The appointment command requires an existing patient ID; use the ID printed by
`create_demo_patient.py` or listed by `list_patients.py`. To use a different API
address, set `API_BASE_URL` (for example, `http://localhost:8001`).

All records in these examples are fictional. This repository is a demo only:
never use real patient information.
