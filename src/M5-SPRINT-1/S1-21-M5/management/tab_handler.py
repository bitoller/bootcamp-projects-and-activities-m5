from menu import products


def calculate_tab(list):
    total = []

    for product in products:
        for item in list:
            if product["_id"] == item["_id"]:
                total.append(product["price"] * item["amount"])
    return {"subtotal": f"${round(sum(total), 2)}"}
