def clean_price(property, error):
    try:
        price = property["price"]
        if price is None:
            error.append({
                "property_id": property["id"],
                "error": "Price is None"
            })
            return None
        
        elif not isinstance(price,(int, float)):
            try:
                price = float(price)
                property["price"] = price
            except ValueError:
                error.append({
                    "property_id": property["id"],
                    "error": "Price is not a number"
                })
                return None
    except KeyError:
        error.append({
            "property_id": property["id"],
            "error": "Price key is missing"
        })
        return None
    return property    
    