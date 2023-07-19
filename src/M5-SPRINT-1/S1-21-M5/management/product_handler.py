from menu import products


def get_product_by_id(id):
    if type(id) != int:
        raise TypeError("product id must be an int")
    for product in products:
        if product["_id"] == id:
            return product
    return {}


def get_products_by_type(product_type):
    if type(product_type) != str:
        raise TypeError("product type must be a str")

    product_list = []

    for product in products:
        if product["type"] == product_type:
            product_list.append(product)
    return product_list


def add_product(menu, **item):
    biggest_id = 0

    for product in menu:
        if product["_id"] > biggest_id:
            biggest_id = product["_id"]

    new_product = {"_id": biggest_id + 1}
    new_product.update(item)
    menu.append(new_product)
    return new_product


def menu_report():
    product_count = len(products)
    total_price = 0

    for item in products:
        total_price += item["price"]

    average_price = round((total_price / product_count), 2)
    most_common_type = products[0]["type"]

    for item in products:
        if products.count(item["type"]) > products.count(most_common_type):
            most_common_type = item["type"]
    return f"Products Count: {product_count} - Average Price: ${average_price} - Most Common Type: {most_common_type}"
