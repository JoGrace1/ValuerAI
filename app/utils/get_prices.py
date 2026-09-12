def get_prices(properties: list[dict]) -> list[float]:
    price_list = []
    for property in properties:
        try:
            price = property["price"]
        except KeyError:
            print(f"Property {property['id']} does not have a price key.")
            continue

        if price is None:
            print(f"Property {property['id']} does not have a price key.")
            continue
        
        if not isinstance(price,(int, float)):
            print(f"Property {property['id']} has an invalid price.")
            continue
        
        price_list.append(price)

    return price_list    

def price_evaluation2(properties):
    price_list = [
        property["price"]
        for property in properties
    ]
    return price_list