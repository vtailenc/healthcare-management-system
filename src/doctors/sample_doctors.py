"""Show a small in-memory directory of fictional doctors."""


def list_doctors():
    return [
        {"id": 1, "name": "Dr. Morgan Demo", "specialty": "Family medicine"},
        {"id": 2, "name": "Dr. Riley Example", "specialty": "Cardiology"},
    ]


if __name__ == "__main__":
    for doctor in list_doctors():
        print(doctor)
