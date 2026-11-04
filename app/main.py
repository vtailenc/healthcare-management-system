from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field
from typing import Optional
import sqlite3
import os

DB_PATH = os.getenv("DATABASE_PATH", "healthcare_demo.db")
app = FastAPI(title=os.getenv("APP_NAME", "Demo Healthcare API"), version="0.1.0")


def connect():
    return sqlite3.connect(DB_PATH)


def initialize():
    with connect() as db:
        db.execute("""
            CREATE TABLE IF NOT EXISTS patients (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                date_of_birth TEXT,
                email TEXT
            )
        """)
        db.execute("""
            CREATE TABLE IF NOT EXISTS appointments (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                patient_id INTEGER NOT NULL,
                doctor_name TEXT NOT NULL,
                appointment_time TEXT NOT NULL,
                reason TEXT,
                FOREIGN KEY(patient_id) REFERENCES patients(id)
            )
        """)


initialize()


class PatientCreate(BaseModel):
    name: str = Field(min_length=1, max_length=120)
    date_of_birth: Optional[str] = None
    email: Optional[str] = None


class AppointmentCreate(BaseModel):
    patient_id: int
    doctor_name: str = Field(min_length=1, max_length=120)
    appointment_time: str
    reason: Optional[str] = None


@app.get("/health")
def health():
    return {"status": "ok", "service": "demo-healthcare-api"}


@app.post("/patients", status_code=201)
def create_patient(payload: PatientCreate):
    with connect() as db:
        cursor = db.execute(
            "INSERT INTO patients (name, date_of_birth, email) VALUES (?, ?, ?)",
            (payload.name, payload.date_of_birth, payload.email),
        )
        patient_id = cursor.lastrowid
    return {"id": patient_id, **payload.model_dump()}


@app.get("/patients")
def list_patients():
    with connect() as db:
        rows = db.execute(
            "SELECT id, name, date_of_birth, email FROM patients ORDER BY id"
        ).fetchall()
    return [
        {"id": r[0], "name": r[1], "date_of_birth": r[2], "email": r[3]}
        for r in rows
    ]


@app.post("/appointments", status_code=201)
def create_appointment(payload: AppointmentCreate):
    with connect() as db:
        patient = db.execute(
            "SELECT id FROM patients WHERE id = ?", (payload.patient_id,)
        ).fetchone()
        if not patient:
            raise HTTPException(status_code=404, detail="Patient not found")
        cursor = db.execute(
            """INSERT INTO appointments
               (patient_id, doctor_name, appointment_time, reason)
               VALUES (?, ?, ?, ?)""",
            (payload.patient_id, payload.doctor_name,
             payload.appointment_time, payload.reason),
        )
        appointment_id = cursor.lastrowid
    return {"id": appointment_id, **payload.model_dump()}


@app.get("/appointments")
def list_appointments():
    with connect() as db:
        rows = db.execute(
            """SELECT id, patient_id, doctor_name, appointment_time, reason
               FROM appointments ORDER BY appointment_time"""
        ).fetchall()
    return [
        {"id": r[0], "patient_id": r[1], "doctor_name": r[2],
         "appointment_time": r[3], "reason": r[4]}
        for r in rows
    ]
