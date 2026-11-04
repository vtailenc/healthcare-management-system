"""Calculate a fictional invoice total from in-memory line items."""


def calculate_total(line_items):
    return round(sum(item["quantity"] * item["unit_price"] for item in line_items), 2)


if __name__ == "__main__":
    demo_line_items = [
        {"description": "Fictional consultation", "quantity": 1, "unit_price": 75.00},
        {"description": "Fictional screening", "quantity": 2, "unit_price": 12.50},
    ]
    print(f"Fictional demo total: ${calculate_total(demo_line_items):.2f}")
