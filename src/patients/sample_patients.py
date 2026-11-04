"""Show a small in-memory list of fictional patients."""


def list_patients():
    return [
        {
            "id": 1,
            "name": "Alex Example",
            "date_of_birth": "1990-01-01",
            "email": "alex@example.test",
        },
        {
            "id": 2,
            "name": "Jamie Sample",
            "date_of_birth": "1985-06-15",
            "email": "jamie@example.test",
        },
    ]


if __name__ == "__main__":
    for patient in list_patients():
        print(patient)
