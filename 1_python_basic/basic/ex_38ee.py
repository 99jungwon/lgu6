orders = [
    {
        "country": "USA",
        "customers": [
            {
                "customer_id": "C001",
                "orders": [
                    {"product": "Laptop", "quantity": 1, "unit_price": 1200},
                    {"product": "Mouse", "quantity": 2, "unit_price": 25}
                ]
            },
            {
                "customer_id": "C002",
                "orders": [
                    {"product": "Smartphone", "quantity": 1, "unit_price": 800}
                ]
            }
        ]
    },
    {
        "country": "Canada",
        "customers": [
            {
                "customer_id": "C003",
                "orders": [
                    {"product": "Laptop", "quantity": 2, "unit_price": 1150},
                    {"product": "Keyboard", "quantity": 1, "unit_price": 100}
                ]
            }
        ]
    }
]



result = {
    "C001": {
        "country": "USA",
        "products": ["Laptop", "Mouse"],
        "total_amount": 1250  # (1 x 1200) + (2 x 25)
    },
    "C002": {
        "country": "USA",
        "products": ["Smartphone"],
        "total_amount": 800
    },
    "C003": {
        "country": "Canada",
        "products": ["Laptop", "Keyboard"],
        "total_amount": 2400  # (2 x 1150) + (1 x 100)
    }
}

def order_by_customers(orders):
    result = {}
    for order in orders:
        for cus in order["customers"]:
            temp_list = []
            total = 0
            for pro in cus["orders"]:
                temp_list.append(pro["product"])
                total += (pro["quantity"] * pro["unit_price"])
                result[cus["customer_id"]] = {
                    "country" : order["country"],
                    "products" : temp_list,
                    "total_amount" : total
                }

# products = [ order['product'] for order in customer['quantity]]
# total_amount = sum(
#   [
#       order['unit_price]*order['quantity] for order in customer['orders']
#   ]
#)

    return result

print(order_by_customers(orders))

