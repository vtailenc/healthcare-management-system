"""Create one clearly fictional patient through the local demo API."""
import json
import sys

from api_client import ApiRequestError, request_json


def main():
    patient = {
        "name": "Taylor Demo",
        "date_of_birth": "1990-01-01",
        "email": "taylor@example.test",
    }
    try:
        created = request_json("/patients", method="POST", payload=patient)
    except ApiRequestError as error:
        print(f"Could not create demo patient: {error}", file=sys.stderr)
        return 1

    print(json.dumps(created, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
