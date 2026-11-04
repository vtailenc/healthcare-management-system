"""Show fictional appointments and a simple patient-based lookup."""


SAMPLE_APPOINTMENTS = [
    {
        "id": 1,
        "patient_id": 1,
        "doctor_name": "Dr. Morgan Demo",
        "appointment_time": "2026-12-01T10:30:00",
        "reason": "Fictional routine visit",
    },
    {
        "id": 2,
        "patient_id": 2,
        "doctor_name": "Dr. Riley Example",
        "appointment_time": "2026-12-02T14:00:00",
        "reason": "Fictional follow-up",
    },
]


def appointments_for_patient(patient_id):
    return [
        appointment
        for appointment in SAMPLE_APPOINTMENTS
        if appointment["patient_id"] == patient_id
    ]


if __name__ == "__main__":
    for appointment in appointments_for_patient(1):
        print(appointment)
