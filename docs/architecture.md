# Architecture (demo)

The FastAPI application exposes REST endpoints and stores demo records in a local
SQLite database. `app/main.py` initializes the schema on startup.

This deliberately minimal layout is intended for experimentation only. A real
healthcare deployment needs a security and privacy architecture review before
handling any sensitive data.
