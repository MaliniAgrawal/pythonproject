# pythonproject

def calculate_total_cost(item_details):
    base_cost = item_details.get("base_cost", 0)
    shipping_cost = item_details.get("shipping_cost", 0)
    tax_rate = item_details.get("tax_rate", 0.0)

    total_cost = base_cost + shipping_cost + (base_cost * tax_rate)
    return total_cost




items = {"base_cost": 100, "shipping_cost": 10, "tax_rate": 0.10}

total_cost = calculate_total_cost(items)
print(total_cost)