"""Create an appointment for an existing demo patient."""
import argparse
import json
import sys

from api_client import ApiRequestError, request_json


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--patient-id", type=int, required=True)
    parser.add_argument(
        "--appointment-time",
        required=True,
        help="Appointment date/time as a string, e.g. 2026-12-01T10:30:00",
    )
    parser.add_argument("--doctor-name", default="Dr. Demo")
    parser.add_argument("--reason", default="Fictional demo appointment")
    args = parser.parse_args()

    appointment = {
        "patient_id": args.patient_id,
        "doctor_name": args.doctor_name,
        "appointment_time": args.appointment_time,
        "reason": args.reason,
    }
    try:
        created = request_json(
            "/appointments", method="POST", payload=appointment
        )
    except ApiRequestError as error:
        print(f"Could not create demo appointment: {error}", file=sys.stderr)
        return 1

    print(json.dumps(created, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
