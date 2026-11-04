"""Print patient records returned by the local demo API."""
import json
import sys

from api_client import ApiRequestError, request_json


def main():
    try:
        patients = request_json("/patients")
    except ApiRequestError as error:
        print(f"Could not list patients: {error}", file=sys.stderr)
        return 1

    if not patients:
        print("No demo patients found. Create one with create_demo_patient.py.")
    else:
        print(json.dumps(patients, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
