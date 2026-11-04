"""Check that the local demo API is responding."""
import json
import sys

from api_client import API_BASE_URL, ApiRequestError, request_json


def main():
    try:
        result = request_json("/health")
    except ApiRequestError as error:
        print(f"Health check failed: {error}", file=sys.stderr)
        return 1

    print(json.dumps(result, indent=2))
    if result.get("status") != "ok":
        print("The API responded but did not report a healthy status.", file=sys.stderr)
        return 1
    print(f"Healthy API at {API_BASE_URL}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
