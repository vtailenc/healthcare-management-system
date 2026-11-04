"""Small standard-library client shared by the API example scripts."""
import json
import os
from urllib.error import HTTPError, URLError
from urllib.request import Request, urlopen


API_BASE_URL = os.getenv("API_BASE_URL", "http://127.0.0.1:8000").rstrip("/")


class ApiRequestError(Exception):
    """Raised when the demo API cannot complete a request."""


def request_json(path, method="GET", payload=None):
    data = None
    headers = {}
    if payload is not None:
        data = json.dumps(payload).encode("utf-8")
        headers["Content-Type"] = "application/json"

    request = Request(
        f"{API_BASE_URL}{path}",
        data=data,
        headers=headers,
        method=method,
    )
    try:
        with urlopen(request, timeout=10) as response:
            return json.loads(response.read().decode("utf-8"))
    except HTTPError as error:
        detail = error.read().decode("utf-8", errors="replace")
        raise ApiRequestError(
            f"API returned HTTP {error.code}: {detail}"
        ) from error
    except URLError as error:
        raise ApiRequestError(f"Could not reach {API_BASE_URL}: {error.reason}") from error
